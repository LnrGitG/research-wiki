_Critical Finance Review_ , 2012, 1: 59–101 

# **Capital Structure Choices** 

Eugene F. Fama<sup>1</sup> and Kenneth R. French<sup>2</sup> 

> 1 _Booth School of Business, University of Chicago_ 

> 2 _Amos Tuck School of Business, Dartmouth College_ 



### ABSTRACT 

We examine three pairs of cross-section regressions that test predictions of the tradeoff model, the pecking order model, and models that center on market conditions. The regressions examine (i) the split of new outside financing between share issues and debt, (ii) the split of new debt financing between short-term and long-term, and (iii) the split of new equity financing between share issues and retained earnings. The pecking order does well until the early 1980s, when the share issues that are its bane become common. The adjustment of leverage to target predicted by the tradeoff model and the response of equity financing to market valuations predicted by the market conditions model have statistically detectable but rather second-order effects on the split of new outside financing between share issues and debt. Targets for shortterm debt seem to influence the mix of short-term versus long-term debt choices of smaller firms, but this targeting effect is weak to non-existent for large firms. Sticky dividends plague the predictions of the pecking order and market conditions models about the split of equity financing between share issues and retained earnings. 



ISSN 2164-5744; DOI 10.1561/103.00000002 ⃝c 2012 E. F. Fama and K. R. French 

_Fama and French_ 

_60_ 

## **1 Introduction** 

We test the predictions of three common models for the financing decisions of firms — the tradeoff model, the pecking order model, and the market conditions model. The central prediction of the tradeoff model is that firms have leverage targets and leverage tends to return to its target. The pecking order model, as framed by Myers (1984) and Myers and Majluf (1984), predicts that because of asymmetric information problems that are more severe for riskier securities, firms prefer to finance with retained earnings, outside financing is primarily debt rather than new shares, and debt financing is primarily short-term. Pecking order financing can also arise for other reasons, for example, issuing costs that are zero for retained earnings, low for short-term debt, and highest for share issues. 

The market conditions model has several variants. They share the prediction that firms with high prices relative to a fundamental like book value issue more new shares. The market-timing version of the model is an offshoot of the behavioral story for the value premium in average stock returns. Debondt and Thaler (1985) and Lakonishok _et al._ (1994) argue that growth stocks (characterized by high ratios of stock price to book value, _P/B_ ) tend to be overvalued and low _P/B_ value stocks tend to be undervalued. Gradual price corrections produce the value premium, that is, low average returns for growth stocks and high average returns for value stocks. If growth stocks are overvalued, it seems reasonable that the debt of growth firms is also likely to be overvalued, with long-term debt more overvalued than shortterm debt (Myers and Majluf, 1984). 

In the market-timing model, managers use financing decisions to take advantage of the slow correction of pricing errors. High _P/B_ growth firms prefer share issues (to take advantage of stock prices that are too high) over new debt or retained earnings. When growth firms issue debt, they favor (more overvalued) long-term debt over short-term debt. Repurchases of overpriced shares are a bad investment for growth firms, but dividends are attractive because, holding total assets fixed, they allow growth firms to issue overvalued securities. For low _P/B_ value firms, everything reverses. Retained earnings are the cheapest financing, followed by slightly underpriced short-term debt, then by more underpriced long-term debt, with most underpriced outside equity last in line. Repurchases of undervalued shares are attractive for value firms, but dividends have high opportunity cost. 

_Capital Structure Choices_ 

_61_ 

Baker and Wurgler (2002) are strong proponents of the market-timing story, which we also label the mispricing model. 

Other models that center on market conditions but do not rely on mispricing also predict a positive relation between equity financing and _P/B_ . For example, with rational pricing, high _P/B_ is a signal of some combination of high expected future cashflows to equity and low discount rates for the cashflows, that is, a low cost of equity capital. Suppose security prices are rational and the capital structure irrelevance theorem of Modigliani and Miller (1958) holds. In this scenario, a low cost of equity capital does not imply that equity is cheaper than other forms of financing. Suppose, however, managers respond to higher _P/B_ with new share financing because they mistakenly believe higher _P/B_ signals a low relative cost of equity. The mistaken belief might arise, for example, because managers do not understand the MM theorem or because they falsely believe _P/B_ signals mispricing. The positive relation between _P/B_ and share financing is then what Miller (1977) calls a neutral mutation: benign behavior that signals nothing about the cost of share issues relative to other forms of financing or about mispricing. This version of the market conditions model is consistent with evidence that capital structure choices have only a moderate impact on the value of most firms (see the excellent review by Graham and Leary, 2011) and with evidence that manager characteristics affect capital structure choices (Bertrand and Schoar, 2003; Graham and Narasimhan, 2004; Lewellen, 2006; Cronqvist _et al._ , 2010). 

The line between the pecking order model of Myers and Majluf (1984) and the mispricing version of the market conditions model is also blurry. In developing the theoretical underpinnings of their model, Myers and Majluf (1984) argue that asymmetric information problems are less severe for firms with obvious growth opportunities. This implies that with appropriate controls for other pecking order explanatory variables, growth firms, which typically have higher _P/B_ , use more new share financing — the prediction of the mispricing model and other variants of the market conditions model. 

In short, a positive relation between _P/B_ and share issues is predicted by many models, some based on irrational pricing and some that assume rational pricing. We classify all these models under the rubric, market conditions models (a label we owe to a referee). Because the relation between security issues and _P/B_ does not in itself allow us to distinguish among market 

_Fama and French_ 

_62_ 

conditions models or between these and the pecking order model of Myers and Majluf (1984), cautious interpretation of the _P/B_ results is in order. 

An important contribution of this paper is a new regression framework that allows us to nest, in a simple way, tests of the tradeoff, pecking order, and market conditions models. We use three pairs of cross-section regressions that focus on (i) the split of total new outside financing between share issues and debt, (ii) the split of new debt financing between short-term and long-term, and (iii) the split of total new equity financing between retained earnings and share issues. Each regression pair imposes a different form of the cashflow constraint linking sources and uses of funds, and imposition of the constraint means the two regressions in a pair are complementary, in a sense that becomes clear. 

The basic cashflow constraint is, 



In Equation (1), _dSt_ is the book value of (equivalently, the proceeds from) common stock issued during the fiscal year ending in calendar year _t, dL t_ is the change in liabilities including preferred stock, _dAt_ is total investment (the change in total assets), _Dt_ is dividends paid, and _Yt_ is earnings, all for the same fiscal year _t_ . The cashflow constraint in (1) says that total new outside financing, _dSt_ + _dL t_ , must cover the demand for financing from investment and dividends less the supply of financing from earnings. (The Appendix gives details on the measurement of the variables.) 

The first two regressions focus on how firms split total new outside financing between share issues and debt, _dSt_ and _dL t_ . The explanatory variables include _dAt_ , _Dt_ , and _Yt_ , the variables on the right side of the cashflow constraint (1). This means the two regressions are complementary: the sum of the slopes on _Yt_ in the _dSt_ and _dL t_ regressions must be minus one, the slopes on _dAt_ must sum to one, and the sum of the slopes on _Dt_ is also one. The slopes on the cashflow variables in the two cross-section regressions thus measure the average split of an additional dollar of earnings between lower share issues and lower debt issues, and the average splits of the financing of investment and dividends between new shares and debt. The slopes on the cashflow variables in the _dSt_ and _dL t_ regressions provide our evidence on the pecking order prediction that new outside financing is primarily debt. 

To test the tradeoff model’s prediction that leverage reverts to its target, the _dSt_ and _dL t_ regressions also include the lagged leverage surplus, _LSt_ −1, 

_Capital Structure Choices_ 

_63_ 

the difference between actual and target leverage at the end of the fiscal year ending in calendar year _t_ − 1, as an explanatory variable. In line with the tradition in the market timing literature (see the reviews of Baker _et al._ , 2007 or Eckbo _et al._ , 2007), the regressions also include the lagged price to book ratio, _P/Bt_ −1, as an explanatory variable. We interpret the _P/Bt_ −1 slopes more broadly, as evidence on market conditions models in general and on the Myers-Majluf version of the pecking order model. In the regressions to explain new outside debt and equity financing, the _P/Bt_ −1 slopes tell us whether, as predicted by these models, higher _P/Bt_ −1 pushes outside financing away from debt toward share issues, and the _LSt_ −1 slopes tell us whether, as predicted by the tradeoff model, a larger leverage surplus leads to less new debt. 

With the control for total required outside financing provided by the investment, dividend, and earnings explanatory variables, the cashflow constraint (1) implies that the slopes for _P/Bt_ −1 or _LSt_ −1 must sum to zero in the _dSt_ and _dL t_ regressions. In other words, imposition of the cashflow constraint on the regressions means additional share issues in response to higher _P/Bt_ −1 or higher _LSt_ −1 imply an exact offset in debt financing — an additional dollar of shares is a dollar less of debt. 

The second pair of regressions focuses on the split of total new debt financing, _dL t_ , between short-term and long-term debt, _dSTDt_ and _dLTDt_ . For these tests, we move stock issues to the right side of the cashflow constraint, 



This form of the constraint says total new debt, _dSTDt_ + _dLTDt_ , must equal the demand for financing from investment and dividends minus the supply of financing from earnings and stock issues. 

The explanatory variables in the _dSTDt_ and _dLTDt_ regressions include the variables on the right side of the cashflow constraint (2). Because we impose (2), the two regressions treat the quantity of new debt as fixed and focus on the split between short-term and long-term. We use these regressions to test the pecking order prediction that firms prefer short-term to longterm debt and the market conditions prediction that higher _P/Bt_ −1 leads firms to use long-term rather than short-term debt. We also test a simple extension of the tradeoff model that implies firms have a target for the ratio of short-term debt to total debt. The _dSTDt_ and _dLTDt_ regressions are again complementary; specifically, the slopes for _dAt_ sum to one, the sum of the 

_Fama and French_ 

_64_ 

slopes for _Dt_ is one, the slopes for each of _Yt_ and _dSt_ sum to minus one, and the slopes for any additional variable sum to zero. 

The last pair of regressions focuses on the split of new equity financing between share issues and retained earnings. We take earnings as given, so firms alter retained earnings by adjusting dividends. To isolate the share issue/dividend decision, we express the cashflow constraint as 



and we include investment, earnings, and new debt issues as explanatory variables in regressions that explain share issues and dividends. 

If the proceeds from share issues are not used to pay dividends or repurchase debt, _dSt_ shows up in _dAt_ , the change in total assets including cash. Thus, with controls for total investment, earnings, and the change in liabilities on the right side of (3), by including _P/Bt_ −1 as an explanatory variable in the _dSt_ and _Dt_ regressions, we test the prediction of the market conditions model that higher _P/Bt_ −1 also makes firms willing to pay more current dividends to absorb the proceeds from share issues. The two regressions also shed light on the prediction of a strong version of the pecking order model that firms vary dividends to finance with low cost retained earnings. 

Our main findings are easily summarized. 

- (1) The first two regressions, which explain the split of total new outside financing between shares and debt, provide reliable evidence that, as predicted by the tradeoff model, firms tend to adjust the mix of new equity and debt to move toward target leverage. The magnitude of the effect is, however, typically small. Thus, our results reinforce earlier evidence that leverage targets are generally not a first-order consideration in financing decisions (e.g., Shyam-Sunder and Myers, 1999; Graham and Harvey, 2001; Fama and French, 2002; Welch, 2004; Iliev and Welch, 2010; DeAngelo and Roll, 2011; Hovakimian and Li, 2011). 

- (2) The second pair of regressions, which explains the split of new debt financing between short-term and long-term, tests the extended tradeoff model’s prediction that firms have a target mix of short-term and long-term debt. We find that when issuing debt, microcaps (firms with stock market capitalization below the 20th NYSE percentile) and small firms (market capitalization between the 20th and 50th NYSE percentile) do tend to move toward a target short-term/long-term mix, and for microcaps the magnitude of the effect is large. This tradeoff effect is weak to non-existent for big stocks. 

_65_ 

_Capital Structure Choices_ 

- (3) All three pairs of regressions provide some evidence that supports the market conditions model. In statistical terms the support ranges from strong to weak, and in economic terms the effects are generally small. There is strong statistical evidence that higher _P/Bt_ −1 firms allocate more new outside financing to share issues, but variation in the mix of new debt and equity in response to _P/Bt_ −1 is typically modest. As predicted by the market conditions model, there are hints in our tests that more of the new debt financing of higher _P/Bt_ −1 firms is long-term during 1963–1982, but there is little evidence of this behavior during 1983–2009. Finally, our tests suggest that higher _P/Bt_ −1 firms pay more dividends so they can issue more new shares, but the statistical reliability of this inference is not overwhelming, and the variation of new shares linked to dividends is tiny. 

- (4) The pecking order model predicts that firms favor debt over share issues for new outside financing and they favor short-term over longterm debt. The cashflow control variables in the first pair _(dSt_ and _dL t )_ and second pair _(dSTDt_ and _dLTDt )_ of regressions isolate these specific financing decisions and so provide direct tests of the pecking order. The prediction that variation in investment, dividends, and earnings is absorbed more by debt than by share issues fares well during 1963–1982. Stock issues and repurchases are more common after 1982 (Fama and French, 2005), however, and in the 1983–2009 tests, share issues absorb about as much cashflow variation as debt. The _dSTDt_ and _dLTDt_ regressions provide no support for the pecking order prediction that firms favor short-term debt. Contrary to the model, long-term debt typically absorbs more of the variation in cashflow variables than short-term debt. 

What is our contribution? The regression to explain total debt issues has precedents in Shyam-Sunder and Myers (1999) and in especially Frank and Goyal(2003).Ataminimum,however,examiningthecomplementaryregression to explain share issues expands the perspective provided by the debt regression. The regressions to explain the split of debt financing between short-term and long-term, and the regressions to explain the split of equity financing between retained earnings and share issues are novel, but one can argue that they address less central predictions of the tradeoff, pecking order, and market conditions models. As in most empirical research, some of our results are predictable from earlier studies that use different approaches. We judge that our tests provide interestingnewresults,as wellas newperspective 

_Fama and French_ 

_66_ 

on existing results. And our regression framework — three pairs of complementary regressions that nest tests of the tradeoff, pecking order, and market conditions models in a simple unified structure — is a contribution that can provide the foundation for much future work. 

We first discuss (in Section 2) the regressions to explain share issues and new debt. Section 3 examines the split of debt financing between short-term and long-term, and Section 4 takes up share issues and dividends (retained earnings). In each case, we discuss the logic of the regressions and then turn to the results. A summary and conclusions are in Section 5. 

## **2 Share Issues versus New Debt** 

### **2.1 The Logic of the Regressions** 

The regressions that examine the split of new outside financing between share issues, _dSt_ , and debt, _dL t_ , build on the cashflow constraint in Equation (1), which says new outside financing must cover the demand for financing from investment and dividends less the supply of financing from earnings. Suppose that for each year _t_ in our sample we estimate two crosssection regressions for individual firms: new equity, _dSt_ , regressed on the change in assets, _dAt_ , dividends, _Dt_ , and earnings, _Yt_ , and new debt, _dL t_ also on _dAt_ , _Dt_ , and _Yt_ . The cashflow constraint (1) holds firm-by-firm and year-by-year. Thus, because we include asset growth, dividends, and earnings as explanatory variables, the sum of each year’s regressions to explain _dSt_ and _dL t_ must reduce to _dAt_ + _Dt_ − _Yt_ . Specifically, the sum of the intercepts in the _dSt_ and _dL t_ regressions must be zero every year, the slopes for _Yt_ must sum to minus one, and the sums of the slopes for _dAt_ and _Dt_ must each be one. These constraints on the intercept and the slopes for _Yt_ , _dAt_ , and _Dt_ continue to hold if we add other explanatory variables to both regressions, and like the intercepts, the slopes for each additional explanatory variable must sum to zero in the two annual regressions. 

There are two primary additional explanatory variables in the _dSt_ and _dL t_ regressions. The first is the lagged price-to-book ratio, _P/Bt_ −1, which is market capitalization (market cap) at the end of December of year _t_ −1 over book equity for the fiscal yearend in _t_ − 1. The second is the lagged leverage surplus, _LSt_ −1, defined as the difference between leverage and target leverage for year _t_ − 1, where leverage is the ratio of book liabilities (including 

_Capital Structure Choices_ 

_67_ 

preferred stock) to book assets for _t_ − 1, and where target leverage is the _t_ − 1 value-weight leverage ratio for the firm’s industry (see Appendix for details). Thus, ignoring other variables added later and using notation that accounts for the constraints on the coefficients and residuals implied by (1), the two regressions estimated each year are, 



In economic terms, the slopes for investment, dividends, and earnings in the two regressions provide estimates of how, on average, required outside financing due to variation in these variables across firms splits between share issues and debt. The slopes for the price-to-book ratio and the lagged leverage surplus then tell us how they push the allocation of outside financing away from the averages. 

Using lagged industry leverage to proxy for target leverage is crude, but the alternatives we have tried (equal-weight industry leverage for _t_ − 1, average equal-weight or value-weight industry leverage for the five years from _t_ −1 to _t_ −5, the firm’s average leverage for _t_ −1 to _t_ −5, and the average leverage of all firms for _t_ − 1) produce similar results on the reversion of leverage to its target. Our inferences about reversion to target are also similar to those from more ambitious cross-section regression approaches that attempt to capture the effects of a wide range of explanatory variables for target leverage suggested by variants of the tradeoff model (see, for example, Fama and French, 2002 or the review of Parsons and Titman, 2008). We focus on book leverage because the results in Welch (2004) suggest that firms do not respond much to variation in market leverage due to changes in stock prices. We have, however, replicated our results using market leverage, and as in Fama and French (2002), estimates of the rate of reversion of leverage to its target are similar for book and market leverage. Rampini and Viswanathan (2010), Rauh and Sufi (2010), and Welch (2011) suggest that non-debt liabilities, such as operating leases, should be included in measures of leverage. We leave such refinements to future work. 

There are also alternatives to _P/Bt_ −1 as a measure of market conditions. Cumulative lagged returns are a common choice. Rhodes-Kropf _et al._ (2005) and Polk and Sapienza (2009) propose other measures. DeAngelo _et al._ (2010) examine the performance of different market conditions variables as predictors of seasoned equity offerings. They find that combining measures 

_Fama and French_ 

_68_ 

provides some enhancement of explanatory power, but in economic terms not much seems to be gained. We choose to go with timeworn _P/Bt_ −1 (the popular choice in the literature) as the sole measure of market conditions, leaving enhancements to future work. 

We use regressions (4) and (5) to shed light on tradeoff, pecking order, and market conditions predictions about the split of outside financing between debt and equity. The slopes for the cashflow variables provide evidence on the pecking order prediction that new outside financing is primarily debt. Thus, the slopes for investment, earnings, and dividends should be further from zero in the new debt regression (5) than in the new shares regression (4). 

In the tradeoff model, leverage tends to return to its target. The prediction is that higher leverage relative to target should, on average, lead firms to substitute away from debt toward equity for outside financing. Thus, the slope for the leverage surplus, _LSt_ −1, should be positive in regression (4) to explain share issues and negative in the debt regression (5). 

As a test for the reversion of leverage to its target, the novelty of regressions (4) and (5) is the cashflow controls. For example, if pecking order forces also affect financing decisions, variation in leverage in response to cashflows may obscure tradeoff forces that push leverage toward its target. The cashflow controls in our regressions should, however, capture pecking order (and other) effects, allowing the slopes for the leverage surplus to produce cleaner estimates of the rate at which leverage reverts to target. Moreover, the constraint on outside financing in Equation (1) implies that, with the cashflow controls, the sum of the slopes on the lagged leverage surplus in regressions (4) and (5) is zero. The slopes for _LSt_ −1 thus produce dollar-for-dollar estimates of how a larger leverage surplus leads firms to substitute share issues for debt. 

The slopes for the lagged price-to-book ratio, _P/Bt_ −1, in regressions (4) and (5) test the prediction of the market conditions model that managers perceive high _P/Bt_ −1 as a signal that the cost of outside equity is low relative to other forms of financing, so high _P/Bt_ −1 growth firms are more likely to meet required outside financing with share issues rather than debt. Using _P/Bt_ −1 to capture these effects is standard. The cashflow control variables in (4), however, allow the slopes on _P/Bt_ −1 to provide sharper tests of the market conditions model. For example, most of the variation in _P/Bt_ −1 across firms is caused by differences in expected growth rather than differences 

_Capital Structure Choices_ 

_69_ 

in expected return (Cohen _et al._ , 2003). High _P/Bt_ −1 growth firms tend to grow more quickly than low _P/Bt_ −1 value firms. Since investment must be financed, if we did not include the cashflow variables in regressions (4) and (5), we would likely find that high _P/Bt_ −1 is associated with more new debt and more new shares, and any effect of market conditions on outside financing would be at least partially obscured. Regressions (4) and (5) address this problem by controlling for required outside financing, that is, the demand for financing from investment and dividends and the supply of financing from earnings. 

Finally, our cross-section regressions impose the same slopes for explanatory variables on all firms, and this warrants careful interpretation of the results. For example, the cashflow slopes in (4) and (5) measure how, on average (that is, across firms), the financing of variation in investment, dividends, and earnings splits between share and debt issues. Likewise, the slopes on _P/Bt_ −1 measure how, on average, higher _P/Bt_ −1 pushes the split of outside financing toward equity and away from debt. Estimates of average effects are informative about overall responses, but they are surely inaccurate for some individual firms. We can envision extensions of the regressions that allow the slopes to vary across firms, for example, via interaction variables. Here we stay with simple transparent functional forms to illustrate the complementary regression approach; we leave extensions for future work. 

### **2.2 Regression Results** 

The two regressions we actually estimate are minor enhancements of (4) and (5), specifically, 



The dependent variable, _dFt_ , is either _dSt_ , the book value of (proceeds from) shares issued during the fiscal year ending in calendar year _t_ , or _dL t_ , the change in liabilities. We estimate different slopes for negative and positive earnings, _NegY t_ and _PosY t_ , to allow for the possibility that debt is more difficult to issue for firms with negative earnings. Like earlier researchers, we include _MCt_ , the log of market cap in June of _t_ , to allow for differences in financing as a function of size. We also include a dummy variable for 

_Fama and French_ 

_70_ 

firms that pay no dividends during fiscal year _t_ , _NoDt_ , and a dummy for firms with negative book equity, _NegBt_ −1. Except for _MCt_ , _P/Bt_ −1, _LSt_ −1, _NegBt_ −1, and _NoDt_ , all the variables in the year _t_ estimates of regression (6) (and regressions reported later) are scaled by year _t_ total assets. 

In the spirit of Fama and MacBeth (1973), we estimate regression (6) year by year for 1963–2009 and draw inferences from averages of the annual slopes and _t_ -statistics for the averages. This is a simple way to produce standard errors of the average slopes that allow for any within year crosscorrelation of the regression residuals. Autocorrelation of the annual slopes is also a potential problem, but skipping the details, we can report that the problem is not serious, probably because the dependent variables in the regressions are year-to-year changes. 

To reduce the influence of outliers, the annual samples are trimmed. The estimates of regression (6), for example, exclude 0.5% of the observations in the right tails of the explanatory variables _PosY t_ , _Dt_ , _P/Bt_ −1, and _LSt_ −1, and 0.5% of the observations in the left tails of _dAt_ and _NegYt_ . Because extreme observations tend to be correlated across variables, trimming results in small reductions in sample sizes. More important, we can report that trimming reduces the standard errors of the average slopes, thus enhancing the information from the regressions. 

Bagwell and Shoven (1989) find that share repurchases surge after 1982. Fama and French (1995) find that the profitability of small firms declines in the early 1980s. We split our 1963–2009 sample in 1983 to accommodate these results. Formal tests (Appendix Table A1) suggest that the true regression slopes for the two periods differ, so we do not show results for the full 1963–2009 period. 

We also report separate results for microcap firms (market cap below the NYSE 20th percentile), small firms (between the 20th and 50th NYSE market cap percentiles), and big firms (above the 50th NYSE percentile). The sample includes NYSE and Amex stocks, with Nasdaq stocks added in 1973. On average 51% of the firms in the sample are microcaps during 1963–1982 and 62% are microcaps during 1983–2009 (Table 1). We partition the sample into three size groups to prevent the large number of tiny stocks from dominating the economically more important large stocks in the regressions. We do not show results for the full sample because formal tests (Appendix Table A2) suggest that the true regression slopes differ across the three size groups. 

_71_ 

_Capital Structure Choices_ 







|_STSt_−1|0.12<br>0.24|0.06|0.22|0.04<br>0.19|0.17<br>0.27|0.08|0.24|0.04<br>0.21|r table|
|---|---|---|---|---|---|---|---|---|---|
|_LSt_−1|−0_._04<br>0_._19|−0_._05|0_._17|−0_._04<br>0_._14|−0_._13<br>0_._26|−0_._12|0_._22|−0_._07<br>0_._19|page fo|
|_P/Bt_−1|1.67<br>1.94|1.87|1.81|2.12<br>1.81|2.72<br>4.26|3.10|3.85|3.37<br>3.80|ee next|
|_NegBt_−1|0.01<br>0.08|0.00|0.05|0.00<br>0.04|0.04<br>0.19|0.02|0.13|0.01<br>0.11|ables. (S|
|_MCt_|2.36<br>0.88|4.23|0.34|6.12<br>0.98|3.53<br>1.16|5.96|0.39|7.94<br>1.01|s vari|
|_Dt_|1.13<br>1.56|1.99|1.68|2.69<br>1.79|0.34<br>1.10|0.89|1.48|1.67<br>1.76|ession|
|_NoDt_|0.48<br>0.50|0.18|0.38|0.06<br>0.24|0.84<br>0.37|0.57|0.48|0.30<br>0.43|he regr|
|_PosYt_|1982<br>5.14<br>4.34|6.53|4.18|6.89<br>3.83|2009<br>3.25<br>4.79|5.59|5.20|6.55<br>5.21|) of t|
|_NegYt_|1963–<br>−1_._51<br>4_._97|−0_._29|1_._78|−0_._09<br>0_._84|1983–<br> −14_._83<br>30_._42|−3_._81|12_._59|−1_._39<br>6_._88|Std Dev|
|_dAt_|7_._97<br>17_._04|11_._79|13_._19|11_._16<br>9_._95|−1_._10 <br>33_._97|11_._10|22_._02|9_._75<br>18_._68|tions (|
|_dLTDt_|2_._11<br>9_._34|3_._40|8_._27|3_._42<br>6_._31|0_._94<br>16_._53|2_._92|12_._80|2_._88<br>10_._49|devia|
|_dSTDt_|2_._43<br>10_._78|2_._85|6_._90|2_._53<br>4_._79|1_._72<br>16_._88|2_._52|8_._54|2_._16<br>6_._54|tandard|
|_dLt_|4_._53<br>13_._99|6_._25|10_._67|5_._96<br>8_._01|2_._66<br>21_._63|5_._44|15_._30|5_._04<br>12_._79|and s|
|_dSt_|0_._94<br>5_._61|1_._28|5_._31|1_._09<br>3_._86|8_._16<br>23_._06|4_._77|15_._30|1_._23<br>11_._08|ns (Ave)|
|Firms|1242|442||581|2375|768||705|. Mea<br>ion.)|
||icro<br>ve<br>td Dev|mall<br>ve|td Dev|ig<br>ve<br>td Dev|icro<br>ve<br>td Dev|mall<br>ve|td Dev|ig<br>ve<br>td Dev|**able 1** <br>escript|
||M<br>A<br>S|S<br>A|S|B<br>A<br>S|M<br>A<br>S|S<br>A|S|B<br>A<br>S|**T**<br>d|



_Fama and French_ 

_72_ 

**Table 1 Description:** We use CRSP and Compustat data for non-financial NYSE, Amex, and (after 1972) Nasdaq firms with fiscal yearends in calendar year _t_ , 1963–2009. The variables are: _dSt_ , the book value of common shares issued during the fiscal year ending in _t_ ; _dLt_ , the change in liabilities, including preferred stock, in fiscal year _t_ ; _dSTDt_ , the change in short-term debt (current liabilities, excluding longterm debt in current liabilities) in fiscal year _t_ ; _dLTDt_ , the change in long-term debt, including preferred stock and long-term debt in current liabilities, in fiscal year _t_ ; _dAt_ , the change in total assets in fiscal year _t_ ; _NegY t_ and _PosYt_ , earnings for firms with negative and positive earnings for fiscal year _t_ ; _NoDt_ , a dummy variable for firms that do not pay dividends in _t_ ; _Dt_ , total dividends paid in fiscal year _t_ ; _MCt_ , the log of market cap in June of _t_ ; _NegBt_ −1, a dummy variable for firms with negative book equity; _P/Bt_ −1, the ratio of market cap for December of _t_ − 1 to book equity for the fiscal yearend in _t_ − 1, for firms with positive book equity; _LSt_ −1, the difference between leverage and target leverage for year _t_ − 1, where leverage is the ratio of book liabilities including preferred stock to book assets for _t_ − 1 and target leverage is the _t_ − 1 value-weight average leverage ratio for the firm’s industry; and _STSt_ −1, the difference between the short-term debt ratio and the target ratio for year _t_ − 1, where the short-term ratio is current liabilities, excluding long-term debt in current liabilities, divided by total liabilities for _t_ − 1 and the target short-term ratio is the _t_ − 1 value-weight average for the firm’s industry. Except for _MCt_ , _P/Bt_ −1, _LSt_ −1, _STSt_ −1, and the two dummy variables, the variables are scaled by assets at the end of year _t_ . The table shows separate results for microcap firms (Micro, market cap in June of year _t_ below the 20th NYSE percentile), small firms (Small, between the 20th and 50th NYSE percentiles), and big firms (Big, above the 50th percentile), and for 1963–1982 and 1983–2009. The annual samples match those used to estimate regression (4), in Table 2; we delete 0.5% of the observations in the right tails of _PosYt_ , _Dt_ , _P/Bt_ −1, and _LSt_ −1, and 0.5% of the observations in the left tails of _dAt_ and _NegY t_ . 

We first examine what the regression slopes for the cashflow variables say about the pecking order model. We then turn to the evidence on the reversion of leverage to target predicted by the tradeoff model. The final step is to discuss what the regressions tell us about the market conditions model. 

**The Pecking Order Model** — In the pecking order model, outside financing in response to variation in investment, earnings, and dividends is primarily debt. This prediction fares best in the regressions for 1963–1982, where share issues on average absorb between 7% and 33% of the marginal variation in _dAt_ , _NegY t_ , _PosY t_ , and _Dt_ , with the rest (67% to 93%) met by debt (Table 2). The regressions for 1983–2009 are a different matter. In the _dSt_ regressions, the average slopes for investment, dividends, and earnings typically more than double from 1963–1982 to 1983–2009, which implies a corresponding decline in the magnitude of the slopes in the _dL t_ regressions. New share issues on average absorb much less than half the variation in the cashflow variables during 1963–1982, but for 1983–2009 equity and debt are on more equal footing. The tests in Appendix Table A1 say that the changes in the average slopes from 1963–1982 to 1983–2009 signal changes in the true slopes. 

_Capital Structure Choices_ 

_73_ 

The summary statistics in Table 1 confirm that during 1963–1982, most outside financing is debt. For each of the three size groups, the average value of _dL t_ is roughly five times the average _dSt_ . New share financing is more important during 1983–2009, particularly among microcap and small stocks. The average value of _dSt_ for small stocks increases from 1.28% of assets in 1963–1982 to 4.77% in 1983–2009, and the average for microcaps increases from 0.94% to 8.16%. The summary statistics and regressions confirm the inference of Fama and French (2002, 2005) and Frank and Goyal (2003) that the pecking order model is less tenable in recent years because of the increased frequency of share issues. 

Other features of the results in Table 2 are worth noting. For example, the average _NegYt_ and _PosY t_ slopes for big firms in the _dSt_ regressions for 1983–2009 are −0.48 and −0.53. Thus, given investment and dividends, the increase in share issues to cover a marginal dollar of negative earnings is on average close to the reduction in response to a dollar of positive earnings. But for microcaps, share issues during 1983–2009 respond more to negative earnings. This suggests that during 1983–2009 debt is more costly to issue for microcap firms with negative earnings. The results for 1963– 1982, however, do not confirm this conclusion. 

The _NoDt_ variable in (6) also produces an interesting result. Firms that do not pay dividends tend to issue more equity and less debt. The incremental share issues of non-payers are large, especially during 1983–2009, when they average 1.34%, 1.85%, and 1.71% of assets per year for microcap, small, and big firms (Table 2). Firms with negative book equity also tend to issue more stock. Negative book equity has a particularly large impact on the debt-equity choice of smaller firms during 1983–2009; the average annual incremental shift toward share issues is 6.58% of assets for small firms and 11.16% for microcaps. Firms that do not pay dividends or have negative book equity apparently differ from other firms in ways that affect financing decisions and are not captured by the other variables in (6). 

In the results for 1963–1982, the market cap variable, _MCt_ , has little explanatory power in the regressions to explain share and debt issues (Table 2). Thus, splitting the sample into microcap, small, and big firms apparently captures most size effects. In the 1983–2009 results, however, there is stronger evidence that in the small and big groups, larger firms tend to issue less equity and more debt. 

_Fama and French_ 

_74_ 

**The Tradeoff Model** — In the tradeoff model, firms have leverage targets, and leverage tends to return to its target. The prediction for outside financing is that a higher leverage surplus leads firms to issue more stock and less debt. In the estimates of (6), the slopes for _LSt_ −1 should be positive in the regressions to explain share issues, which, given the cashflow controls in (6), implies exactly offsetting negative slopes in the paired regressions to explain debt issues. 

Table 2 provides statistically strong evidence that leverage reverts to its target. The average slopes for _LSt_ −1 in the regressions to explain share issues are positive and between 2.44 and 10.49 standard errors from zero for all size groups for 1963–1982 and 1983–2009. The average slopes for microcaps are further from zero than the slopes for small and big firms, particularly during 1983–2009. 

Appendix Table A1 says that for microcaps the true average rate at which leverage reverts to target during 1983–2009 is almost surely higher than the rate for 1963–1982. In contrast, for small and big firms the average _LSt_ −1 

Table 2 — Part A: Regressions to explain _dSt_ 

||_at_|_dAt_|_NegY_|_PosYt_|_NoDt_|_Dt_|_MCt_|_NegB_1|_P/Bt_−1|_LSt_−1|_R_<sup>2</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||_t_||1963|–1982||_t_−||||
|Micro||||||||||||
|Coef|−1_._16|0_._14|−0_._17|−0_._15|0.59|0_._32|0_._08|1_._00|0_._41|2_._98|0.21|
|_t_-stat|−5_._32|8_._18|−6_._44|−5_._46|3.69|7_._80|1_._48|0_._82|7_._05|7_._15||
|Small||||||||||||
|Coef|−1_._40|0_._19|−0_._15|−0_._22|0.71|0_._33|0_._09|2_._80|0_._47|2_._01|0.28|
|_t_-stat|−2_._47|11_._08|−1_._09|−9_._11|2.75|5_._64|0_._59|2_._70|4_._19|3_._79||
|Big||||||||||||
|Coef|−0_._42|0_._20|−0_._07|−0_._21|0.42|0_._24|−0_._06|0_._44|0_._26|1_._46|0.29|
|_t_-stat|−1_._68|17_._98|−1_._03|−7_._50|1.25|6_._96|−1_._88|0_._35|4_._87|3_._78||
||||||1983|–2009||||||
|Micro||||||||||||
|Coef|−2_._23|0_._41|−0_._60|−0_._35|1.34|0_._72|0_._09|11_._16|0_._72|7_._28|0.59|
|_t_-stat|−5_._61|19_._80|−21_._80|−16_._88|9.69|12_._71|1_._12|12_._33|20_._30|10_._47||
|Small||||||||||||
|Coef|3_._02|0_._40|−0_._57|−0_._48|1.85|0_._64|−0_._91|6_._58|0_._57|1_._67|0.54|
|_t_-stat|2_._47|18_._08|−16_._20|−13_._35|6.39|9_._36|−5_._38|4_._82|10_._57|2_._62||
|Big||||||||||||
|Coef|1_._34|0_._37|−0_._48|−0_._53|1.71|0_._38|−0_._37|1_._63|0_._25|1_._72|0.49|
|_t_-stat|2_._38|18_._49|−8_._45|−14_._85|5.24|5_._66|−5_._34|0_._87|4_._13|2_._44||
|||||||||||(_Conti_|_nued_)|







_Capital Structure Choices_ 

_75_ 

Table 2 — Part B: Regressions to explain _dLt_ 

||_at_|_dAt_|_NegYt_|_PosYt_|_NoDt_|_Dt_|_MCt_|_NegBt_−1|_P/Bt_−1|_LSt_−1|_R_<sup>2</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||||1963|–1982||||||
|Micro||||||||||||
|Coef|1_._16|0_._86|−0_._83|−0_._85|−0_._59|0_._68|−0_._08|−1_._00|−0_._41|−2_._98|0.88|
|_t_-stat|5_._32|51_._69|−31_._95|−32_._14|−3_._69|16_._38|−1_._48|−0_._82|−7_._05|−7_._15||
|Small||||||||||||
|Coef|1_._40|0_._81|−0_._85|−0_._78|−0_._71|0_._67|−0_._09|−2_._80|−0_._47|−2_._01|0.82|
|_t_-stat|2_._47|48_._76|−6_._12|−32_._18|−2_._75|11_._45|−0_._59|−2_._70|−4_._19|−3_._79||
|Big||||||||||||
|Coef|0_._42|0_._80|−0_._93|−0_._79|−0_._42|0_._76|0_._06|−0_._44|−0_._26|−1_._46|0.83|
|_t_-stat|1_._68|72_._45|−13_._71|−28_._94|−1_._25|22_._07|1_._88|−0_._35|−4_._87|−3_._78||
||||||1983|–2009||||||
|Micro||||||||||||
|Coef|2_._23|0_._59|−0_._40|−0_._65|−1_._34|0_._28|−0_._09|−11_._16|−0_._72|−7_._28|0.56|
|_t_-stat|5_._61|28_._56|−14_._43|−31_._11|−9_._69|5_._05|−1_._12|−12_._33|−20_._30|−10_._47||
|Small||||||||||||
|Coef|−3_._01|0_._60|−0_._43|−0_._52|−1_._85|0_._36|0_._91|−6_._58|−0_._57|−1_._67|0.58|
|_t_-stat|−2_._47|26_._83|−11_._98|−14_._68|−6_._39|5_._24|5_._38|−4_._82|−10_._57|−2_._62||
|Big||||||||||||
|Coef|−1_._34|0_._63|−0_._52|−0_._47|−1_._71|0_._62|0_._37|−1_._63|−0_._25|−1_._72|0.66|
|_t_-stat|−2_._38|31_._76|−9_._17|−13_._02|−5_._24|9_._19|5_._34|−0_._87|−4_._13|−2_._44||







**Table 2** . Average slopes from estimates of regression (6) to explain the split of new outside financing between share issues and total debt issues. 

The regressions are estimated each year _t_ during 1963–2009 using CRSP and Compustat data for nonfinancial NYSE, Amex, and (after 1972) Nasdaq firms with fiscal yearends in calendar year _t_ . The dependent variable is either _dSt_ (book value of common shares issued during the fiscal year ending in _t)_ or _dLt_ (change in liabilities, including preferred stock, during the fiscal year ending in _t)_ . In addition to the regression intercept _(at )_ the explanatory variables are: _dAt_ , the change in total assets from _t_ − 1 to _t_ ; _NegY t_ and _PosYt_ , earnings for firms with negative and positive earnings for the fiscal year ending in _t_ ; _NoDt_ , a dummy variable for firms that do not pay dividends in _t_ ; _Dt_ , total dividends paid during the fiscal year ending in _t_ ; _MCt_ , the log of market cap in June of _t_ ; _NegBt_ −1, a dummy variable for firms with negative book equity; _P/Bt_ −1, the ratio of market cap for December of _t_ − 1 to book equity for the fiscal yearend in _t_ − 1, for firms with positive book equity; and _LSt_ −1 _,_ the difference between leverage and target leverage for year _t_ − 1. Except for _MCt_ , _P/Bt_ −1, _LSt_ −1, and the two dummy variables, the dependent and explanatory variables are scaled by assets at the end of year _t_ . The table shows averages of the annual regression slopes (Coef) and the _t_ -statistics ( _t_ -stat) for the average slopes (the ratios of the average slopes to their time-series standard errors, estimated using the standard deviations of the annual slopes), and _R_<sup>2</sup> , the average value of the annual regression coefficient of determination. We show separate results for microcap firms (Micro, market cap in June of year _t_ below the 20th NYSE percentile), small firms (Small, between the 20th and 50th NYSE percentiles), and big firms (Big, above the 50th percentile), and for 1963–1982 and 1983–2009. To reduce the influence of outliers, the annual samples are trimmed, deleting 0.5% of the observations in the right tails of _PosYt_ , _Dt_ , _P/Bt_ −1, and _LSt_ −1, and 0.5% of the observations in the left tails of _dAt_ and _NegY t_ . On average, the regressions for 1963–1982 use 1242 microcaps, 442 small firms, and 581 big firms, and those for 1983–2009 use 2375 microcaps, 768 small firms, and 705 big firms. 

_Fama and French_ 

_76_ 

slopes for 1963–1982 and 1983–2009 are not reliably different. Appendix Table A2 suggests that the true slopes for microcaps differ from those for small or big firms, but the differences between the average slopes for small and big firms may be due to chance. The benefits of moving leverage toward its target are apparently larger for microcaps, especially during 1983–2009. 

The reversion of leverage to target is statistically reliable, but except for the microcaps of 1983–2009, it is economically weak. During 1963–1982 the cross-section standard deviation of the leverage surplus for microcaps, averaged across years, is 0.19 (Table 1). The average _LSt_ −1 slope for microcaps in the _dSt_ regression is 2.98 for this period so, roughly speaking, a leverage surplus one standard deviation above zero increases a microcap’s expected annual share issues by 0.57% _(_ 2 _._ 98 × 0 _._ 19 _)_ of assets (and reduces debt issues by the same amount) relative to a microcap with no leverage surplus. The comparable predicted increases in share issues for small and big firms during 1963–1982 and 1983–2009 are even smaller. Only the estimate for microcaps for 1983–2009 suggests that the leverage surplus has much effect on stock and debt issues; roughly speaking, a leverage surplus one standard deviation above zero on average increases annual share issues and reduces debt issues by 1.89% of assets. All this is in line with previous evidence that leverage reverts to its target but at the proverbial snail’s pace (for example, Fama and French, 2002; Flannery and Rangan, 2006; Kayhan and Titman, 2007; Huang and Ritter, 2009; Hovakimian and Li, 2011), and with the evidence that if there are leverage targets, they are rather soft (Graham and Harvey, 2001; Welch, 2004, DeAngelo and Roll, 2011). 

Leary and Roberts (2005) argue that adjustment costs can explain the slow reversion of leverage to its target. If adjustment costs are to explain our results, they must be lower for microcaps than for small or big firms, and they must be lower for microcaps (but not for small or big firms) later in our 1963–2009 sample period. We doubt that adjustment costs are the whole story. 

**The Market Conditions Model** — Inferences about the market conditions model center on the average slopes for the lagged price-to-book ratio, _P/Bt_ −1. The model says managers believe, rightly or wrongly, that higher _P/Bt_ −1 signals a lower cost of share issues relative to other forms 

_Capital Structure Choices_ 

_77_ 

of financing, so higher _P/Bt_ −1 firms allocate more outside financing to share issues. The positive average slopes for _P/Bt_ −1 in the Table 2 regressions to explain stock issues are in line with this prediction. The average slopes for 1963–1982 and 1983–2009 are all more than 4.1 standard errors from zero. The positive average slopes for _P/Bt_ −1 in the regressions for share issues are also consistent with the prediction of Myers and Majluf (1984) that the asymmetric information problems that drive pecking order financing are less severe for high _P/Bt_ −1 firms with clear growth opportunities. 

There is an interesting and novel size effect in the _P/Bt_ −1 slopes. The slopes for microcaps and small firms are further from zero than the slopes for big firms during both 1963–1982 and 1983–2009. For proponents of the market conditions model, this suggests that the belief that _P/Bt_ −1 is informative about the relative cost of share issues is more prevalent among managers of smaller firms. The inference for proponents of the Myers-Majluf version of the pecking order is that higher _P/Bt_ −1 is more informative about growth opportunities for smaller firms. 

The average slopes for _P/Bt_ −1 in the regressions to explain stock issues are statistically far from zero, but in economic terms the effects are large only for smaller firms and only during the 1983–2009 period of generally higher stock issue activity. Combining the average slopes for _P/Bt_ −1 in Table 2 with the average cross-section standard deviations in Table 1 says that during 1963–1982 a one standard deviation higher value of _P/Bt_ −1 is associated with increases in annual share issues (and reductions in debt issues) that average only about 0.47%, 0.85%, and 0.80% of assets for big, small, and microcap firms. The estimates for 1983–2009 — 0.95% for big firms, 2.19% for small firms, and 3.07% for microcaps — are more impressive, at least for microcaps and small firms. 

## **3 Short-Term versus Long-Term Debt** 

### **3.1 The Logic of the Regressions** 

The pecking order, market conditions, and tradeoff models also make predictions about debt financing. The pecking order model predicts that debt financing in response to cashflows is mostly short-term. In Myers and Majluf (1984), a preference for short-term versus long-term debt financing arises 

_Fama and French_ 

_78_ 

because the asymmetric information problems that drive pecking order financing are more severe for long-term debt. In a simpler pecking order model, the preference for short-term debt is just due to lower issuing costs. 

The logic of the market conditions model is that if managers perceive, rightly or wrongly, that high _P/Bt_ −1 growth stocks are overvalued, they are also likely to judge that the debt of growth firms is overvalued, with long-term debt more overvalued than short-term debt. The model thus predicts that higher _P/Bt_ −1 firms that issue debt prefer long-term debt. The pecking order model of Myers and Majluf (1984) suggests that asymmetric information problems are less severe for firms with clear growth opportunities, which also implies that controlling for cashflows, higher _P/Bt_ −1 firms that issue debt lean more toward long-term debt than lower _P/Bt_ −1 

The tradeoff model predicts that various forces, including the tax deductibility of interest and potential bankruptcy costs associated with debt, push firms toward an optimal mix of debt and equity. Tradeoff arguments also suggest predictions about the split of debt between short-term and long-term. For example, a company that shifts some of its debt from longterm to short-term increases the probability of bankruptcy and expected bankruptcy costs, but the incentives of its creditors to monitor and discipline management also increase (Diamond, 2004). Benmelech (2009) argues that the characteristics of a firm’s collateral can also affect its debt maturity. Assets that are more redeployable and more easily sold allow the firm to use longer term debt. In our suggested extension of the tradeoff model, these and other forces push firms toward an optimal mix of short-term and long-term debt; that is, a firm’s ratio of short-term debt to total liabilities tends to revert to a target. When it issues debt, a firm is more likely to issue long-term debt if its short-term ratio is above target and a firm below target is more likely to issue short-term debt. 

As with leverage, we use industry averages to measure target short-term debt ratios. We define a firm’s lagged short-term surplus, _STSt_ −1, as the difference between its short-term ratio for year _t_ − 1 and its target ratio for _t_ −1, where the short-term ratio is short-term debt divided by total liabilities for _t_ − 1 and the target short-term ratio is the _t_ − 1 average for the firm’s industry, with each firm in the industry weighted by its total liabilities (see Appendix for details). 

_Capital Structure Choices_ 

_79_ 

To test pecking order, market conditions, and tradeoff predictions about the split of debt financing between short-term and long-term, we lean on the cashflow constraint (2), which says that new financing from short-term and long-term debt must cover the demand for financing from investment and dividends less the supply of financing from earnings and share issues. Adding _dSt_ to the other cashflow variables, _dAt_ , _Dt_ , and _Yt_ , on the right side of the regressions controls for total required new debt (rather than total required outside financing) to isolate the choice between short-term and long-term debt, 







The change in short-term debt, _dSTDt_ , in (7) is the change in current liabilities during the fiscal year ending in calendar year _t_ ; _dLTDt_ in (8) is the change in long-term debt, including preferred stock. As the notation indicates, the constraints on the sums of the coefficients and residuals in (7) and (8) are the same as those in (4) and (5), with the additional constraints that the slopes for _dSt_ must sum to minus one and the slopes for _STSt_ −1 sum to zero. 

The slopes on the cashflow variables, _dAt_ , _Dt_ , _Yt_ , and _dSt_ , in (7) and (8) tell us how, on average, new debt splits between short-term and longterm in response to variation in investment, dividends, earnings, and share issues. The pecking order model predicts that debt financing in response to cashflows is mostly short-term. In other words, the slopes for _dAt_ , _Dt_ , _Yt_ , and _dSt_ should be further from zero for short-term debt than for long-term debt. The slopes on the lagged price-to-book ratio in (7) and (8) then tell us how _P/Bt_ −1 pushes the split of debt financing away from the averages. The market conditions model and the Myers-Majluf version of the pecking order model predict that higher _P/Bt_ −1 firms substitute away from shortterm debt toward long-term debt, so the slope on _P/Bt_ −1should be positive in the regression to explain _dLTDt_ , with an exactly offsetting negative slope in the _dSTDt_ regression. Finally, the tradeoff model predicts that firms tend to revert to their target short-term ratio, so the slope on _STSt_ −1 should be negative in the _dSTDt_ regression and positive in the _dLTDt_ regression. 

_Fama and French_ 

_80_ 

### **3.2 Regression Results** 

The explanatory variables in the actual cross-section regressions to test predictions about debt financing match those in (6) except we add share issues, _dSt_ , and replace the lagged leverage surplus with the lagged shortterm surplus, _STSt_ −1. The dependent variables, _dFt_ , in the paired regressions are _dSTDt_ and _dLTDt_ , short-term and long-term debt issued in fiscal year _t_ , 



The prediction of the market conditions model and the pecking order of Myers and Majluf (1984) that the new debt of high _P/Bt_ −1 firms tends to be long-term gets at best weak support in the _dSTDt_ −1 and _dLTDt_ −1 regressions for 1963–1982 and no support in results for 1983–2009 (Table 3). The average slopes for _P/Bt_ −1 in the _dLTDt_ regressions for 1963–1982 are positive for all three size groups but only the average slope for microcaps is more than 2.0 standard errors from zero. In the regressions for 1983–2009, the average slope for microcaps is quite close to zero, and the average slopes for small and big firms have the wrong sign (negative). 

Pecking order predictions about the response of short-term and longterm debt financing to cashflow variables also fare poorly in Table 3. The regressions say that given total new debt, with few exceptions long-term debt absorbs more of the variation in investment, earnings, dividends, and share issues than short-term debt. Thus, asymmetric information problems, issuing costs, and any other pecking order forces that predict a preference for short-term debt apparently do not play an important role in debt financing. 

The tradeoff model’s prediction that firms have targets for the short-term debt ratio is more successful, at least among smaller firms. The _STSt_ −1 slopes for microcaps and small stocks are positive and more than 3.5 standard errors from zero in the long-term debt regressions for 1963–1982 and 1983–2009. Thus, controlling for total new debt, microcaps and small stocks with a higher short-term surplus tend to issue more long-term debt and less short-term debt. For big stocks, however, the average slope for _STSt_ −1 in the _dLTDt_ regression is negative (the wrong sign) but indistinguishable from zero for 1963–1983, and the positive average slope for 1983–2009 is just 1.74 standard errors from zero. 

_Capital Structure Choices_ 

_81_ 



|_R_2|0.58|0.45||0.42||0.45|0.34|0.38|_tinued_)|
|---|---|---|---|---|---|---|---|---|---|
|_STSt_−1|−5_._63<br>−10_._92|−1_._94|−3_._60|0_._28|0_._65|−10_._62<br>−14_._44|−2_._24<br>−4_._47|−0_._96<br>−1_._74|(_Con_|
|_P/Bt_−1|−0_._28<br>−2_._88|−0_._08|−1_._13|−0_._12|−1_._97|−0_._01<br>−0_._60|0_._03<br>0_._99|0_._09<br>3_._15||
|_NegBt_−1|−1_._67<br>−0_._88|−4_._36|−1_._31|−0_._81|−0_._98|−1_._94<br>−2_._29|0_._52<br>0_._84|1_._32<br>1_._24||
|_MCt_|−0_._52<br>−7_._68|−0_._43|−1_._68|0_._10|3_._02|−0_._43<br>−5_._96|−0_._07<br>−0_._46|0_._09<br>2_._54||
|_Dt_|0_._74<br>11_._65|0_._21|3_._87|0_._14|3_._95|0_._73<br>12_._12|0_._18<br>3_._20|0_._12<br>4_._03||
|_NoDt_|1963–1982<br>0_._31<br>1_._53|−0_._37|−1_._55|−0_._23|−0_._83|1983–2009<br>0_._97<br>4_._92|0_._21<br>1_._43|0_._30<br>1_._92||
|_dSt_|−0_._53<br>−12_._26|−0_._34|−18_._47|−0_._32|−13_._69|−0_._49<br>−31_._92|−0_._28<br>−15_._26|−0_._24<br>−20_._10||
|_PosYt_|−0_._36<br>−14_._06|−0_._13|−3_._86|−0_._12|−3_._99|−0_._39<br>−20_._06|−0_._15<br>−8_._11|−0_._15<br>−9_._48||
|_NegYt_|−0_._71<br>−25_._36|−0_._44|−2_._53|−0_._64|−5_._02|−0_._55<br>−33_._33|−0_._38<br>−10_._85|−0_._29<br>−13_._07||
|_dAt_|0_._58<br>47_._52|0_._41|31_._47|0_._38|25_._49|0_._52<br>41_._98|0_._32<br>23_._90|0_._30<br>44_._47||
|_at_|0_._42<br>1_._37|0_._79|0_._74|−1_._32|−5_._64|1_._91<br>5_._20|0_._10<br>0_._12|−1_._01<br>−3_._01||
||Micro<br>Coef<br>_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef|_t_-stat|Micro<br>Coef<br>_t_-stat|Small<br>Coef<br>_t_-stat|Big<br>Coef<br>_t_-stat||







_Fama and French_ 

_82_ 







||44||61||65||44||69||74||en||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_R_2|0.||0.||0.||0.||0.||0.||we||
|_STSt_−1|5_._63|10_._92|1_._94|3_._60|−0_._28|−0_._65|10_._62|14_._44|2_._24|4_._47|0_._96|1_._74|bilities bet||
|_P/Bt_−1|0_._28|2_._88|0_._08|1_._13|0_._12|1_._97|0_._01|0_._60|−0_._03|−0_._99|−0_._09|−3_._15|new lia||
|_NegBt_−1|1_._67|0_._88|4_._36|1_._31|0_._81|0_._98|1_._94|2_._29|−0_._52|−0_._84|−1_._32|−1_._24|ocation of|.)|
|_MCt_|0_._52|7_._68|0_._43|1_._68|−0_._10|−3_._02|0_._43|5_._96|0_._07|0_._46|−0_._09|−2_._54|in the all|scription|
|_Dt_|82<br>0_._26|4_._01|0_._79|14_._15|0_._86|24_._30|09<br>0_._27|4_._49|0_._82|14_._37|0_._88|29_._30|to expla|table de|
|_NoDt_|1963–19<br>−0_._31|−1_._53|0_._37|1_._55|0_._23|0_._83|1983–20<br>−0_._97|−4_._92|−0_._21|−1_._43|−0_._30|−1_._92|sion (9)|age for|
|_dSt_|−0_._47|−10_._96|−0_._66|−36_._11|−0_._68|−28_._79|−0_._51|−32_._61|−0_._72|−38_._57|−0_._76|−64_._00|of regres|ee next p|
|_PosYt_|−0_._64|−25_._44|−0_._87|−26_._51|−0_._88|−29_._94|−0_._61|−31_._64|−0_._85|−46_._48|−0_._85|−54_._35|imates|debt. (S|
|_NegYt_|−0_._29|−10_._27|−0_._56|−3_._19|−0_._36|−2_._82|−0_._45|−27_._82|−0_._62|−17_._91|−0_._71|−31_._87|s from est|ong-term|
|_dAt_|0_._42|34_._46|0_._59|44_._69|0_._62|42_._48|0_._48|38_._87|0_._68|50_._29|0_._70|103_._90|ge slope|ies and l|
|_at_|−0_._42|−1_._37|−0_._79|−0_._74|1_._32|5_._64|−1_._91|−5_._20|−0_._10|−0_._12|1_._01|3_._01|**3**. Avera|t liabilit|
||Micro<br>Coef|_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef|_t_-stat|Micro<br>Coef|_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef|_t_-stat|**Table**|curren|



_Capital Structure Choices_ 

_83_ 

**Table 3 Description:** The regressions are estimated each year _t_ during 1963–2009 using CRSP and Compustat data for non-financial NYSE, Amex, and (after 1972) Nasdaq firms with fiscal yearends in calendar year _t_ . The dependent variable is either _dSTDt_ (change in shortterm debt, which is current liabilities, during the fiscal year ending in calendar year _t)_ or _dLTDt_ (change in long-term debt). In addition to the regression intercept _(at )_ the explanatory variables are: _dAt_ , the change in total assets from _t_ − 1 to _t_ ; _NegYt_ and _PosYt_ , earnings for firms with negative and positive earnings for the fiscal year ending in _t_ ; _dSt_ , the book value of common shares issued from the fiscal yearend in calendar year _t_ − 1 to the fiscal yearend in _t_ ; _NoDt_ , a dummy variable for firms that do not pay dividends in _t_ ; _Dt_ , total dividends paid during the fiscal year ending in _t_ ; _MCt_ , the log of market cap in June of _t_ ; _NegBt_ −1, a dummy variable for firms with negative book equity; _P/Bt_ −1, the ratio of market cap for December of _t_ − 1 to book equity for the fiscal yearend in _t_ − 1, for firms with positive book equity; and _STSt_ −1, the difference between the short-term debt ratio and the target ratio for year _t_ − 1. Except for _MCt_ , _P/Bt_ −1, _STSt_ −1, and the two dummy variables, the dependent and explanatory variables are scaled by assets at the end of year _t_ . The table shows averages of the annual regression slopes (Coef) and the _t_ -statistics ( _t_ -stat) for the average slopes (the ratios of the average slopes to their time-series standard errors, estimated using the standard deviations of the annual slopes), and _R_<sup>2</sup> , the average value of the annual regression coefficient of determination. We show separate results for microcap firms (Micro, market cap in June of year _t_ below the 20th NYSE percentile), small firms (Small, between the 20th and 50th NYSE percentiles), and big firms (Big, above the 50th percentile), and for 1963– 1982 and 1983–2009. To reduce the influence of outliers, the annual samples are trimmed, deleting 0.5% of the observations in the right tails of _PosYt_ , _Dt_ , and _P/Bt_ −1 _,_ and 0.5% of the observations in the left tails of _dAt_ , _NegYt_ , and _dSt_ . On average, the regressions for 1963– 1982 use 1244 microcaps, 441 small firms, and 580 big firms, and those for 1983–2009 use 2380 microcaps, 767 small firms, and 702 big firms. 

The magnitude of the tradeoff effect for microcaps is substantial. The average _STSt_ −1 slopes are 5.63 for 1963–1982 and 10.62 for 1983–2009, and the average standard deviations of _STS_ are 0.24 and 0.27 (Table 1), so roughly speaking, a short-term surplus one standard deviation above the mean increases a microcap firm’s expected allocation to long-term debt by 1.35% _(_ 5 _._ 63 × 0 _._ 25 _)_ of assets in the first period and 2.87% of assets in the second. The effect of the short-term surplus is weaker, however, among small stocks and apparently non-existent for big stocks, especially during the early years of our sample period. 

In sum, the estimates of regression (9) provide hints of the relevance of tradeoff, pecking order, and market conditions predictions in debt maturity decisions, but evidence that is consistent across size groups and time periods is lacking. Given that the evidence is so mixed, it seems safe to conclude that the forces we consider do not play a dominant role in long-term versus short-term debt choices. 

_Fama and French_ 

_84_ 

## **4 Dividends and Share Issues** 

### **4.1 The Logic of the Regressions** 

Our final task is to test the predictions of the pecking order and market conditions models about the split of equity financing between share issues and retained earnings. Earnings are not a choice variable; to control retained earnings firms must vary dividends. To focus on the choice between share issues and dividends, we use the cashflow constraint in (3), which we repeat here, 



Equation (3) says investment not financed by earnings and new debt must be financed by net share issuance, that is, by share issues minus dividends. Equivalently, (3) implies that holding investment, earnings, and new debt fixed, every additional dollar of new shares must be consumed by an additional dollar of dividends. This version of the cashflow constraint suggests the paired regressions, 





The notation captures the constraints on the regression coefficients and residuals implied by equation (3). If we subtract the dividend regression (11) from the share issues regression (10), we get (3), so the difference between the slopes for _dAt_ in the _dSt_ and _Dt_ regressions is one, the difference between the slopes for _Yt_ in the _dSt_ and _Dt_ regressions is minus one, and the same is true for the _dL t_ slopes. Equation (3) also implies that (10) and (11) have the same intercepts and residuals. Finally, the slopes for _P/Bt_ −1 and any other variables not in the cashflow constraint (3) must also be identical in the two regressions. In words, because the cashflow variables in (10) and (11) control for variation in _dSt_ − _Dt_ , variation in share issues linked to other explanatory variables must be matched by variation in dividends in the same direction. 

If managers interpret the price-to-book ratio as information about the relative cost of new share financing, higher _P/Bt_ −1 should lead firms to issue shares. The proceeds from share issues can be put into investment (including cash), in which case they show up in _dAt_ , or they can be paid out as 

_Capital Structure Choices_ 

_85_ 

dividends. We then interpret the market conditions model as predicting that controlling for investment, higher _P/Bt_ −1 leads some firms to increase dividends to make larger issues of shares. In the pecking order model, share issues are, for one reason or another, the most expensive form of financing, which in itself should lead firms to lower dividends to fund investment outlays not covered by earnings and new debt. 

### **4.2 Regression Results** 

As usual, we estimate enhanced versions of (10) and (11), 



The dependent variable, _dFt_ , is either share issues, _dSt_ , or dividends, _Dt_ , for the fiscal year ending in calendar year _t_ . The new explanatory variable is lagged dividends, _Dt_ −1, dividends for fiscal year _t_ −1. There is no consensus about why firms pay dividends, but there is strong evidence, from Fama and Babiak (1968) to Skinner (2008), that dividends are sticky. We include _Dt_ −1 in regression (12) to allow for management’s reluctance to change dividends. (More precisely, _Dt_ −1 is an estimate of the total dividends that would be paid in fiscal year _t_ if split-adjusted dividends per share did not change from _t_ − 1 to _t_ . See the Appendix for details.) 

The persistence of dividends is clear in Table 4. The average slopes for _Dt_ −1 are 0.88 or higher in the dividend regressions. Dividend persistence is strongest for big stocks. The average _Dt_ −1 slope for big stocks is 0.98 for 1963–1982 and 0.93 for 1983–2009. Since the dividend regressions include earnings as an explanatory variable, the deviation of a _Dt_ −1 slope from 1.0 is an estimate of the annual speed-of-adjustment of dividends to target dividends (a fixed proportion of earnings) in Lintner’s (1956) partial adjustment model. Adjustment is slow for microcaps (12% per year for 1963–1982 and 10% for 1983–2009), and it is slower for small stocks (7% and 8% per year) and big stocks (2% and 7%). 

The stickiness of dividends is also apparent in the earnings slopes in the dividend regressions of Table 4. The average slopes for _PosY t_ are at least 2.8 standard errors from zero, but the response of dividends to earnings is nevertheless feeble. On average, between four and nine cents of an additional 

_Fama and French_ 

_86_ 



|_R_2|0.82||0.85||0.92||0.27||0.61||0.66|_ntinued_)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_Dt_−1|0_._88|57_._83|0_._93|47_._93|0_._98|43_._93|0_._90|20_._38|0_._92|32_._94|0_._93<br>37_._35|(_Co_|
|_P/Bt_−1|−0_._02|−3_._21|0_._01|0_._65|0_._01|2_._57|0_._02|3_._68|0_._05|2_._24|0_._02<br>1_._48||
|_NegBt_−1|0_._01|0_._19|0_._01|0_._11|−0_._07|−1_._31|0_._25|3_._20|0_._76|2_._25|0_._86<br>2_._02||
|_MCt_|0_._06|6_._22|0_._12|1_._68|0_._01|0_._93|0_._03|1_._76|−0_._09|−2_._41|0_._00<br>−0_._06||
|_dLt_|63–1982<br>0_._02|6_._02|0_._03|2_._74|−0_._01|−0_._27|83–2009<br>0_._02|4_._25|0_._07|2_._74|0_._08<br>2_._25||
|_PosYt_|19<br>0_._07|10_._65|0_._09|6_._88|0_._06|2_._80|19<br>0_._04|5_._21|0_._07|3_._94|0_._07<br>3_._70||
|_NegYt_|0.01|3.95|0.02|1.53|0.04|1.00|0.01|4.03|0.04|2.68|0.07<br>1.72||
|_dAt_|−0_._02|−5_._56|−0_._03|−2_._85|0_._00|0_._09|−0_._02|−4_._49|−0_._06|−2_._88|−0_._06<br>−2_._24||
|_at_|−0_._22|−8_._18|−0_._61|−2_._26|−0_._14|−1_._68|−0_._03|−0_._64|0_._59|2_._21|−0_._03<br>−0_._16||
||Micro<br>Coef|_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef|_t_-stat|Micro<br>Coef|_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef<br>_t_-stat||







_Capital Structure Choices_ 

_87_ 



|98|95|97||97||95||93|ity||
|---|---|---|---|---|---|---|---|---|---|---|
|_R_2<br>0.|0.|0.||0.||0.||0.|equ||
|_Dt_−1<br>0_._88|57_._83<br>0_._93|47_._93<br>0_._98|43_._93|0_._90|20_._38|0_._92|32_._94|0_._93<br>37_._35|net new|ription.)|
|_P/Bt_−1<br>−0_._02|−3_._21<br>0_._01|0_._65<br>0_._01|2_._57|0_._02|3_._68|0_._05|2_._24|0_._02<br>1_._48|ocation of|table desc|
|_NegBt_−1<br>0_._01|0_._19<br>0_._01|0_._11<br>−0_._07|−1_._31|0_._25|3_._20|0_._76|2_._25|0_._86<br>2_._02|ain the all|page for|
|_MCt_<br>0_._06|6_._22<br>0_._12|1_._68<br>0_._01|0_._93|0_._03|1_._76|−0_._09|−2_._41|0_._00<br>−0_._06|2) to expl|(See next|
|_dLt_<br>–1982<br>−0_._98|−333_._04<br>−0_._97|−97_._35<br>−1_._01|−43_._69|–2009<br>−0_._98|−252_._58|−0_._93|−36_._71|−0_._92<br>−27_._68|ession (1|e issues.|
|_PosYt_<br>1963<br>−0_._93|−132_._76<br>−0_._91|−69_._75<br>−0_._94|−47_._81|1983<br>−0_._96|−117_._75|−0_._93|−49_._11|−0_._93<br>−52_._46|ates of regr|gs and shar|
|_NegYt_<br>−0_._99|−271_._33<br>−0_._98|−73_._30<br>−0_._96|−23_._93|−0_._99|−383_._64|−0_._96|−62_._41|−0_._93<br>−21_._94|from estim|ned earnin|
|_dAt_<br>0_._98|330_._51<br>0_._97|95_._27<br>1_._00|53_._55|0_._98|284_._08|0_._94|48_._43|0_._94<br>38_._56|ge slopes|een retai|
|_at_<br>−0_._22|−8_._18<br>−0_._61|−2_._26<br>−0_._14|−1_._68|−0_._03|−0_._64|0_._59|2_._21|−0_._03<br>−0_._16|**4**. Avera|ing betw|
|Micro<br>Coef|_t_-stat<br>Small<br>Coef|_t_-stat<br>Big<br>Coef|_t_-stat|Micro<br>Coef|_t_-stat|Small<br>Coef|_t_-stat|Big<br>Coef<br>t-stat|**Table**|fnanc|







_Fama and French_ 

_88_ 

**Table 4 Description:** The regressions are estimated each year _t_ during 1963–2009 using CRSP and Compustat data for non-financial NYSE, Amex, and (after 1972) Nasdaq firms with fiscal yearends in calendar year _t_ . The dependent variable is either _Dt_ (total dividends paid during the fiscal year ending in _t)_ or _dSt_ (book value of common shares issued during the fiscal year ending in calendar year _t)_ . In addition to the regression intercept ( _at )_ the explanatory variables are: _dAt_ , the change in total assets from _t_ − 1 to _t_ ; _NegYt_ and _PosYt_ , earnings for firms with negative and positive earnings for the fiscal year ending in _t_ ; _dL t_ , the change in liabilities, including preferred stock, during the fiscal year ending in _t_ ; _MCt_ , the log of market cap in June of _t_ ; _NegBt_ −1, a dummy variable for firms with negative book equity; _P/Bt_ −1, the ratio of market cap for December of _t_ − 1 to book equity for the fiscal yearend in _t_ − 1, for firms with positive book equity; and _Dt_ −1, split-adjusted dividends paid during the fiscal year ending in _t_ − 1. Except for _MCt_ , _P/Bt_ −1, and the two dummy variables, the dependent and explanatory variables are scaled by assets at the end of year _t_ . The table shows averages of the annual regression slopes (Coef) and the _t_ -statistics ( _t_ -stat) for the average slopes (the ratios of the average slopes to their time-series standard errors, estimated using the standard deviations of the annual slopes), and _R_<sup>2</sup> , the average value of the annual regression coefficient of determination. We show separate results for microcap firms (Micro, market cap in June of year _t_ below the 20th NYSE percentile), small firms (Small, between the 20th and 50th NYSE percentiles), and big firms (Big, above the 50th percentile), and for 1963–1982 and 1983–2009. To reduce the influence of outliers, the annual samples are trimmed, deleting 0.5% of the observations in the right tails of _PosYt_ , _Dt_ −1, and _P/Bt_ −1, and 0.5% of the observations in the left tails of _dAt_ , _NegYt_ , and _dLt_ . On average, the regressions for 1963–1982 use 1245 microcaps, 442 small firms, and 581 big firms, and those for 1983–2009 use 2380 microcaps, 769 small firms, and 705 big firms. 

dollar of positive earnings goes to dividends, with the remainder used to reduce share issues. Dividends almost always respond less to negative earnings than to positive earnings. This is in line with Lintner’s (1956) claim that managers are reluctant to cut dividends when faced with negative earnings. But it may also mean that many firms with negative earnings pay no dividends. In any case, the estimates of regression (12) for share issues and dividends say that, given investment and new debt, higher positive earnings show up almost entirely as lower share issues rather than higher dividends, and bigger losses are covered almost entirely by share issues rather than lower dividends. 

The remaining cashflow controls in (12) are investment, _dAt_ , and debt issues, _dL t_ . The slopes for _dAt_ in the _dSt_ and _Dt_ regressions again say that holding earnings and new debt fixed, higher investment is financed almost entirely by share issues, not by a reduction in dividends. Similarly, holding investment and earnings fixed, firms that issue less new debt make up 

_89_ 

_Capital Structure Choices_ 

almost all the shortfall with share issues, not smaller dividend payments. All these results confirm that dividends are sticky: they move hardly at all with variation in investment, earnings, and debt issues. 

The average adjusted _R_<sup>2</sup> in the dividend regressions for 1963–1982 are 0.82 or higher. Most of the explanatory power comes from lagged dividends. The _t_ -statistics for the average _Dt_ −1 slopes for 1963–1982 exceed 43.0. There is less explanatory power in the dividend regressions for 1983– 2009. The drop in the average adjusted _R_<sup>2</sup> for microcaps, from 0.82 in the first period to 0.27 in the second, is the most extreme, but the declines for small firms (from 0.85 to 0.61) and big firms (0.92 to 0.66) are also substantial. At least part of the reduction in explanatory power is due to an increase in the fraction of firms that do not pay dividends (Fama and French, 2001). The average fraction of big firms that do not pay dividends grows from 6% in 1963–1982 to 30% in 1983–2009 (Table 1). The shift away from dividends is even more dramatic for smaller firms. On average, 57% of small firms and 84% of microcaps do not pay dividends during 1983–2009, versus 18% and 48% for 1963–1982. 

The estimates of regression (12) say that almost all variation in investment, earnings, and new debt in the cashflow constraint (3) is absorbed by share issues. As a result, the explanatory power of the _dSt_ version of (12) is high, with average adjusted _R_<sup>2</sup> at least 0.95 in the first period and 0.93 in the second, and average slopes for the cashflow variables that are all more than 21 standard errors from zero. 

Table 4 provides some support for the prediction of the market conditions model that, controlling for other cashflow variables, high _P/Bt_ −1 growth firms increase dividends to issue shares and low _P/Bt_ −1 value firms repurchase shares rather than pay dividends. Five of the six dividend regressions produce the positive average _P/Bt_ −1 slope predicted by the model and three are more than two standard errors above zero. The slopes, however, are tiny. Only one average _P/Bt_ −1 slope, 0.05 _(t_ = 2 _._ 67 _)_ for small firms during 1983– 2009, is bigger than 0.02. For perspective, the average _P/Bt_ −1 slopes in the _dSt_ −1 version of regression (6) in Table 2 are all positive and at least ten times the matching average _P/Bt_ −1 slopes in Table 4. Thus, the tradeoff of new equity for new debt in response to variation in _P/Bt_ −1 (regression (6)) is at least ten times stronger than the tradeoff of share issues for retained earnings (regression (12)). In short, the costs and benefits that produce sticky dividends apparently overwhelm any effects of market conditions. 

_Fama and French_ 

_90_ 

As noted above, a strong version of the pecking order model predicts that the high cost of share issues (due to asymmetric information problems, transaction costs, or other factors) leads firms to reduce dividends to fund investment outlays not covered by earnings and new debt. The extreme stickiness of dividends in response to variation in investment, earnings, and debt issues might thus be taken as a blow to this version of the pecking order model. Myers (1984) recognizes this problem and stipulates that dividends are outside the purview of the pecking order, in effect conceding that whatever costs and benefits produce sticky dividends apparently outweigh pecking order forces that would produce more variation in dividends. 

## **5 Conclusions and Caveats** 

We test the tradeoff, pecking order, and market conditions models with three pairs of cross-section regressions. Each pair focuses on predictions about different kinds of financing. The first pair of regressions explains the split of new outside financing between share issues and debt. The second examines the choice between short-term and long-term debt. The third pair focuses on the split of equity financing between share issues and retained earnings. Table 5 summarizes the models’ predictions and the regression results. 

**Tradeoff Model** — Our evidence on the tradeoff model’s prediction that leverage reverts to its target comes from the paired regressions that split total new outside financing between shares and debt. There is reliable evidence that leverage moves toward its target, but like others (e.g., Fama and French, 2002), we find that reversion is quite slow. This raises questions about relevance (Shyam-Sunder and Myers, 1999; Hovakimian and Li, 2011), especially given other evidence that leverage targets are not a first-order consideration in financing decisions (Graham and Harvey, 2001; Welch, 2004; DeAngelo and Roll, 2011). 

The regressions that split total new debt between short-term and longterm test an extension of the tradeoff model. If tradeoff forces push firms toward an optimal mix of short-term and long-term debt, then controlling for total debt issues, firms below their target allocation will issue more short-term debt and those above will issue less. Our results on this 

_Capital Structure Choices_ 

_91_ 







|Market Conditions|Firms with higher _P/Bt_−1<br>allocate more outside<br>fnancing to share issues,<br>more debt fnancing to<br>long-term debt, and more<br>equity fnancing to new<br>shares.<br>Controlling for total outside<br>fnancing, new share issues<br>are positively related to<br>_P/Bt_−1, but the effect is<br>economically large only for<br>smaller frms in 1983–2009.<br>There is only weak evidence<br>that high _P/Bt_−1 frms favor<br>long-term debt in<br>1963–1982 and there is no<br>evidence in 1983–2009.<br>There is reliable evidence<br>that high _P/Bt_−1 frms<br>increase dividends to issue<br>shares, but the effect is<br>economically tiny.<br>s.|
|---|---|
|Pecking Order|Firms favor debt over new<br>share issues, short-term debt<br>over long-term debt, and<br>retained earnings over new<br>share issues.<br>New debt absorbs most of the<br>variation in_dAt_,_Yt_, and _Dt_ in<br>1963-1982, but share issues<br>are about as important as new<br>debt in 1983–2009.<br>Long-term debt absorbs more<br>variation in investment,<br>earnings, dividends, and<br>share issues than short-term<br>debt.<br>Controlling for total equity<br>fnancing, share issues absorb<br>almost all variation in<br>investment, earnings, and<br>debt issues.<br>edictions and Empirical Result|
|Tradeoff|Firms have targets for<br>leverage and for short-term<br>relative to long-term debt,<br>and adjust their new<br>fnancing to move back<br>toward their targets.<br>Reversion of leverage to<br>target is statistically reliable<br>but, except for microcaps in<br>1983–2009, it is economically<br>weak.<br>Controlling for total new<br>debt, smaller frms with a<br>higher short-term surplus<br>tend to issue more long-term<br>debt.<br>**Table 5**. Summary of Pr|
||Predictions<br>Share Issues vs New<br>Debt (Controlling for<br>total outside<br>fnancing)<br>Short-term vs<br>Long-term Debt<br>(Controlling for total<br>new debt)<br>Share Issues vs<br>Retained Earnings<br>(Controlling for total<br>equity fnancing)|



_Fama and French_ 

_92_ 

prediction are mixed, ranging from strong support among microcap stocks, modest support among small stocks, and no support among big stocks. 

**Market Conditions Model** — The regressions that split total outside financing between share issues and debt support the prediction of the market conditions model that higher price-to-book firms allocate more outside financing to share issues and less to debt. The average _P/Bt_ −1 slopes in regressions to explain _dSt_ are reliably positive for microcap, small, and big firms during 1963–1982 and 1983–2009. In economic terms, however, substitution of share issues for debt in response to _P/Bt_ −1 is modest except for microcaps and small firms, and then only during 1983–2009. 

Support for other predictions of the market conditions model is at best mixed. The prediction that higher _P/Bt_ −1 is associated with more long-term than short-term new debt (second set of regressions) gets some support during 1963–1982, but not during 1983–2009. There is also evidence (from the third set of regressions) that higher _P/Bt_ −1 leads firms to pay dividends in order to issue shares, but the magnitude of the effect is tiny. 

**Pecking Order** — Our evidence that firms prefer debt to new shares for outside financing during 1963–1982, but not during 1983–2009, confirms earlier results on this prediction of the pecking order model (Fama and French, 2002; Frank and Goyal, 2003). The regressions that split new debt issues between short-term and long-term are novel, and they do not support the pecking order prediction that issuing costs (asymmetric information problems or simple transaction costs) that are higher for long-term debt lead firms to prefer short-term debt. This prediction fails in the tests for 1963–1982 as well as in the tests for 1983–2009. Not surprisingly in light of previous evidence on the stickiness of dividends, our regressions to explain share issues and dividends do not support the prediction of a strong version of the pecking order model that firms vary dividends to avoid the high costs of issuing shares. 

Finally, stock issues and repurchases are more common later in the 1963– 2009 period, particularly among smaller firms, and this change permeates our results. The pecking order prediction that most of the variation in investment, dividends, and earnings is absorbed by debt rather than by share issues does well during 1963–1982, but the prediction fails during 1983– 2009 when share issues become more common. In contrast, the reversion 

_Capital Structure Choices_ 

_93_ 

of leverage to target predicted by the tradeoff model and the variation in the split between debt and equity financing in response to _P/Bt_ −1 predicted by the market conditions model hinge on share issues and repurchases. Thus, the mispricing model’s prediction that higher _P/Bt_ −1 pushes outside financing toward share issues does better for microcaps and small firms during 1983–2009, when the share issues and repurchases that are the bane of the pecking order become common. The reversion of leverage to target is also stronger for microcaps during 1983–2009. 

## **A Appendix** 

### **A.1 Variable** 

The data are from the Center for Research in Security Prices (CRSP) and Compustat, supplemented by book equity data for NYSE stocks collected from Moody’s manuals, as in Davis _et al._ (2000). The variables we use in the regressions for year _t_ (traditional Compustat item numbers in parentheses) are: 

- _dAt_ Investment: Change in assets (6) during fiscal year _t_ . 

- _Yt_ Earnings: Income before extraordinary items available for common (237) plus extraordinary income (48) during fiscal year _t_ . 

- _PosY t_ Positive earnings: Earnings if _Yt_ is positive, 0 if _Yt_ is negative. 

- _NegYt_ Negative earnings: Earnings if _Yt_ is negative, 0 if _Yt_ is positive. _MCt_ Market cap: The log of the price times shares outstanding at the end of June of calendar year _t_ , from CRSP. 

- _Dt_ Dividends: Dividends per share by ex-date (26) at the end of fiscal year _t_ times shares outstanding (25) at the end of _t_ . 

- _NoDt_ No dividends: A dummy variable that is 1 if the firm does not pay dividends in fiscal year _t_ and 0 otherwise. 

- _Dt_ −1 Lagged dividends: Split-adjusted dividends per share by ex-date (26) at the end of fiscal year _t_ − 1 times shares outstanding (25) at the end of _t_ . We use the Compustat adjustment factor (27) to adjust for splits and stock dividends during fiscal year _t_ . For example, if there is a three-for-one split during year _t_ , we divide dividends per share for fiscal year _t_ − 1 by three. 

_Fama and French_ 

_94_ 

- _P/Bt_ −1 Lagged price-to-book ratio: Market equity (CRSP price times shares outstanding) in December of year _t_ − 1 divided by aggregate book equity for the fiscal year ending in calendar year _t_ − 1. Book equity is stockholders equity (216) (or common equity, 60, plus carrying value of preferred stock, 130, or assets, 6, minus reported liabilities, 181) plus balance sheet deferred taxes and investment tax credit (35) if available, minus postretirement benefits (330) if available, minus preferred stock liquidating value (10) if available, or redemption value (56) if available, or carrying value (130). 

- _NegBt_ −1 Negative book equity: A dummy variable that is 1 if the firm’s book equity at the end of fiscal year _t_ − 1 is negative and 0 otherwise. 

- _LSt_ −1 Lagged leverage surplus: The difference between the firm’s leverage ratio and its target leverage ratio. The leverage ratio is assets (6) minus common equity (60) at the end of fiscal year _t_ − 1 divided by assets at the end of _t_ − 1. The target leverage ratio is the average leverage ratio at the end of _t_ − 1 for the firms in the same industry, with each firm weighted by its assets (6) at the end of _t_ − 1. Firms are assigned to one of ten industries each year using the industry definitions at: http://mba.tuck.dartmouth.edu/pages/faculty/ ken.french/Data Library/det 10 ind port.html. 

   - _dSt_ Book value of shares issued: Change in common equity (Compustat data item 60) plus dividends, _Dt_ , minus earnings, _Yt_ , during fiscal year _t_ . 

   - _dL t_ Change in total liabilities, including preferred: Change in assets (6) minus change in common equity (60) during fiscal year _t_ . 

- _dSTDt_ Change in short-term debt: Change in current liabilities (5) during fiscal year _t_ . 

- _dLTDt_ Change in long-term debt: Change in total liabilities, _dL t_ , minus change in current liabilities, _dSTDt_ . 

_95_ 

_Capital Structure Choices_ 

- _STSt_ −1 Lagged short-term surplus: The difference between the firm’s short-term debt ratio and its target ratio. The short-term debt ratio is current liabilities (5) at the end of fiscal year _t_ − 1, divided by total liabilities (assets 6 minus common equity 60) at the end of _t_ − 1. The target ratio is the average short-term ratio at the end of _t_ − 1 for the firms in the same industry, with each firm weighted by its total liabilities at the end of _t_ − 1. Firms are assigned to one of ten industries each year using the industry definitions at: http://mba.tuck. dartmouth.edu/pages/faculty/ken.french/Data Library/ det 10 ind port.html. 

All variables except _MCt_ , _P/Bt_ −1, _LSt_ −1, _STSt_ −1, _NegBt_ −1, and _NoDt_ are divided by assets at the end of fiscal year _t_ . The flow variables, _dAt_ , _Yt_ , _PosY t_ , _NegYt_ , _dSt_ , _dL t_ , _dSTDt_ , _dLTDt_ , _Dt_ , and _Dt_ −1, are then multiplied by 100. We exclude financial firms (Standard Industrial Classification codes between 6000 and 6999). We also exclude firms from the regressions for year _t_ if we are missing: market cap (from CRSP) for December of _t_ − 1, June of _t_ , and the fiscal yearend in _t_ − 1; dividends per share by ex date, Compustat shares outstanding, income before extraordinary items available for common, and extraordinary income for the fiscal year ending in _t_ ; assets, common equity, and current liabilities for the fiscal yearends in calendar years _t_ − 1 and _t_ ; and book equity for the fiscal year ending in calendar year _t_ − 1. Finally, we exclude firms whose common equity at the end of year _t_ − 1 exceeds their assets at the end of _t_ − 1. Firms must also have dividends per share by ex date for fiscal year _t_ − 1 to be included in the year _t_ regressions in Table 4. 

### **A.2 Comparisons of Slopes across Size Groups and Periods** 

Table A1 reports tests of whether the average regression slopes in Table 2 are different for 1983–2009 versus 1963–1982. Table A2 reports tests of whether the average regression slopes differ across the microcap, small, and big size groups. 

_Fama and French_ 

_96_ 



|_P/Bt_−1<br>_LSt_−1<br>0_._31<br>4_._31<br>4_._65<br>5_._31<br>0_._10<br>−0_._34<br>0_._78<br>−0_._40<br>−0_._01<br>0_._26<br>−0_._11<br>0_._32<br>982 and 1983–2009.<br>nancial NYSE, Amex, and<br>k value of common shares<br>iables are:_dAt_, the change<br>or the fscal year ending in<br>scal year ending in_t_;_MCt_,<br>−1, the ratio of market cap<br>and _LSt_−1_,_ the difference<br>y variables, the dependent<br>p frms (Micro, market cap<br>percentiles), and big frms<br>rs, the annual samples are<br>of the observations in the<br>and 1963–1982 (Ave Dif),<br>caps, 442 small frms, and<br>ble shows results only for<br>uding preferred stock) are|
|---|
|_NegBt_−1<br>10_._16<br>6_._70<br>3_._78<br>2_._20<br>1_._19<br>0_._53<br>for 1963–1<br>ata for non-f<br>e is _dSt_ (boo<br>planatory var<br>ve earnings f<br>during the f<br>equity; _P/Bt_<br> book equity;<br>e two dumm<br>s for microca<br>d 50th NYSE<br>nce of outlie<br>−1, and 0.5%<br> 1983–2009<br>e 1242 micro<br>  frms. The ta<br>abilities, incl|
|_MCt_<br>0_._01<br>0_._09<br>−1_._00<br>−4_._42<br>−0_._31<br>−4_._07<br>e 2 differ<br>Compustat d<br>dent variabl<br>t_(at)_the ex<br>e and positi<br>idends paid<br>egative book<br>ith positive <br>_St_−1, and th<br>arate result<br>the 20th an<br>ce the infue<br>−1, and _LSt_<br>e slopes for<br>63–1982 us<br>and 705 big<br>change in li|
|_Dt_<br>0.39<br>5.63<br>0.31<br>3.45<br>0.14<br>1.87<br>s in Tabl<br>CRSP and <br>he depen<br>n intercep<br>ith negativ<br>_t_, total div<br>ms with n<br>for frms w<br> _P/Bt_−1,_L_<br>e show sep<br>l, between<br>9. To redu<br>_t_, _Dt_, _P/Bt_<br> the averag<br>ions for 19<br>all frms,<br> for _dLt_ (|
|_NoDt_<br>0.75<br>3.55<br>1.15<br>2.96<br>1.30<br>2.78<br>ion slope<br>009 using <br>ar year _t_. T<br>e regressio<br>or frms w<br>nds in_t_; _D_<br>able for fr<br>d in_t_ −1,<br>pt for _MCt_,<br>f year_t_. W<br>rms (Smal<br> 1983–200<br>ils of _PosY_<br>e between <br>he regress<br>ps, 768 sm<br> the results|
|_PosYt_<br>−0_._21<br>−6_._10<br>−0_._26<br>−5_._92<br>−0_._33<br>−7_._24<br>e regress<br>g 1963–2<br> in calend<br>dition to th<br>earnings f<br>pay divide<br>ummy vari<br>cal yearen<br>  −1. Exce<br>t the end o<br>e), small f<br>–1982 and <br>the right ta<br>e differenc<br>average, t<br>75 microca<br>uation (1)|
|_at_<br>_dAt_<br>_NegYt_<br>Micro<br>Ave Dif<br>−1_._07<br>0_._27<br>−0_._43<br>t-stat<br>−2_._36<br>10_._26<br>−11_._43<br>Small<br>Ave Dif<br>4_._42<br>0_._22<br>−0_._42<br>t-stat<br>3_._28<br>7_._80<br>−2_._96<br>Big<br>Ave Dif<br>1_._75<br>0_._17<br>−0_._41<br>t-stat<br>2_._86<br>7_._43<br>−4_._63<br>**Table A1**. Tests of whether the averag<br>The regressions are estimated each year_t_ durin<br>(after 1972) Nasdaq frms with fscal yearends<br>issued during the fscal year ending in_t)_. In ad<br>in total assets from_t_ −1 to_t_;_NegYt_ and _PosYt_,<br>_t_;_NoDt,_a dummy variable for frms that do not<br>the log of market cap in June of_t_;_NegBt_−1, a d<br>for December of _t_ −1 to book equity for the fs<br>between leverage and target leverage for year_t_<br>and explanatory variables are scaled by assets a<br>in June of year_t_ below the 20th NYSE percentil<br>(Big, above the 50th percentile), and for 1963<br>trimmed, deleting 0.5% of the observations in <br>left tails of _dAt_ and _NegYt_. The table shows th<br>and the_t_-statistic (_t_-stat) for the difference. On<br>581 big frms, and those for 1983–2009 use 23<br>the _dSt_ regressions. Given the constraint of eq|



_Capital Structure Choices_ 

_97_ 







|_LSt_−1|0_._97|0_._71|1_._38|1_._52|0_._41|3_._69|0_._55|0_._52|1_._06|_ntinued_)|
|---|---|---|---|---|---|---|---|---|---|---|
|_P/Bt_−1|−0_._06|0_._11|−0_._56|0_._14|0_._07|2_._07|0_._21|0_._11|1_._91|(_Co_|
|_NegBt_−1|−0_._73|1_._57|−0_._47|1_._89|1_._89|1_._00|2_._59|1_._91|1_._35||
|_MCt_|0_._00|0_._18|−0_._02|0_._14|0_._06|2_._45|0_._15|0_._15|0_._97||
|_Dt_|−0_._01|0_._07|−0_._11|0_._08|0_._04|2_._01|0_._09|0_._07|1_._33||
|_NoDt_|63–1982<br>−0_._12|0_._30|−0_._39|0_._18|0_._33|0_._53|0_._29|0_._42|0_._69||
|_PosYt_|19<br>0_._08|0_._03|2_._19|0_._06|0_._03|1_._82|−0_._01|0_._03|−0_._46||
|_NegYt_|−0_._02|0_._14|−0_._12|−0_._10|0_._07|−1_._40|−0_._08|0_._17|−0_._48||
|_dAt_|−0_._05|0_._02|−2_._84|−0_._06|0_._01|−4_._59|−0_._01|0_._01|−0_._98||
|_at_|Small<br>0_._24|0_._71|0_._34|Big<br>−0_._74|0_._23|−3_._26|Big<br>−0_._99|0_._66|−1_._50||
||ro vs<br>Dif|Err|at|ro vs<br>Dif|Err|at|all vs<br>Dif|Err|at||
||Mic<br>Ave|Std|_t_-st|Mic<br>Ave|Std|_t_-st|Sm<br>Ave|Std|_t_-st||



_Fama and French_ 

_98_ 



|_LSt_−1|5_._61<br>0_._85<br>6_._61<br>5_._57<br>1_._03<br>5_._39<br>−0_._04<br>0_._93<br>−0_._05<br>groups<br>  Amex, and<br>mon shares<br>the change<br>year ending<br>r ending in<br> the ratio of<br>d_LSt_−1_,_the<br>ariables, the<br>s in June of<br> frms (Big)<br>n slopes for<br>ies standard<br>samples are<br>tions in the<br>g frms, and<br> regressions.<br>l except for|
|---|---|
|_P/Bt_−1|0_._16<br>0_._05<br>2_._95<br>0_._47<br>0_._06<br>8_._28<br>0_._31<br>0_._06<br>5_._45<br>ross size<br>ncial NYSE,<br>alue of com<br>les are:_dAt_,<br>r the fscal <br>he fscal yea<br>ity; _P/Bt_−1, <br>equity; an<br>o dummy v<br>market cap<br>les, and big<br>ual regressio<br>its time-ser<br>the annual<br> the observa<br>, and 581 bi<br>for the_dSt_ <br>are identica|
|_NegBt_−1|4_._58<br>1_._47<br>3_._11<br>9_._53<br>1_._79<br>5_._31<br>4_._95<br>2_._20<br>2_._25<br>differ ac<br>a for non-fna<br>s _dSt_ (book v<br>natory variab<br>e earnings fo<br>paid during t<br>ive book equ<br>positive book<br>1, and the tw<br>(Micro) have<br>YSE percenti<br>ween the ann<br>difference to<br>ce of outliers,<br> and 0.5% of <br>2 small frms<br>s results only<br>erred stock)|
|_MCt_|1_._01<br>0_._17<br>5_._76<br>0_._46<br>0_._12<br>3_._79<br>−0_._55<br>0_._20<br>−2_._78<br>Table 2<br>pustat dat<br> variable i<br>_)_the expla<br>nd positiv<br>dividends <br>with negat<br>frms with<br>_t_−1, _LSt_−<br>ocap frms<br>and 50th N<br>rences bet<br>he average<br>he infuen<br>and _LSt_−1,<br>rocaps, 44<br>table show<br>uding pref|
|_Dt_|0_._07<br>0_._07<br>1_._00<br>0_._33<br>0_._08<br>4_._08<br>0_._26<br>0_._08<br>3_._27<br>lopes in<br>P and Com<br>dependent<br>tercept (_at_<br> negative a<br> _Dt_, total <br> for frms <br> _t_ −1, for<br>or _MCt_, _P/B_<br>ear_t_. Micr<br> the 20th <br>f the diffe<br>e ratio of t<br>To reduce t<br>_t_, _P/Bt_−1, <br>e 1242 mic<br>frms. The<br>ilities, incl|
|_NoDt_|83–2009<br>−0_._51<br>0_._29<br>−1_._75<br>−0_._37<br>0_._30<br>−1_._24<br>0_._14<br>0_._31<br>0_._45<br>ession s<br>using CRS<br>ear _t_. The <br>gression in<br>frms with <br>ends in _t_; <br>y variable <br>yearend in<br>1. Except f<br>e end of y<br>re between<br>(Ave Dif) o<br>erence (th<br>ferences).<br>f _PosYt_, _D_<br>3–1982 us<br>d 705 big<br>nge in liab|
|_PosYt_|19<br>0_._12<br>0_._03<br>4_._07<br>0_._18<br>0_._03<br>5_._47<br>0_._06<br>0_._02<br>2_._50<br>age regr<br>963–2009  <br>calendar y<br>n to the re<br>nings for <br>t pay divid<br>1, a dumm<br>r the fscal<br>r year_t_ −<br>assets at th<br> (Small) a<br>age values<br>verage diff<br>annual dif<br>ight tails o<br>ons for 196<br>l frms, an<br>r _dLt_ (cha|
|_NegYt_|−0_._03<br>0_._03<br>−0_._86<br>−0_._12<br>0_._05<br>−2_._62<br>−0_._10<br>0_._05<br>−2_._06<br>the aver<br>r _t_ during 1<br>earends in <br>_)_. In additio<br>d _PosYt_, ear<br> that do no<br>of _t_; _NegBt_−<br>ok equity fo<br>leverage fo<br>e scaled by<br>small frms <br>shows aver<br>at) for the a<br>ation of the<br>ions in the r<br>the regressi<br>ps, 768 smal<br>e results fo<br>tats.|
|_at_<br>_dAt_|ro vs Small<br>Dif<br>−5_._25<br>0_._01<br>Err<br>1_._07<br>0_._02<br>at<br>−4_._89<br>0_._40<br>ro vs Big<br>Dif<br>−3_._57<br>0_._04<br>Err<br>0_._66<br>0_._02<br>at<br>−5_._42<br>2_._44<br>all vs Big<br>Dif<br>1_._68<br>0_._03<br>Err<br>1_._31<br>0_._02<br>at<br>1_._28<br>2_._19<br>**able A2**. Tests of whether<br> regressions are estimated each yea<br>er 1972) Nasdaq frms with fscal y<br>ed during the fscal year ending in_t_<br>otal assets from _t_-1 to _t_; _NegYt_ an<br> _NoDt_, a dummy variable for frms<br>_Ct_, the log of market cap in June <br>ket cap for December of_t_ −1 to bo<br>rence between leverage and target<br>endent and explanatory variables ar<br> _t_ below the 20th NYSE percentile,<br>above the 50th percentile. The table<br>size groups, and the_t_-statistic (_t_-St<br>r, estimated using the standard devi<br>med, deleting 0.5% of the observat<br>tails of_dAt_ and_NegYt_. On average,<br>e for 1983–2009 use 2375 microca<br>n the constraint of equation (1) th<br>nges in the signs of all slopes and_t_-s|
||Mic<br>Ave<br>Std<br>_t_-st<br>Mic<br>Ave<br>Std<br>_t_-st<br>Sm<br>Ave<br>Std<br>_t_-st<br>**T**<br>The <br>(aft<br>issu<br>in t<br>in _t_;<br>_t_; _M_<br>mar<br>diffe<br>dep<br>year<br>are<br>two<br>erro<br>trim<br>left<br>thos<br>Give<br>cha|



_Capital Structure Choices_ 

_99_ 

## **Acknowledgments** 

Jeffrey Pontiff, two referees, and the editor (Ivo Welch) provided helpful comments. 

## **References** 

- Bagwell, L. and J. Shoven. 1989. “Cash Distributions to Shareholders.” _Journal of Economic Perspectives_ 3(Summer): 129–149. 

- Baker, M., R. S. Ruback, and J. Wurgler. 2007. “Behavioral Corporate Finance: A Survey.” In _Handbook of Corporate Finance: Empirical Corporate Finance_ , B. Espen Eckbo, ed., Volume 1 (North Holland/Elsevier, Handbooks in Finance Series), Ch. 4. 

- Baker, M. and J. Wurgler. 2002. “Market Timing and Capital Structure.” _Journal of Finance_ 57: 1–32. 

- Benmelech, E. 2009. “Asset Salability and Debt Maturity: Evidence from Nineteenth-century American Railroads.” _Review of Financial Studies_ 22: 1545–1584. 

- Bertrand, M. and A. Schoar. 2003. “Managing with Style: The Effect of Managers on Firm Policies.” _Quarterly Journal of Economics_ 118: 1168–1208. 

- Cohen, R. B., C. Polk, and T. Vuolteenaho. 2003. “The Value Spread.” _Journal of Finance_ 58: 609–641. 

- Cronqvist, H., A. K. Makhija, and S. E. Yonker. 2011. “Behavioral Consistency in Corporate Finance: CEO Personal and Corporate Leverage.” _Journal of Financial Economics_ , forthcoming. 

- Davis, J. L., E. F. Fama, and K. R. French. 2000. “Characteristics, Covariances, and Average Returns: 1929–1997.” _Journal of Finance_ 55: 389–406. 

- DeAngelo, H., L. DeAngelo, and R. M. Stulz. 2010. “Seasoned Equity Offerings, Market Timing, and the Corporate Lifecycle.” _Journal of Financial Economics_ 95: 275–295. 

- DeAngelo, H. and R. Roll. 2011. “How Stable are Corporate Capital Structures?” Manuscript, March. 

- DeBondt, W. F. M. and R. Thaler. 1985. “Does the Stock Market Overreact?” _Journal of Finance_ 40: 793–805. 

- Diamond, D. W. 2004. “Presidential Address, Committing to Commit: Short-Term Debt when Enforcement is Very Costly.” _Journal of Finance_ 59: 1447–1479. 

- Eckbo, B. E., R. W. Masulis, and Ø. Norli. 2007. “Security Offerings.” In _Handbook of Corporate Finance: Empirical Corporate Finance_ , B. Espen Eckbo, ed., Volume 1 (North Holland/Elsevier, Handbooks in Finance Series), Ch. 6. 

- Fama, E. F. and H. Babiak. 1968. “Dividend Policy of Individual Firms: An Empirical Analysis.” _Journal of the American Statistical Association_ 63: 1132–1161. 

- Fama, E. F. and K. R. French. 1995. “Size and Book-to-Market Factors in Earnings and Returns.” _Journal of Finance_ 50: 131–156. 

- Fama, E. F. and K. R. French. 2001. “Disappearing Dividends: Changing Firm Characteristics or Lower Propensity to Pay?” _Journal of Financial Economics_ 60: 3–43. 

- Fama, E. F. and K. R. French. 2002. “Testing Tradeoff and Pecking Order Predictions about Dividends and Debt.” _Review of Financial Studies_ 15(Spring 2002): 1–33. 

- Fama, E. F. and K. R. French. 2005. “Financing Decisions: Who Issues Stock?” _Journal of Financial Economics_ 76: 549–582. 

_Fama and French_ 

_100_ 

- Fama, E. F. and J. MacBeth. 1973. “Risk, Return, and Equilibrium: Empirical Tests.” _Journal of Political Economy_ 81: 607–636. 

- Flannery, M. J. and K. P. Rangan. 2006. “Partial Adjustment Toward Target Capital Structures.” _Journal of Financial Economics_ 79: 469–506. 

- Frank, M. Z. and V. K. Goyal. 2003. “Testing the Pecking Order Theory of Capital Structure.” _Journal of Financial Economics_ 67: 217–248. 

- Graham, J. R. and C. R. Harvey. 2001. “The Theory and Practice of Corporate Finance: Evidence from the Field.” _Journal of Financial Economics_ 60: 187–243. 

- Graham, J. R. and M. T. Leary. 2011. “A Review of Empirical Capital Structure Research and Directions for the Future.” _Annual Review of Financial Economics_ 3. 

- Graham, J. R. and K. Narasimhan. 2004. “Corporate Survival and Managerial Experiences During the Great Depression.” Manuscript. 

- Hovakimian, A. and G. Li. 2011. “In Search of Conclusive Evidence: How to Test for Adjustment to Target Capital Structure.” _Journal of Corporate Finance_ 17: 33–44. 

- Huang, R. and J. Ritter. 2009. “Testing Theories of Capital Structure and Estimating the Speed of Adjustment.” _Journal of Financial and Quantitative Analysis_ 44: 237–271. 

- Iliev, P. and I. Welch. 2010. “Reconciling Estimates of the Speed of Adjustment of Leverage Ratios.” Manuscript. 

- Kayhan, A. and S. Titman. 2007. “Firms’ Histories and Their Capital Structures.” _Journal of Financial Economics_ 83: 1–32. 

- Lakonishok, J., A. Shleifer, and R. W. Vishny. 1994. “Contrarian Investment, Extrapolation, and Risk.” _Journal of Finance_ 49: 1541–1578. 

- Leary, M. T. and M. R. Roberts. 2005. “Do Firms Rebalance Their Capital Structures?” _Journal of Finance_ 60: 2575–2619. 

- Lewellen, K. 2006. “Financing Decisions when Managers are Risk Averse.” _Journal of Financial Economics_ 82: 551–589. 

- Lintner, J. 1956. “Distribution of Incomes of Corporations Among Dividends, Retained Earnings, and Taxes.” _American Economic Review_ 46: 97–113. 

- Miller, M. H. 1977. “Debt and Taxes.” _Journal of Finance_ 32: 261–275. 

- Modigliani, F. and M. H. Miller. 1968. “The Cost of Capital, Corporation Finance, and the Theory of Investment.” _American Economic Review_ 48: 261–297. 

- Myers, S. C. 1984. “The Capital Structure Puzzle.” _Journal of Finance_ 39: 575–592. 

- Myers, S. C. and N. S. Majluf. 1984. “Corporate Financing and Investment Decisions when Firms Have Information the Investors Do Not Have.” _Journal of Financial Economics_ 13: 187–221. 

- Parsons, C. and S. Titman. 2008. “Empirical Capital Structure: A Review.” _Foundations and Trends in Finance_ 3: 1–93. 

- Polk, C. and P. Sapienza. 2009. “The Stock Market and Corporate Investment: A Test of Catering Theory.” _Review of Financial Studies_ 22: 187–217. 

- Rampini, A. A. and S. Viswanathan. 2010. “Collateral and Capital Structure.” Manuscript. 

- Rauh, J. and A. Sufi. 2010. “Product Markets, Leases, and Asset Similarity.” _Review of Finance_ , forthcoming. 

- Rhodes-Kropf, M., D. T. Robinson, and S. Viswanathan. 2005. “Valuation Waves and Merger Activity: The Empirical Evidence.” _Journal of Financial Economics_ 77: 561–603. 

- Shyam-Sunder, L. and S. Myers. 1999. “Testing Static Tradeoff Against Pecking Order Models of Capital Structure.” _Journal of Financial Economics_ 51: 219–244. 

_101_ 

_Capital Structure Choices_ 

- Skinner, D. J. 2008. “The Evolving Relation Between Earnings, Dividends, and Stock Repurchases.” _Journal of Financial Economics_ 87: 582–609. 

- Welch, I. 2004. “Capital Structure and Stock Returns.” _Journal of Political Economy_ 112: 106–131. 

- Welch, I. 2011. “Two Common Problems in Capital Structure Research: The Financial-Debtto-Asset Ratio and Issuing Activity Versus Leverage Changes.” _International Review of Finance_ 11: 1–17. 

