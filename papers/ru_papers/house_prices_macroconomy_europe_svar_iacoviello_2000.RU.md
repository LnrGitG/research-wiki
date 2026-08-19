---
title: "House Prices and the Macroeconomy in Europe: Results from a Structural VAR Analysis"
authors: "Matteo Iacoviello"
year: 2000
publisher: "ECB"
type: working-paper
series: "ECB Working Paper Series"
number: 18
url: https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp018.pdf
source_pdf: raw/papers/Iacoviello. HOUSE PRICES AND THE MACROECONOMY IN EUROPE.pdf
converted: 2026-08-19
language: en
note: "Re-extracted from ECB source. 42/66 pages have clear text. Pages 1, 3, 44-65 use custom font encoding (garbled)."
---

# House Prices and the Macroeconomy in Europe: Results from a Structural VAR Analysis

**Matteo Iacoviello**
**April 2000**

**ECB Working Paper No. 18**

## Abstract

This paper uses a structural vector autoregressive (SVAR) approach to identify the main macroeconomic factors behind fluctuations in house prices in six European countries (France, Germany, Italy, Spain, Sweden and UK) over the last twenty-five years. Quarterly time series for GDP, house prices, money, inflation and interest rates are characterised by a multivariate process driven by supply, nominal, monetary, inflation and demand shocks. The results show that: (i) adverse monetary shocks have generally a significant negative impact on real house prices, and the timing of the response in house prices matches that of output; (ii) the magnitude of the response in house prices to a monetary shock can be partly justified by looking at the different housing and financial market institutions in the countries; (iii) monetary and demand shocks play an important role in driving house price fluctuations over the short run. The paper also interprets the major house price cycles and their link with the economic activity in light of the estimated shocks. Overall, the approach suggests that house prices can be embedded in a relatively simple macroeconometric model in a useful way, and that understanding their dynamics can shed some light over several macroeconomic episodes of the last quarter of century in Europe.

## Non-executive summary

In the last three decades or so, big changes in asset prices have occurred in many industrialised economies. While it is felt that macroeconomic factors in general and monetary policy conditions in particular were an important factor behind asset price inflation and deflation, there appears to be a lot of uncertainty upon the impact of these factors on long-term asset prices, such as those of equity, land and real estate. It is agreed that central banks should pursue primarily the goal of price stability, but the question of whether they should also react to asset price movements is still open. The issue is complicated by the fact that the link between asset prices and macroeconomic fluctuations is still poorly understood from an empirical point of view.

## Contents

1. Introduction
2. Theories and evidence on house price fluctuations
   2.1 Housing market characteristics and the "microeconomics" of house prices
   2.2 Housing markets, monetary policy and the macroeconomy
3. Econometric methodology: Vector Autoregressions and Common Trends
   3.1 Why VARs?
   3.2 The empirical methodology
   3.3 Hypotheses about cointegration
   3.4 Identifying structural shocks
4. Properties of the data
   4.1 Sources of data
   4.2 Unit root and Cointegration Tests
   4.3 Cointegration relations
5. Empirical evidence
   5.1 Impulse responses
   5.2 Variance decompositions
6. An informal interpretation of house price movements
7. Conclusions
A. The Common Trends Methodology
B. Comparing monetary shocks in Europe
References
Figures

---

E U R O P E A N C E N T R A L B A N K
WORKING PAPER SERIES
WORKING PAPER NO. 
WORKING PAPER NO. 18
18
HOUSE PRICES AND THE
MACROECONOMY IN EUROPE:
RESULTS FROM A STRUCTURAL
VAR ANALYSIS
BY MATTEO IACOVIELLO
APRIL 2000
 
  
 

 

 
 7KDQNV,WKDQNPDQ\SHRSOHDWWKH(&%HVSHFLDOO\,JQD]LR$QJHORQL*XQWKHU&RHQHQ%HQRLW0RMRQ)UDQN6PHWVDQGDQDQRQ\PRXVUHIHUHH,DPDOVRJUDWHIXOWR+HQULN+DQVHQDQG$QGHUV:DUQHIRUSURYLGLQJ
PHZLWKWKH5$76FRGHVDQGKHOSLQLPSOHPHQWLQJWKHFRPPRQWUHQGVSURFHGXUH,ZRXOGDOVROLNHWRWKDQN0LFKDHO(KUPDQQ5DVPXV)DWXP1REXKLUR.L\RWDNL&ODXGLD2JOLDORURDQG'DQQ\4XDKIRUKHOSIXO
GLVFXVVLRQV)LQDOO\,DPSDUWLFXODUO\LQGHEWHGWR5DRXO0LQHWWLVLQFHWKHPDLQLGHDVRIWKLVSDSHUDUHWKHUHVXOWRIFROODERUDWHGZRUNZLWKKLP2IFRXUVHDOOWKHHUURUVDUHPLQH7KHRSLQLRQVH[SUHVVHGLQWKLVZRUN
GRQRWQHFHVVDULO\UHIOHFWWKHYLHZVRIWKH(XURSHDQ&HQWUDO%DQN
0DWWHR,DFRYLHOORHPDLODGGUHVV0,DFRYLHOOR#OVHDFXN
ECB Working Paper No 18 April 2000
3
Contents
Abstract
4
Non executive summary
5
1
Introduction
6
2
Theories and evidence on house price fluctuations
7
2.1
Housing market characteristics and the “microeconomics”
of house prices
8
2.2
Housing markets, monetary policy and the macroeconomy
9
3
Econometric methodology: Vector Autoregressions and
Common Trends
11
3.1
Why VARs?
3.2
The empirical methodology
12
3.3
Hypotheses about cointegration
13
3.4
Identifying structural shocks
15
4
Properties of the data
17
4.1
Sources of data
17
4.2
Unit root and Cointegration Tests
19
4.2.1 Unit root tests
19
4.2.2 Cointegration tests
19
4.3
Cointegration relations
21
5
Empirical evidence
22
5.1
Impulse responses
22
5.1.1 Permanent shocks
23
5.1.2 Temporary shocks
25
5.2
Variance decompositions
30
6
An informal interpretation of house price movements
31
7
Conclusions
33
A
The Common Trends Methodology
35
B
Comparing monetary shocks in Europe
38
References
39
Figures
43
ECB Working Paper No 18   April 2000
4
Abstract
This paper uses a structural vector autoregressive (SVAR) approach to identify the main
macroeconomic factors behind fluctuations in house prices in six European countries (France,
Germany, Italy, Spain, Sweden and UK) over the last twenty-five years. Quarterly time series for GDP,
house prices, money, inflation and interest rates are characterised by a multivariate process driven by
supply, nominal, monetary, inflation and demand shocks. The results show that: (i) adverse monetary
shocks have generally a significant negative impact on real house prices, and the timing of the
response in house prices matches that of output; (ii) the magnitude of the response in house prices
to a monetary shock can be partly justified by looking at the different housing and financial market
institutions in the countries; (iii) monetary and demand shocks play an important role in driving
house price fluctuations over the short run. The paper also interprets the major house price cycles
and their link with the economic activity in light of the estimated shocks. Overall, the approach
suggests that house prices can be embedded in a relatively simple macroeconometric model in a
useful way, and that understanding their dynamics can shed some light over several macroeconomic
episodes of the last quarter of century in Europe.
ECB Working Paper No 18 April 2000
5
Non executive summary
In the last three decades or so, big changes in asset prices have occurred in many industrialised
economies. While it is felt that macroeconomic factors in general and monetary policy conditions in
particular were an important factor behind asset price inflation and deflation, there appears to be a
lot of uncertainty upon the impact of these factors on long-term asset prices, such as those of equity,
land and real estate. It is agreed that central bankers should respond to asset price volatility in the
context of an overall strategy for monetary policy, and the profession seems to converge on the
effects of an exogenous monetary shock on output and consumer prices. However, less is known on
how to respond to asset price volatility, as well on the impact of macroeconomic disturbances on
asset prices.
To address the second of these two issues, the paper uses a structural vector autoregressive (SVAR)
approach to identify the main macroeconomic factors behind fluctuations in house prices in six
European countries (France, Germany, Italy, Spain, Sweden and UK) over the last twenty-five years. It
uses quarterly time series for GDP, house prices, money, inflation and interest rates to understand
how these variables react to supply, nominal, monetary, inflation and demand shocks.
The results show that:
1)
adverse monetary shocks have generally a significant negative impact on real house prices, and
the timing of the response in house prices matches that of aggregate GDP;
2)
the magnitude of the response in house prices to a monetary shock can be partly justified by
looking at the different housing and financial market institutions in the countries;
3)
Monetary and demand shocks play an important role in driving house price fluctuations over the
short run.
The paper also interprets the major house price cycles and their link with the economic activity in
light of the estimated shocks. It appears that the major boom-busts in house prices occurred in the
countries under exam over the last decades have been driven by a combination of factors all pushing
in the same direction.
The overall contribution of the paper is three-fold: first, the approach suggests that house prices can
be embedded in an effective way in a relatively simple macroeconometric model that can provide
some quantitative estimates of the sensitivity of asset prices to macroeconomic conditions. Secondly,
it provides evidence that house prices, as expected, are much more sensitive than consumer prices to
the stance of monetary policy and to other macroeconomic disturbances. Thirdly, it shows that
understanding house price dynamics can shed some light over several macroeconomic episodes of
the last quarter of century in Europe.
4 Lqwurgxfwlrq
Lq wkh odvw wkuhh ghfdghv ru vr elj fkdqjhv lq dvvhw sulfhv kdyh rffxuuhg lq pdq| lqgxvwuldolvhg
hfrqrplhv1 Zkloh lw lv ihow wkdw pdfurhfrqrplf idfwruv lq jhqhudo dqg prqhwdu| srolf| frqglwlrqv
lq sduwlfxodu zhuh dq lpsruwdqw idfwru ehklqg dvvhw sulfh lq dwlrq dqg gh dwlrq4/ wkhuh dsshduv
wr eh d orw ri xqfhuwdlqw| xsrq wkh hhfwv ri wkhvh idfwruv rq orqj0whup dvvhw sulfhv/ vxfk dv wkrvh
ri htxlw|/ odqg dqg uhdo hvwdwh1 Lw lv djuhhg wkdw fhqwudo edqnhuv rxjkw wr uhvsrqg wr dvvhw sulfh
yrodwlolw| lq wkh frqwh{w ri dq ryhudoo vwudwhj| iru prqhwdu| srolf|/ dqg wkh surihvvlrq vhhpv wr
frqyhujh rq wkh hhfwv ri dq h{rjhqrxv prqhwdu| srolf| vkrfn rq rxwsxw dqg frqvxphu sulfhv51
Krzhyhu/ ohvv lv nqrzq rq krz wr uhvsrqg wr dvvhw sulfh yrodwlolw|/ dv zhoo rq wkh lpsdfw ri
pdfurhfrqrplf glvwxuedqfhv rq dvvhw sulfhv61 Erwk wkhvh frqfhuqv zhuh rq wkh djhqgd lq wkh
4<<< Ndqvdv Ihg V|psrvlxp Qhz Fkdoohqjhv iru Prqhwdu| Srolf|= v|psrvlxp sduwlflsdqwv
qrwhg wkdw wkh lqwhusuhwdwlrq ri dvvhw sulfh fkdqjhv zdv frpsolfdwhg ehfdxvh ri sureohpv lq
glvwlqjxlvklqj pryhphqwv gulyhq e| hfrqrplf ixqgdphqwdov iurp dvvhw sulfh exeeohv1 Wkh|
dovr djuhhg wkdw uhvhdufk zdv qhhghg wr lghqwli| wkh fkdqqhov e| zklfk dvvhw sulfh fkdqjhv duh
wudqvplwwhg lqwr wkh uhdo hfrqrp| dqg wr ghwhuplqh wkh txdqwlwdwlyh lpsruwdqfh ri wkhvh hhfwv
+Vhoorq dqg Exvndv/ 4<<<,1
Wklv sdshu wdnhv d suholplqdu| vwhs wrzdugv wkh vhfrqg srlqw/ dqdo|vlqj lq d vwuxfwxudo yhfwru
dxwruhjuhvvlrq +YDU, frqwh{w krz krxvh sulfhv uhvsrqg wr wkh pdlq vkrfnv wkdw duh wkrxjkw
wr gulyh hfrqrplf xfwxdwlrqv/ xvlqj gdwd rq vl{ pdmru Hxurshdq hfrqrplhv1 Sxwwlqj krxvh
sulfhv lq dq rwkhuzlvh vwdqgdug YDU pd| dsshdu sx}}olqj dw uvw vljkw1 \hw d odujh iudfwlrq ri
shuvrqdo vhfwru*v qhw zruwk lq wkh ghyhorshg hfrqrplhv lv lq wkh irup ri krxvlqj htxlw|7/ dqg wkh
wrwdo ydoxh ri wkh krxvlqj vwrfn h{fhhgv JGS/ riwhq vxevwdqwldoo|> fkdqjhv lq lwv ydoxh fdq kdyh
hhfwv rq djjuhjdwh frqvxpswlrq/ ru rq wkh delolw| ri krxvhkrogv wr eruurz iru frqvxpswlrq ru
surgxfwlrq/ wkxv wudqvplwwlqj wkhlu hhfwv wr wkh uhdo hfrqrp|1
Xvlqj d YDU wr h{sodlq krxvh sulfhv fdq dovr khos glvhqwdqjolqj krz pxfk ri wkh yduldelolw|
lq krxvh sulfhv lv dwwulexwdeoh wr prqhwdu| dqg rwkhu idfwruv/ vxfk dv ghpdqg dqg vxsso| glvwxu0
edqfhv1 Dowkrxjk lw grhv qrw doorz wr dqdo|vh gluhfwo| wkh olqn ehwzhhq qdqfldo olehudolvdwlrq
dqg krxvh sulfhv wkdw kdv uhfhlyhg d orw ri dwwhqwlrq lq uhfhqw olwhudwxuh8/ lw kdv wkh yluwxh wr
jlyh vrph txdolwdwlyh dqg txdqwlwdwlyh hylghqfh rq wkh lqwhuuhodwlrqvklsv ehwzhhq wkh krxvlqj
4 Vhh/ dprqj wkh rwkhuv/ Vkljhpl +4<<8,/ Lwr dqg Lzdlvdnr +4<<8,/ Kxwfklvrq +4<<7,/ Ehuqdqnh dqg Jhuwohu
+4<<<,1
5 Rq wkh qdwxuh ri wklv djuhhphqw/ vhh Fkulvwldqr hw do1+4<<<, dqg Vlpv +4<<;,1
6 Vrph h{fhswlrqv duh Odvwudshv +4<<;, rq wkh hhfw ri prqhwdu| vkrfnv rq vwrfn sulfhv lq wkh J: frxqwulhv
dqg Kxwfklvrq +4<<7, rq prqhwdu| vkrfnv dqg odqg sulfhv lq Mdsdq1 Rq krz wr uhvsrqg wr dvvhw sulfh yrodwlolw|/
vhh Ehuqdqnh dqg Jhuwohu +4<<<,1
7 Wklv iudfwlrq lv ehwzhhq 83 dqg :3 shufhqw/ dffruglqj wr Srwhued +4<<4,1
8 Vhh iru lqvwdqfh wkh sdshuv e| Plohv +4<<5, dqg Ruwdor0Pdjqh* dqg Udg| +4<<<,1
pdunhw dqg wkh zlghu hfrqrp|1 Orrnlqj dw pruh wkdq rqh frxqwu|/ lq dgglwlrq/ fdq surylgh d
urexvwqhvv fkhfn iru wkh uhvxowv/ dv zhoo dv jlylqj lqglfdwlrqv xsrq wkh glhuhqfhv lq wkh wudqv0
plvvlrq phfkdqlvp1 Wklv lv sduwlfxoduo| lpsruwdqw lq wkh oljkw ri wkh idfw wkdw krxvlqj pdunhwv
glhu vljqlfdqwo| ehwzhhq Hxurshdq frxqwulhv/ dqg wkhvh glhuhqfhv pljkw sod| d sduw lq wkh
wudqvplvvlrq phfkdqlvp ri wkh vkrfnv1
Wkh uhvxowv ri wkh sdshu fdq eh vxppdulvhg dv iroorzv= yhfwru dxwruhjuhvvlrqv xvlqj gdwd
rq krxvh sulfhv dqg rwkhu pdfurhfrqrplf yduldeohv lq vl{ pdmru Hxurshdq hfrqrplhv +Iudqfh/
Jhupdq|/ Lwdo|/ Vsdlq/ Vzhghq dqg XN, uhyhdo wkdw= +l, dgyhuvh prqhwdu| vkrfnv kdyh jhqhudoo|
d vljqlfdqw qhjdwlyh lpsdfw rq uhdo krxvh sulfhv/ zlwk d wlplqj lq wkh uhvsrqvh ri krxvh sulfhv
wkdw pdwfkhv wkdw ri rxwsxw> +ll, wkh pdjqlwxgh ri wkh uhvsrqvh ri krxvh sulfhv wr d prqhwdu|
glvwxuedqfh fdq eh sduwo| mxvwlhg e| orrnlqj dw wkh glhuhqw krxvlqj dqg qdqfldo pdunhw
lqvwlwxwlrqv lq wkh frxqwulhv> +lll, prqhwdu| dqg ghpdqg vkrfnv sod| dq lpsruwdqw uroh lq gulylqj
krxvh sulfh xfwxdwlrqv ryhu wkh vkruw uxq1 Lq dgglwlrq/ wkh dssurdfk |lhogv sodxvleoh uhvxowv
iru wkh uhvsrqvhv ri wkh rwkhu yduldeohv lq wkh prgho/ wkxv vxjjhvwlqj wkdw krxvh sulfhv fdq eh
hpehgghg lq d uhodwlyho| vlpsoh pdfurhfrqrphwulf prgho lq dq hhfwlyh zd|1
Wkh uhpdlqghu ri sdshu lv rujdqlvhg dv iroorzv= wkh qh{w Vhfwlrq vxuyh|v wkhru| dqg hylghqfh
rq krxvh sulfh xfwxdwlrqv dqg wkh pdfurhfrqrp|1 Vhfwlrq 6 h{sodlqv krz d YDU iudphzrun
fdq eh xvhixoo| dgrswhg wr ghvfuleh wkh pdlq pdfurhfrqrplf irufhv gulylqj krxvh sulfhv dqg
od|v rxw wkh hfrqrphwulf phwkrgrorj|/ wkdw uholhv rq wkh frpprq wuhqgv dssurdfk ghyhorshg
e| Nlqj/ Sorvvhu/ Vwrfn dqg Zdwvrq +NSVZ/ khqfhiruwk, +4<<4,1 Vhfwlrq 7 ghvfulehv wkh gdwd
dqg wkhlu wlph0vhulhv surshuwlhv1 Vhfwlrq 8 suhvhqwv wkh pdlq uhvxowv/ l1h1 lpsxovh uhvsrqvhv dqg
yduldqfh ghfrpsrvlwlrqv1 Vhfwlrq 9 xvhv wkh hvwlpdwhg vwuxfwxudo vkrfnv wr lqwhusuhw wkh pdmru
pdfurhfrqrplf hslvrghv wkdw kdyh dffrpsdqlhg dvvhw sulfh pryhphqwv lq wkh frxqwulhv xqghu
h{dp ryhu wkh odvw 53 |hduv ru vr1 Ilqdoo|/ Vhfwlrq : frqfoxghv1
5 Wkhrulhv dqg hylghqfh rq krxvh sulfh xfwxdwlrqv
Vlqfh wkh wkhruhwlfdo dqg hpslulfdo olwhudwxuh rq krxvh +dqg/ lq jhqhudo/ dvvhw, sulfh g|qdplfv
dqg wkhlu olqn zlwk wkh pdfurhfrqrp| lv hqruprxv/ lw zrxog eh xqzlvh wr dwwhpsw wr ixoo|
uhylhz lw khuh1 L kdyh slfnhg rxw iru glvfxvvlrq d qxpehu ri sdshuv wkdw duh pruh forvho| uhodwhg
wr wkh dssurdfk ri wklv zrun1
L kdyh vhsdudwhg vwxglhv wkdw duh pruh vshflf wr wkh krxvh
sulfh g|qdplfv lq sduwlfxodu iurp wkrvh wkdw wu| wr exlog d eulgjh ehwzhhq krxvh sulfhv dqg wkh
pdfurhfrqrp|1
ECB Working Paper No 18 G April 2000                                                                                                      7
514 Krxvlqj pdunhw fkdudfwhulvwlfv dqg wkh plfurhfrqrplfv ri krxvh sulfhv
Wkhuh duh pdq| uhdvrqv zk| wkh krxvlqj pdunhw lv xqolnh wkh pdunhwv iru pdq| rwkhu jrrgv
dqg vhuylfhv +vhh Nhqq|/ 4<<;,1
Krxvlqj jrrgv kdyh d gxdo qdwxuh ri frpprglwlhv dqg ri
lqyhvwphqw dvvhw/ qrupdoo| dffrxqwlqj iru d pxfk juhdwhu iudfwlrq ri krxvhkrog qhw zruwk wkdq
frusrudwh htxlw| +Srwhued/ 4<<4,1 Wkhuh duh dovr pdq| rwkhu vshfldo ihdwxuhv ri wkh krxvlqj
pdunhw +Txljoh|/ 4<<5/ dqg Plohv/ 4<<8,= +l, lwv uhodwlyho| kljk frvw ri vxsso|/ +ll, lwv gxudelolw|/
+lll, lwv khwhurjhqhlw|/ +ly, lwv orfdwlrqdo {lw|/ +y, wkh srvvlelolw| wr udlvh ordqv djdlqvw krxvlqj
froodwhudo> +yl, wkh h{lvwhqfh ri d zhoo0ghyhorshg vhfrqgdu| pdunhw1 Wkhvh ihdwxuhv lpso| wkdw wkh
krxvlqj pdunhw lv uhdoo| d froohfwlrq ri orrvho| frqqhfwhg exw vhjphqwhg pdunhwv1 Dv d uhvxow/
wdonlqj ri krxvh sulfhv lq jhqhudo lv d elw kd}dugrxv/ dowkrxjk lw wxuqv rxw wr eh d qhfhvvdu|
devwudfwlrq iru wkh sxusrvhv ri wkh sdshu1
Lq wkh vlpsohvw wkhruhwlfdo iudphzrun/ gxh wr Srwhued +4<;7,/ wkh krxvlqj pdunhw lv ghvfulehg
dv frqvlvwlqj ri wzr vhsdudwh pdunhwv/ rqh iru wkh vwrfn ri h{lvwlqj krphv/ zklfk ghwhuplqhv wkhlu
sulfh/ dqg wkh rwkhu iru wkh qhz frqvwuxfwlrq rz/ zklfk ghwhuplqhv wkh ohyho ri qhz lqyhvwphqw1
Htxloleulxp uhtxluhv wkdw krphrzqhuv0lqyhvwruv hduq wkh vdph uhwxuq rq krxvlqj lqyhvwphqw dv
rq rwkhu dvvhwv/ zkhuh krxvlqj uhwxuq lv wkh vxp ri wkh ydoxh ri uhqwdo vhuylfhv dqg fdslwdo
jdlqv1 Wkh ydoxh ri uhqwdo vhuylfhv lv dvvxphg wr eh ghwhuplqhg lq d shuihfw pdunhw iru krxvlqj
vhuylfhv/ htxdwlqj ghpdqg dqg +suhghwhuplqhg, vxsso|1 Wkh g|qdplfv ri vxsso| frph iurp d
Wrelq*v t0w|sh lqyhvwphqw ixqfwlrq1 Jlyhq fxuuhqw krxvh sulfhv/ wklv ghwhuplqhv ixwxuh vxsso|
dqg khqfh wrpruurz*v uhqw/ dqg khqfh/ yld duelwudjh/ wkh udwh ri fdslwdo jdlqv1 Dffruglqj wr
wklv prgho/ d vxgghq ghpdqg vkrfn +h1j1/ dq lqfuhdvh iroorzlqj d idyrxudeoh wd{ uhirup, fdxvhv
uhqwv wr lqfuhdvh lq rughu wr pdlqwdlq htxloleulxp1 Wklv zloo ohdg lqyhvwphqwv wr lqfuhdvh/ zklfk
zloo lqgxfh h{shfwdwlrqv ri ixwxuh uhqw ghfuhdvhv iurp wkh qhz kljkhu ohyho dv wkh vwrfn dgmxvwv
xszdugv1 Wklv lpsolhv wkdw dq xqh{shfwhg srvlwlyh vkrfn wr wkh krxvlqj pdunhw zloo kdyh dq
lpphgldwh srvlwlyh lpsdfw rq krxvh sulfhv/ zklfk zloo eh iroorzhg e| dq dgmxvwphqw wrzdugv
wkh orqj0uxq htxloleulxp lq zklfk wkhuh zloo eh frqwlqxrxv sulfh ghfuhdvhv1 Wkhuhiruh/ sulfhv
zloo kdyh d phdq0uhyhuwlqj whqghqf|1 Pruh lpsruwdqwo|/ revhuyhg sulfh pryhphqwv zloo uh hfw d
frpelqdwlrq ri vkrfnv dqg dgmxvwphqw phfkdqlvpv/ wkh odwwhu lpso|lqj srvlwlyh dxwrfruuhodwlrqv
lq wkh krxvh sulfhv1
Wklv vwdqgdug prgho lpsolhv wkdw/ iroorzlqj d vkrfn/ krxvh sulfhv zloo vprrwko| dgmxvw wr0
zdugv htxloleulxp1 Ri frxuvh/ lw lv qrw wkh rqo| srvvlelolw|= phfkdqlvpv wkdw zrxog jlyh ulvh
wr f|folfdo dgmxvwphqw lqyroyh/ iru lqvwdqfh/ eruurzlqj frqvwudlqwv/ olnh lq Vwhlq +4<<8,1 Vwhlq*v
vwduwlqj srlqw lv wkdw wkh sxufkdvh ri d krxvh uhtxluhv d vxevwdqwldo grzq sd|phqw1 Dw dq| ohyho
ri krxvh sulfhv/ idplolhv0ex|huv +zkr douhdg| rzq d krxvh exw kdyh uhdvrqv wr pryh, fdq eh
8                                                                                                         ECB Working Paper No 18 G April 2000 
vruwhg lqwr wkuhh jurxsv= 4, xqfrqvwudlqhg pryhuv> 5, frqvwudlqhg pryhuv> 6, frqvwudlqhg
qrq0pryhuv1 Idplolhv lq wkh uvw jurxs duh vx!flhqwo| zhdowk| wkdw qdqfldo frqvwudlqwv gr
qrw dhfw wkhlu ehkdylrxu1 Iru wkhp/ ghpdqg iru krxvhv lv d ghfuhdvlqj ixqfwlrq ri wkh sulfh1
Idplolhv lq wkh vhfrqg jurxs kdyh qrw hqrxjk zhdowk/ dqg idfh elqglqj qdqfldo frqvwudlqwv=
wkhlu qhw ghpdqg iru krxvlqj lv dq lqfuhdvlqj ixqfwlrq ri wkh sulfh/ vlqfh zlwk d kljkhu sulfh wkh|
fdq drug d kljkhu grzqsd|phqw iru d qhz krxvh1 Idplolhv lq wkh wklug jurxs duh vr zhdowk
frqvwudlqhg wkdw wkh| duh ehwwhu r vlwwlqj wljkw/ qhlwkhu ex|lqj qru vhoolqj1 Rqh nh| lpsolfdwlrq
ri wklv prgho lv wkdw/ vxemhfw wr fhuwdlq frqglwlrqv/ wkh lpsdfw ri ixqgdphqwdo glvwxuedqfhv rq
krxvh sulfhv fdq eh juhdwo| pdjqlhg uhodwlyh wr wkh ehqfkpdun fdvh ri qr qdqfldo frqvwudlqwv1
Plohv +4<<5/ 4<<8, ghyhorsv d qxpehu ri wkhruhwlfdo prghov lq zklfk wkh nh| hohphqw lv wkh
ghulydwlrq ri dq h{suhvvlrq iru wkh xvhu frvw ri krxvlqj1 Lq sduwlfxodu/ kh h{solflwo| prghov wkh
lpsdfw ri wkh uhvwulfwlrqv rq wkh dydlodelolw| ri ixqgv wr wkh krxvhkrogv/ lq wkh irup ri d orzhu
erxqg rq wkh dprxqw ri krxvlqj htxlw| wkdw lqglylgxdov pxvw rzq1 Klv pdlq uhvxow lv wkdw wkh
hhfw ri doorzlqj htxlw| zlwkgudzdo iurp wkh krxvlqj pdunhw xsrq vdylqj/ frqvxpswlrq dqg
krxvh sulfhv fdq eh erwk vxevwdqwldo dqg surorqjhg= lq sduwlfxodu/ kh vkrzv wkdw wkh hdvlqj ri
fuhglw frqglwlrqv zloo ohdg wr lqfuhdvh lq krxvh sulfhv dqg lq wkh vwrfn ri rxwvwdqglqj pruwjdjhv
lq wkh hfrqrp|1
Hduo| hpslulfdo vwxglhv ri wkh krxvlqj pdunhw kdyh irfxvhg rq vrph sduwlfxodu ihdwxuhv ri
wkh krxvh sulfhv/ orrnlqj lq sduwlfxodu dw wkh XV pdunhw9= Fdvh dqg Vkloohu +4<;</ 4<<3, vwxg|
wkhlu dxwrfruuhodwlrq surshuwlhv> Srwhued +4<<4, irfxvhv rq fkdqjhv lq wkh frqvwuxfwlrq frvwv/ lq
wkh uhdo diwhu0wd{ frvw ri krphrzqhuvkls/ dqg rq ghprjudsklf idfwruv dv srvvleoh ghwhuplqdqwv
ri vkliwv ri ghpdqg dqg vxsso| lq wkh krxvlqj pdunhw= e| xvlqj phgldq krxvh sulfhv rq 6< flwlhv
iurp 4<;3 wr 4<<3/ kh vkrzv wkdw vkliwv lq lqfrph dqg lq frqvwuxfwlrq frvwv kdyh lpsruwdqw
hhfwv rq uhdo krxvh sulfh fkdqjhv exw qgv olwwoh vxssruw iru wkh lpsruwdqfh ri ghprjudsklf
idfwruv1 Ehvlghv orrnlqj dw plfurhfrqrplf ghwhuplqdqwv ri krxvh sulfhv/ dqrwkhu ghedwhg lvvxh
kdv ehhq zkhwkhu krxvh sulfhv kdyh rqo| ehhq gulyhq rqo| e| ixqgdphqwdo ghpdqg dqg vxsso|
idfwruv ru li lw lv srvvleoh wr qg hylghqfh ri exeeohv lq wkh krxvlqj pdunhw1 D jrrg vxuyh| ri
wkhvh lvvxhv lv Fkr +4<<9,1
515 Krxvlqj pdunhwv/ prqhwdu| srolf| dqg wkh pdfurhfrqrp|
Wkh lghd wkdw dvvhw sulfhv pljkw sod| d uroh lq wkh wudqvplvvlrq phfkdqlvp dqg lq wkh pdfurh0
frqrp| lq jhqhudo lv qrw qhz lq hfrqrplfv/ dqg gdwhv edfn dw ohdvw wr Yheohq +4<37, dqg Ilvkhu
+4<66,1 Lq uhfhqw |hduv/ wkh lghd vhhpv wr kdyh ehfrph lqfuhdvlqjo| srsxodu1 Pdq| ri wkh vxuyh|
9 Pdq| krxvh sulfh htxdwlrqv/ prvwo| vhhq dv lqyhuwhg ghpdqg fxuyhv iru krxvlqj/ kdyh ehhq hvwlpdwhg lq wkh
sdvw iru wkh Xqlwhg Nlqjgrp wrr1 Vhh Pxhooedxhu dqg Pxusk| +4<<:, dqg uhihuhqfhv wkhuhlq1
ECB Working Paper No 18 G April 2000                                                                                                           9
sdshuv sxeolvkhg lq wkh Zlqwhu 4<<8 Mrxuqdo ri Hfrqrplf Shuvshfwlyhv v|psrvlxp rq wkh Prq0
hwdu| Wudqvplvvlrq Phfkdqlvp dqdo|vh/ gluhfwo| ru lqgluhfwo|/ wkh uroh ri wkh krxvlqj pdunhw lq
wkh wudqvplvvlrq phfkdqlvp:1
Wkh vr0fdoohg prqhwdulvw ylhz +Phow}hu/ 4<<8, frpprqo| hpskdvlvhv wzr ylhzv= wkhvh
lqyroyh Wrelq*v t wkhru| ri lqyhvwphqw dqg zhdowk hhfwv rq frqvxpswlrq1
Wkh odwwhu kdv
lwv urrwv lq Prgljoldql*v olih0f|foh prgho/ lq zklfk frqvxpswlrq lv ghwhuplqhg e| wkh olihwlph
uhvrxufhv ri frqvxphuv/ zklfk duh pdgh xs ri kxpdq fdslwdo/ uhdo dvvhwv dqg qdqfldo zhdowk1
Zkhq dvvhw sulfhv idoo/ vr gr olihwlph uhvrxufhv/ dqg frqvxpswlrq idoov1
Wkh Wrelq*v t ylhz vwduwv e| uhfrjqlvlqj wkdw wkh wudqvplvvlrq surfhvv ehjlqv dqg rshudwhv lq
wkh dvvhw pdunhw/ zkhuh frvwv ri lqirupdwlrq dqg wudqvdfwlrq duh orzhu wkdq wkh frvwv ri fkdqjlqj
surgxfwlrq ru dgmxvwlqj frqvxpswlrq ru lqyhvwphqw lq gxudeohv1 Li wkhuh lv xqfhuwdlqw| derxw
wkh prqhwdu| srolf| lqlwldo lpsxovh/ dvvhw sulfhv uhvsrqg pruh txlfno|1 Fkdqjhv lq uhodwlyh sulfhv
rq wkh dvvhw pdunhwv vsloo ryhu wr wkh rxwsxw pdunhwv> lq wkh fdvh ri dq h{sdqvlrqdu| prqhwdu|
srolf|/ wkh sulfh ri wkh dvvhw fdq eh deryh lwv uhsodfhphqw frvw/ dqg surgxfwlrq lqfuhdvhv1
Wkh fuhglw fkdqqho ylhz +Ehuqdqnh dqg Jhuwohu/ 4<<8,/ rq wkh rwkhu kdqg/ dvvxphv wkdw
fuhglw pdunhwv duh qrw iulfwlrqohvv/ ehfdxvh ri sureohp ri lqirupdwlrq/ hqirufhphqw dqg lqfhq0
wlyhv1 Ehfdxvh ri wklv/ fuhglw fdq eh pruh hdvlo| jlyhq wr djhqwv zlwk vrxqg qdqfldo srvlwlrqv/ ru
zkr fdq rhu froodwhudo dv d jxdudqwhh1 Dq lpsolfdwlrq ri wklv lv wkdw wkh ydoxh ri wkh froodwhudo
+iru lqvwdqfh/ krph htxlw| ydoxh, ghwhuplqhv djhqw*v delolw| wr eruurz dqg ohqg/ dqg lwv xfwx0
dwlrqv dhfw wkh djhqw*v ohyhudjh dqg khu delolw| wr frqvxph dqg surgxfh1 Lq wxuq/ wklv lpsolhv
wkdw surf|folfdo pryhphqwv lq wkh qdqfldo frqglwlrqv ri eruurzhuv kdyh uvw rughu hhfwv rq
djjuhjdwh rxwsxw dqg zhdowk/ dqg fdq pdjqli| lqyhvwphqw dqg rxwsxw xfwxdwlrqv uhodwlyh wr
d iulfwlrqohvv hfrqrp| +dv lq Nl|rwdnl dqg Prruh/ 4<<:/ dqg Ehuqdqnh/ Jhuwohu dqg Jlofkulvw/
4<<<,1
Wkhuh lv d orw ri hpslulfdo hylghqfh rq krxvlqj pdunhw xfwxdwlrqv dqg wkh pdfur0hfrqrp|=
pxfk ri lw lv pdlqo| ghvfulswlyh lq qdwxuh1 Hqjoxqg dqg Lrdqqlghv +4<<:, wdnh dq lqwhuqdwlrqdo
hpslulfdo shuvshfwlyh rq krxvlqj sulfhv lq d sdqho ri 48 RHFG frxqwulhv= wkhlu zrun/ zkloh
grfxphqwlqj wkh srvlwlyh lpsdfw ri JGS jurzwk dqg wkh qhjdwlyh lpsdfw ri lqfuhdvh lq lqwhuhvw
udwhv rq krxvh sulfhv/ grhv qrw surylgh hylghqfh rq wkh g|qdplfv wkdw krxvh sulfhv pljkw kdyh
iroorzlqj d vkrfn1
Rwkhu hylghqfh frphv iurp wzr ELV vwxglhv= lq wkhlu furvv0frxqwu| vwxg| rq wkh olqn ehwzhhq
uhdo krxvh sulfhv dqg krxvhkrog vdylqj/ Nhqqhg| dqg Dqghuvrq +4<<7, srlqw rxw wkh gl!fxow| lq
lghqwli|lqj wkh idfwruv jryhuqlqj krxvh sulfh xfwxdwlrqv1 Zkloh wkh| fdqqrw uxoh rxw wkh srvvl0
: H{dpsohv duh Ehuqdqnh dqg Jhuwohu +4<<8, dqg Phow}hu +4<<8,> Wd|oru +4<<8/ sdj14:, glvfxvvhv krz pruwjdjh
udwhv fdq eh dhfwhg e| fkdqjhv lq wkh vkruw whup lqwhuhvw udwhv1
10                                                                                                    ECB Working Paper No 18 G April 2000
elolw| ri vshfxodwlrq lq wkh krxvlqj pdunhwv dfurvv frxqwulhv/ wkh| vxjjhvw wkdw prqhwdu| srolf|
vwdqfh/ vfdo wuhdwphqw ri krxvlqj dqg qdqfldo olehudolvdwlrq pljkw sod| d uroh lq gulylqj sulfh
vzlqjv1 Erulr/ Nhqqhg| dqg Surzvh*v +4<<7, xqlyduldwh uhjuhvvlrqv ri d uhdo dvvhw sulfh lqgh{
rq fuhglw dqg rwkhu yduldeohv vxjjhvw wkdw wkh fuhglw sod|v dqg lpsruwdqw uroh lq gulylqj dvvhw
sulfhv/ dqg vxjjhvw iru wkh 4<;3v d wudqvplvvlrq phfkdqlvp jrlqj iurp qdqfldo olehudolvdwlrq
wr lqfuhdvh lq fuhglw wr lqfuhdvh lq dvvhw sulfhv lq Vzhghq/ Ilqodqg dqg Qruzd|1
Phow}hu +4<<8, frpsduhv udwhv ri sulfh fkdqjh iru qhz rqh0idplo| krxvhv dqg wkh X1V1 JGS
gh dwru/ dqg vkrzv wkdw shdnv lq wkh udwh ri fkdqjh ri krxvlqj sulfhv suhfhgh hdfk shdn lq wkh
gh dwru e| derxw wzr |hduv1 Kh dovr grfxphqwv vlplodu sdwwhuqv iru XN dqg Vzhghq1 Erpkr
+4<<7, h{sodlqv txduwhuo| xfwxdwlrqv lq JGS jurzwk lq X1V1/ Mdsdq dqg Jhupdq| iurp 4<:5
wr 4<<41 Kh vkrzv wkdw jurzwk ghshqgv srvlwlyho| rq odjjhg uhdo krxvh sulfhv/ d qglqj wkdw
fdq eh frqvlvwhqw zlwk d prqhwdulvw ylhz ri wkh wudqvplvvlrq phfkdqlvp1 Kljjlqv dqg Rvohu
+4<<:, xvh furvv0frxqwu| gdwd iru RHFG frxqwulhv iurp 4<;7 wr 4<<6= wkh| dujxh wkdw krxvlqj
dqg htxlw| sulfhv zhuh lq dwhg e| vshfxodwlyh sulfh exeeohv lq pdq| frxqwulhv/ dqg wkdw dvvhw
sulfh ghfolqhv ri wkh hduo| 4<<3v uhsuhvhqwhg d ckdqjryhu* iurp hduolhu exeeohv1 Wkh| edvh wklv
frqfoxvlrq rq wkh revhuydwlrq wkdw frxqwulhv zkrvh dvvhw sulfhv urvh ixuwkhvw lq wkh odwh 4<;3v
irxqg wkhlu dvvhw sulfhv idoolqj wkh ixuwkhvw odwhu rq/ d uhvxow wkdw krogv hyhq dffrxqwlqj iru wkh
lq xhqfh ri hfrqrplf ixqgdphqwdov1
6 Hfrqrphwulf phwkrgrorj|= Yhfwru Dxwruhjuhvvlrqv dqg Frpprq Wuhqgv
614 Zk| YDUvB
D vxusulvlqj idfw ri doprvw doo wkh hpslulfdo vwxglhv rq krxvh sulfh xfwxdwlrqv dqg wkh pdfurh0
frqrp| lv wkdw/ zkloh wkh| uhfrjqlvh wkh lpsruwdqfh ri krxvh sulfhv lq wkh wudqvplvvlrq phfk0
dqlvp/ wkh| gr qrw pdnh xvh ri rqh ri wkh prvw frqyhqlhqw dqg xvhg wrrov wr vxppdulvh wkh
g|qdplf uhodwlrqvklsv ehwzhhq wkh yduldeohv1 Lqvwhdg/ iroorzlqj vwdqgdug sudfwlfh vlqfh Vlpv*
+4<;3, vhplqdo frqwulexwlrq/ wklv sdshu xvhv yhfwru dxwruhjuhvvlrqv wr ghvfuleh pdfurhfrqrplf
g|qdplfv lqyroylqj frqvxphu dqg krxvh sulfhv/ rxwsxw/ prqh| dqg lqwhuhvw udwhv1
Ri frxuvh/ dsso|lqj wklv phwkrgrorj| wr krxvh sulfh g|qdplfv lv qrw zlwkrxw lwv vnhswlfv;1
Lq d uhfhqw sdshu rq wkh Krxvlqj Pdunhw dqg wkh HPX/ Pdfohqqdq/ Pxhooedxhu dqg Vwhskhqv
+4<<;, +PPV/ khqfhiruwk, dujxh wkdw wkh lqvwlwxwlrqdo glhuhqfhv h{lvwlqj lq Hxursh/ lq sdu0
wlfxodu lq krxvlqj dqg fuhglw frqglwlrqv/ qhfhvvdulo| lpso| odujh glhuhqfhv lq wkh prqhwdu|
wudqvplvvlrq phfkdqlvp dfurvv Hxurshdq frxqwulhv1 Wkh| dovr vwdwh wkdw YDU vwxglhv ri wkh
wudqvplvvlrq phfkdqlvp duh vxemhfw wr d qxpehu ri vhulrxv fulwlflvpv/ wkh uvw ehlqj ri plv0
; Shukdsv wklv lv wkh uhdvrq zk| qrerg| kdv uxq YDUv zlwk krxvh sulfhv diwhu doo1
ECB Working Paper No 18 G April 2000                                                                                                     11
vshflfdwlrq ehfdxvh ri wkh rplvvlrq ri lpsruwdqw yduldeohv/ vxfk dv dvvhw sulfhv1 Ixuwkhupruh/
wkh| dujxh wkdw d YDU frxog rqo| eh d srru dssur{lpdwlrq wr wkh g|qdplf uhvsrqvhv ri dv0
vhw sulfhv wr vwuxfwxudo vkrfnv1 Lw vhhpv wkdw wkh dssolhg hfrqrphwulfldq lv ohiw zlwk qr krsh=
hlwkhu lqfoxgh krxvh sulfhv/ dqg ehlqj xqdeoh wr ixoo| fdswxuh wkhlu g|qdplfv/ ru wr h{foxgh
wkhp/ xqghuvshfli|lqj wkh prgho1 E| lqfoxglqj krxvh sulfhv lq dq rwkhuzlvh uhodwlyho| vwdqgdug
vshflfdwlrq/ wklv sdshu krshv wr eh lppxqh dw ohdvw lq sduw wr wkh vhfrqg fulwlflvp1
Lq dsso|lqj wkh YDU phwkrgrorj| wr krxvh sulfhv/ vrph zduqlqjv duh wkhuhiruh lq rughu1
4, Dv Frfkudqh +4<<7, srlqwv rxw/ dq| YDU phfkdqlfdoo| dffrxqwv iru 433( ri wkh yduldqfh ri
wkh yduldeohv e| xqiruhfdvwdeoh pryhphqwv lq wkh hqgrjhqrxv yduldeohv1 Vhdufklqj iru h{rjhqrxv
glvwxuedqfhv lv d zd| wr orrn iru srolf|/ ru whfkqrorj|/ ru eholhiv0lqgxfhg fkdqjhv lq wkdw yduldeoh1
Lw grhv qrw vd| d orw derxw shuihfwo| dqwlflsdwhg vkrfnv ru v|vwhpdwlf srolflhv1 Qru fdq lw hdvlo|
glvwlqjxlvk ehwzhhq ixqgdphqwdo yhuvxv qrq0ixqgdphqwdo ghwhuplqdqwv ri krxvh sulfhv/ vxfk dv
vshfxodwlyh exeeohv1 Diwhu doo/ dqg ghvslwh wkh frpprqo| khog ylhz wkdw lq wkh odwh 4<;3v dvvhw
pdunhwv lq pdq| lqgxvwuldolvhg frxqwulhv zhuh khog doriw e| exeeohv</ rqh ri wkh ohvvrqv wr frph
iurp uhvhdufk lv wkdw rqh fdq qhyhu suryh zkhwkhu d jlyhq errp0exvw f|foh lq krxvh sulfhv zdv
wuxo| d exeeoh +Kdplowrq dqg Zklwhpdq/ 4<;8,1 Wr wkh h{whqw wkdw hyhq wkh prvw h{wuhph sulfh
ulvh pljkw kdyh ehhq gulyhq e| vrph xqrevhuyhg ixqgdphqwdo idfwru/ wkh YDU dssurdfk ri wklv
sdshu zloo wu| wr dqdo|vh zklfk idfwruv frxog eh wkh vrxufh ri krxvh sulfh xfwxdwlrqv1
5, Olqhdulw| lv dovr d fuxfldo lvvxh1 Krxvh sulfhv dqg rwkhu yduldeohv fdq uhdfw glhuhqwo|
wr vkrfnv htxdo lq pdjqlwxgh exw ri rssrvlwh vljq1 PPV +4<<;,/ iru lqvwdqfh/ dujxh wkdw lq
vshfxodwlyh pdunhwv/ vxfk dv wkh krxvlqj pdunhw/ wkh g|qdplfv ru wkh uhvsrqvh ri krxvh sulfhv
wr lqwhuhvw udwhv duh qrq0olqhdu dqg qrq0frqvwdqw ryhu wlph1
6, Wkh lvvxh ri wkh sursdjdwlrq phfkdqlvp lv fuxfldo wrr1 Wkh vdph lpsxovh jhqhudwhv glhu0
hqw uhvsrqvhv ehfdxvh ri dq xqghuo|lqj glhuhqw sursdjdwlrq phfkdqlvp1 Iurp wkh pdjqlwxgh
dqg wkh vkdsh ri wkh uhvsrqvhv/ ru frqwuroolqj iru rwkhu yduldeohv wkdw pljkw sod| d uroh lq wkh
wudqvplvvlrq ri d vkrfn/ lw lv srvvleoh wr lqihu vrphwklqj rq zkdw kdsshqv iroorzlqj d vkrfn/ dqg
zk|1 Krzhyhu/ lq pdq| fdvhv pruh wkdq rqh wudqvplvvlrq fkdqqho lv frqvlvwhqw zlwk wkh vdph
uhvsrqvh1
615 Wkh hpslulfdo phwkrgrorj|
Wklv vhfwlrq ghvfulehv krz wkh orqj0uxq sursrvlwlrqv ri hfrqrplf wkhru| fdq eh xvhg wr lghqwli|
wkh pdlq vrxufhv ri hfrqrplf xfwxdwlrqv1 Lq wkdw wkh dssurdfk ri Eodqfkdug dqg Txdk +4<;<,/
NSVZ +4<<4,/ dqg Zduqh +4<<6, lv iroorzhg1 D pruh ghwdlohg ghvfulswlrq ri wkh phwkrgrorj|
< Vhh wkh glvfxvvlrq lq Kljjlqv dqg Rvohu +4<<:/ sdjh 448, dqg uhihuhqfhv wkhuhlq1
12                                                                                                  ECB Working Paper No 18  G  April 2000  
lv lq wkh Dsshqgl{ D1
Dv lw lv zhoo nqrzq/ zkhq d jurxs ri yduldeohv lv irxqg wr eh qrq0vwdwlrqdu| exw frlqwhjudwhg/
d xvhixo vshflfdwlrq iru wkhlu g|qdplf lqwhudfwlrq lv d yhfwru0huuru0fruuhfwlrq +YHFP, prgho1
D YHFP prgho/ lq sduwlfxodu/ sodfhv qrq0olqhdu uhgxfhg0udqn uhvwulfwlrqv rq wkh pdwul{ ri
orqj0uxq lpsdfwv iurp d YDU1 NSVZ +4<<4,/ lq sduwlfxodu/ sursrvh d glvwlqfwlrq ehwzhhq
vwuxfwxudo vkrfnv zlwk shupdqhqw hhfwv rq wkh ohyho ri wkh yduldeohv +vd|/ d srvlwlyh vxsso|
vkrfn/ udlvlqj rxwsxw lq wkh orqj0uxq, iurp wkrvh zlwk rqo| whpsrudu| hhfwv +vd|/ d ghpdqg
vkrfn wkdw fdq eh wkrxjkw wr kdyh }hur orqj0uxq hhfw rq rxwsxw dqg rwkhu uhdo yduldeohv,1
Wkh shupdqhqw vkrfnv duh wkh vrxufhv ri wkh vr0fdoohg frpprq vwrfkdvwlf wuhqgv dfurvv wkh
vhulhv/ dqg wkh qxpehu ri wkhvh vkrfnv lv htxdo wr wkh qxpehu ri yduldeohv lq wkh v|vwhp ohvv wkh
qxpehu ri frlqwhjudwlqj uhodwlrqvklsv ehwzhhq wkhp1 Wkh +uhpdlqlqj, wudqvlwru| lqqrydwlrqv
htxdo wkh qxpehu ri frlqwhjudwlqj uhodwlrqvklsv +lqwxlwlyho|/ d frlqwhjudwlqj yhfwru lghqwlhv d
olqhdu frpelqdwlrq ri wkh yduldeohv wkdw lv vwdwlrqdu| wkxv holplqdwlqj wkh wuhqg/ vr wkdw vkrfnv
wr lw gr qrw holplqdwh wkh vwhdg| vwdwh lq vxfk d v|vwhp,1
L vshfli| d yh glphqvlrqdo YDU zlwk [| @
k
|
ps
ks
l
l
/ zkhuh [| lv d yhfwru
frpsulvlqj uhdo lqfrph +||,/ d phdvxuh ri uhdo prqh| edodqfhv +ps|,/ d uhdo krxvh sulfh lqgh{ 0
l1h1/ d qrplqdo krxvh sulfh lqgh{ gh dwhg e| wkh frqvxphu sulfh ohyho 0 +ks|,/ d vkruw0whup qrplqdo
lqwhuhvw udwh +l|,/ dqg dqqxdolvhg txduwhuo| +frqvxphu sulfh, lq dwlrq +|,1 Uhdo yduldeohv duh
vshflhg lq qdwxudo orjdulwkpv/ lqwhuhvw udwh dqg frqvxphu sulfh lq dwlrq lq shufhqwdjh whupv1
Vhyhudo hpslulfdo txhvwlrqv fdq eh dqvzhuhg iurp wklv uhsuhvhqwdwlrq1 Lv wkhuh hylghqfh ri d
orqj0uxq prqh| ghpdqg vfkhgxohB Lv wkh uhdo lqwhuhvw udwh vwdwlrqdu|B Krz gr uhdo krxvh sulfhv
ehkdyh lq wkh orqj0uxq dqg zkdw lv wkhlu uhodwlrqvkls zlwk uhdo rxwsxwB Krz gr uhdo dqg qrplqdo
yduldeohv lqwhudfw iroorzlqj d glvwxuedqfhB Krz fdq zh glvhqwdqjoh lqqrydwlrqv zlwk shupdqhqw
hhfwv rq wkh yduldeohv iurp wkrvh zlwk rqo| wudqvlwru| hhfwvB Zkdw dffrxqwv iru prvw ri wkh
revhuyhg yrodwlolw| lq uhdo krxvh sulfhv wkdw kdv fkdudfwhulvhg pdq| dgydqfhg hfrqrplhv ryhu
wkh odvw ghfdghvB
616 K|srwkhvhv derxw frlqwhjudwlrq
Zlwk 8 yduldeohv lq wkh gdwdvhw/ krz pdq| frpprq vwrfkdvwlf wuhqgv fdq zh h{shfw wr qgB
Prqh|/ Rxwsxw dqg Lqwhuhvw Udwhv= Wkh ulvh lq sulfh ohyhov lq prvw frxqwulhv gxulqj
wkh odvw ghfdghv vxjjhvwv wkh srvvlelolw| ri d vwrfkdvwlf wuhqg dvvrfldwhg zlwk wkh ghvljq ri wkh
prqhwdu| srolf|= lq rwkhu zrugv/ dv vxjjhvwhg e| Jdol +4<<5,/ wkh fhqwudo edqn*v ghvluh wr dyrlg
rxwsxw xfwxdwlrqv pd| uhvxow lq qrplqdo lqvwdelolw|/ lq wkh vhqvh ri ohdglqj wr d frpprq wuhqg
ohdglqj qrplqdo udwhv/ prqh| edodqfhv dqg rxwsxw1 Dowhuqdwlyho|/ wkh uhodwlrq ehwzhhq wkhvh
ECB Working Paper No 18  G April 2000                                                                                                       13
yduldeohv fdq eh lqwhusuhwhg/ dv grqh iru lqvwdqfh lq Frhqhq dqg Yhjd +4<<<, dqg Furzghu/
Krpdq dqg Udvfkh +4<<<,/ dv d wudglwlrqdo prqh| ghpdqg ixqfwlrq olqnlqj uhdo edodqfhv wr
d vfdoh yduldeoh dqg d phdvxuh ri wkh rssruwxqlw| frvw ri pdlqwdlqlqj oltxlglw|1 Wkdw wklv olqn
lv d prqh| ghpdqg ixqfwlrq pxvw eh lqwhusuhwhg zlwk fdxwlrq wkrxjk/ iru dw ohdvw 8 uhdvrqv43=
4, wkhuh frxog eh pdq| frlqwhjudwlqj yhfwruv dw lvvxh lq d vlplodu v|vwhp= prqh| ghpdqg
+ehwzhhq ps/ | dqg l, lv rqh/ exw djjuhjdwh ghpdqg dv zhoo/ iru lqvwdqfh +ehwzhhq | dqg l,>
5, d phdvxuh ri vkruw0whup lqwhuhvw udwhv fdq zhoo uhsuhvhqw rzq udwkhu wkdq rxwvlgh udwh rq
prqh|> 6, dq| phdvxuh ri prqh| lv dq djjuhjdwh ryhu frpsrqhqwv zlwk glhuhqw fkdudfwhulvwlfv>
7, ghqlwlrqdo dqg vwuxfwxudo euhdnv fdqqrw eh ljqruhg> 8, wkh iuhtxhqf| ri revhuydwlrq pd|
dhfw erwk h{rjhqhlw| dqg frlqwhjudwlrq/ dv glvfxvvhg e| Khqgu| +4<<8,1
Lqwhuhvw Udwhv dqg Lqiodwlrq= Wkhuh duh wkhruhwlfdo uhdvrqv wr eholhyh wkdw uhdo lqwhuhvw
udwhv duh vwdwlrqdu|1 Lq rwkhu zrugv/ wkhuh lv d olqn ehwzhhq wkh wzr qrplqdo yduldeohv wkdw
fruuhvsrqgv wr d prglhg Ilvkhu htxdwlrq/ l1h1 l| @  . | . %|441
Rxwsxw dqg Uhdo Krxvh Sulfhv= Lv wkhuh d orqj uxq uhodwlrqvkls ehwzhhq krxvh sulfhv
dqg frqvxphu sulfhvB Vkrxog zh h{shfw uhdo krxvh sulfhv wr eh frqvwdqw ryhu wlph ru qrwB D
srvvleoh dqvzhu/ zklfk lv vxjjhvwhg e| Srwhued +4<;7,/ jrhv dv iroorzv= li wkh orqj0uxq krxvlqj
vxsso| fxuyh dqg wkh vxsso| fxuyh iru doo wkh rwkhu jrrgv zhuh shuihfwo| hodvwlf/ wkh vwhdg| vwdwh
sulfh ri vwuxfwxuhv zrxog ghshqg hqwluho| rq frqvwuxfwlrq frvwv/ zklfk duh suredeo| lqghshqghqw
ri wkh ohyho ri frqvwuxfwlrq1 Krzhyhu/ surylghg wkdw dq| idfwru ghwhuplqlqj uhdo hvwdwh vxsso|/
vxfk dv odqg/ oxpehu ru frqvwuxfwlrq zrunhuv/ lv dydlodeoh lq {hg vxsso| 0 wkxv dfwlqj dv d
olplwlqj idfwru 0/ rqh fdq h{shfw wkdw wkh surgxfwlrq srvvlelolw| iurqwlhu ehwzhhq krxvhv dqg
rwkhu jrrgv45 lv qrw dw1 Wkdw lpsolhv d srvvleoh xszdug wuhqg lq uhdo krxvh sulfhv ryhu wkh
orqj0uxq461 \hw rqh fdq uhdvrqdeo| h{shfw uhdo krxvh sulfhv wr eh frlqwhjudwhg zlwk JGS/ vlqfh
wkh JGS fdq jlyh d phdvxuh ri krz pxfk wkh surgxfwlrq srvvlelolwlhv iurqwlhu lv vkliwlqj rxw
ryhu wlph471 Lq d vhqvh/ wklv fdqglgdwh frlqwhjudwlqj yhfwru/ phdvxulqj hodvwlflw| ri uhdo krxvh
sulfhv wr rxwsxw/ fdq eh wkrxjkw ri d orqj0uxq vxsso| fxuyh iru wkh krxvlqj vwrfn/ surylghg wkdw
qhz lqyhvwphqw lq vwrfn lv d frqvwdqw iudfwlrq ri JGS dqg wkdw wkh vxsso| fxuyh iru krxvlqj
43 Vhh Hulfvvrq +4<<;, iru d wkrurxjk glvfxvvlrq ri wkhvh srlqwv1
44 Wkh zrug prglhg lv xvhg ehfdxvh wkh Ilvfkhu uhodwlrqvkls vkrxog eh pruh surshuo| prghoohg dv d orqj
uxq uhodwlrqvkls ehwzhhq qrplqdo lqwhuhvw udwhv dqg h{shfwhg lq dwlrq/ dv grqh lq Furzghu hw do1 +4<<<,1 Xvlqj
lq dwlrq lq shulrg | n  dv d sur{| iru lq dwlrq h{shfwdwlrqv dqg prghoolqj wkh v|vwhp zlwk Z|n lqvwhdg ri Z|
|lhoghg doprvw xqfkdqjhg uhvxowv1
45 D uhsuhvhqwdwlyh vdpsoh ri rwkhu jrrgv hqwhuv wkh frqvxphu sulfh lqgh{/ ri frxuvh1
46 Iru wkh Xqlwhg Nlqjgrp/ Plohv +4<<8/ sdjh 73, grfxphqwv dq xszdug wuhqg lq uhdo krxvh sulfhv ryhu wkh
odvw fhqwxu|1 Dowkrxjk lw lv frqfhlydeoh wkdw dw ohdvw sduw ri wkh dssduhqw ulvh lq wkh uhdo sulfh ri krxvhv lv gxh wr
krph lpsuryhphqwv/ d txdolw| dgmxvwhg lqgh{ ri uhdo krxvh sulfhv zrxog suredeo| vwloo eh jurzlqj ryhu wlph1 Iru
furvv0frxqwu| hylghqfh ryhu wkh odvw ghfdghv rqo|/ vhh Fxwohu +4<<8,1
47 Qrwh wkdw L dp qrw lqyhvwljdwlqj d uhodwhg exw glhuhqw lvvxh/ vxfk dv wkh srvvlelolw| wkdw krxvlqj zhdowk lv
d frqvwdqw iudfwlrq ri lqfrph ryhu wlph1 Wklv lqirupdwlrq ghqhv d frlqwhjudwlqj yhfwru/ exw fdqqrw eh lqfoxghg
lq rxu dqdo|vlv vlqfh rxu 5 grhv qrw lqfoxgh dq| phdvxuh ri wkh krxvlqj vwrfn1
14                                                                                                  ECB Working Paper No 18 G April 2000  
vwuxfwxuhv grhv qrw vkliw ryhu wlph481
L orrn wkhuhiruh iru wkh iroorzlqj uhsuhvhqwdwlrqv=
|
ps
ks
l

@
k
e+
4
3
e
3
l
2
@
k

3
4
3
l

@
k
3
4
4
l
wkh uvw lghqwli|lqj d orqj0uxq prqh| ghpdqg vfkhgxoh/ vd|/ ps| @ e+||  el|/ wkh vhfrqg
olqnlqj uhdo krxvh sulfhv dqg rxwsxw/ l1h1 ks| @ ||> dqg wkh odvw rqh lpso|lqj vwdwlrqdu| +h{
dqwh, uhdo lqwhuhvw udwh1 Dowrjhwkhu/ diwhu wkh qrupdolvdwlrq rq ps> ks dqg / wklv vshflfdwlrq
lpsrvhv u +u  4, @ 9 qrq0whvwdeoh }hur uhvwulfwlrqv1 Wkh wkuhh uhpdlqlqj uhvwulfwlrqv +wzr ehlqj
}hur uhvwulfwlrqv dqg rqh lpsrvlqj d 4 frh!flhqw rq wkh lqwhuhvw udwh lq ,/ jlyhq wkh rwkhuv/
duh lqvwhdg whvwdeoh491
617 Lghqwli|lqj vwuxfwxudo vkrfnv
Wkh sdudphwhuv ri wkh frlqwhjudwlqj yhfwruv fdq eh xvhg wr uhvwulfw wkh orqj0uxq pxowlsolhuv ri
wkh shupdqhqw vkrfnv +iru ghwdlov/ vhh Dsshqgl{ D,1
Wklv ghulyhv iurp wkh idfw wkdw lqirupdwlrq derxw wkh frlqwhjudwlqj vsdfh doorzv wr irupxodwh
d YDU lq wkh irup ri dq huuru fruuhfwlrq prgho1 Vwduwlqj iurp wkh uhgxfhg irup ri d YDU lq
ohyhov/ zkhuh [ lv wkh froxpq yhfwru ri hqgrjhqrxv yduldeohv/ ] lv d yhfwru ri ghwhuplqlvwlf
frpsrqhqwv/ n lv wkh odj rughu dqg H%% @  
[| @ D[|3 . === . D&[|3& . ]| . %|
wkh YHFP uhsuhvhqwdwlrq ri wkh YDU/ zkhuh/ zlwk xvxdo qrwdwlrq/  uhsuhvhqwv wkh uvw
glhuhqfh rshudwru/ lv=
[| @ [|3  +D2 . === . D&, [|3  ===  D&[|3&n . ]| . %|
dqg wkh prylqj dyhudjh uhsuhvhqwdwlrq fdq eh fdvw dv=
[| @ F+O,%|
48 Qhhgohvv wr vd|/ dq| hvwlpdwhg uhodwlrqvkls zloo kdyh wr eh lqwhusuhwhg zlwk fdxwlrq/ dv wkhuh duh qrw orqj
wlph vhulhv rq krxvh sulfhv iru pdq| ri wkh frxqwulhv wkdw wklv vwxg| dqdo|vhv1
49 Mrkdqvhq +4<<4, vkrzv wkdw wkh dv|pswrwlf glvwulexwlrq ri wkh pd{lpxp olnholkrrg hvwlpdwhv iru q lv d pl{hg
Jdxvvldq glvwulexwlrq1 Wkdw lpsolhv wkdw wkh olnholkrrg udwlr whvw iru jlyhq k|srwkhvlv derxw uhvwulfwlrqv rq q lv/
iru jlyhq udqn/ dv|pswrwlfdoo| glvwulexwhg dv d 21
ECB Working Paper No 18 G April 2000                                                                                                       15
Shupdqhqw Vkrfnv= Lghqwlfdwlrq ri wkh shupdqhqw vkrfnv fdq wkhq eh dfklhyhg e| lpsrvlqj
mxvw hqrxjk uhvwulfwlrqv vr wkdw wkh vkrfnv dqg wkhlu orqj0uxq hhfwv pd| eh jlyhq dq hfrqrplf
lqwhusuhwdwlrq1 Hqjoh dqg Judqjhu +4<;:, kdyh vkrzq wkdw wkh froxpqv ri F +4, lq wkh uhvwulfwhg
YDU deryh duh ruwkrjrqdo wr wkh frlqwhjudwlqj yhfwruv/ l1h1
F +4, @ 31 Lq wklv yhlq/ wkh
lghqwlfdwlrq vwudwhj| lpsrvhv wkh iroorzlqj frqvwudlqwv rq wkh 8  8 pdwul{ ri wkh orqj0uxq
pxowlsolhuv F+4,1 Wklv pdwul{ lv sduwlwlrqhg lq= F+4, @ ^S 3` vr wkdw wkh pdwul{ S lv d 8  5
pdwul{ zkrvh froxpqv uhsuhvhqw wkh orqj0uxq uhvsrqvhv ri wkh yduldeohv wr shupdqhqw vkrfnv/
zkhuhdv wkh orqj0uxq uhvsrqvhv wr wkh whpsrudu| vkrfnv duh dvvxphg wr eh }hur1 Wkh 8  5
pdwul{ S jlylqj wkh orqj0uxq pxowlsolhuv ri wkh shupdqhqw vkrfnv pxvw eh vshflhg lq d zd|
vxfk wkdw lwv froxpqv duh ruwkrjrqdo wr wkh pdwul{ ri frlqwhjudwlqj uhodwlrqv1
Zlwk wkh yduldeohv rughuhg dv
k
|
ps
ks
l
l
/ L uhvwulfw wkh +4> 5, hohphqw ri wkh orqj0
uxq lpsdfw pdwul{ S wr eh }hur/ vr wkdw rqh ri wkh wzr shupdqhqw vkrfnv fdq eh suhfoxghg iurp
kdylqj d orqj0uxq hhfw rq wkh ohyho ri rxwsxw |4:1 Dffruglqjo|/ L doorz wkh rwkhu vkrfn wr dhfw
| lq wkh orqj uxq= wklv vkrfn lv wkhuhiruh wkh rqo| vrxufh ri xqlw urrw ehkdylrxu lq wkh JGS/ dqg
fdq eh wkrxjkw ri dv d vxsso| vkrfn1
Lq ghwdlo/ wkh S pdwul{ ri frpprq wuhqgv zloo eh=
S @ hS @
5
99999999997
4
3
e+
e
3
4
3
4
6
::::::::::8
5
7 4
3

4
6
8 #
5
99999999997
orqj uxq hhfw ri vkrfn rq |
orqj uxq hhfw ri vkrfn rq ps
orqj uxq hhfw ri vkrfn rq ks
orqj uxq hhfw ri vkrfn rq l
orqj uxq hhfw ri vkrfn rq 
6
::::::::::8
Iru dq| ydoxh ri wkh sdudphwhu  +wr eh hvwlpdwhg,/ wkh qrplqdo vkrfn +vhfrqg froxpq,
ohdyhv rxwsxw dqg uhodwlyh sulfhv xqfkdqjhg/ |lhoglqj d orzhu +kljkhu, ohyho ri uhdo edodqfhv
dqg kljkhu +orzhu, lq dwlrq dqg lqwhuhvw udwhv lq wkh orqj uxq4;1 Rqh srvvleoh lqwhusuhwdwlrq ri
wklv vkrfn/ iroorzlqj Frhqhq dqg Yhjd +4<<<,/ fdq eh wkdw ri d fkdqjh lq wkh prqhwdu| srolf|
remhfwlyh ri wkh prqhwdu| dxwkrulw|= lq wkh Hxurshdq h{shulhqfh/ lw frxog fdswxuh d srvvleo|
suhdqqrxqfhg frpplwphqw wr d glhuhqw lq dwlrq wdujhw/ exw dovr/ pruh lq jhqhudo/ lw pljkw
vwdqg iru d shupdqhqw qrplqdo vkrfn1
Wkh vxsso| vkrfn +uvw froxpq, lqfuhdvhv rxwsxw/ uhdo edodqfhv dqg uhdo krxvh sulfhv lq wkh
orqj0uxq/ zlwk zhljkwv glfwdwhg e| wkh hvwlpdwhg frlqwhjudwlqj yhfwruv1 Vr orqj dv wkh hvwlpdwh
4: Wklv surfhgxuh pljkw dsshdu d elw dg krf/ exw fkrrvlqj  lq d zd| wkdw dvvrfldwhv hdfk vkrfn zlwk d
idploldu hfrqrplf phfkdqlvp lv qrw d edg lghd/ hvshfldoo| zkhq/ dv zlwk wklv surfhgxuh/ vwurqj eholhiv derxw wkh
hhfwv ri doo vkrfnv rq hdfk yduldeohv h{fhhg wkh plqlpxp uhtxluhphqwv iru lghqwlfdwlrq1 Vhh/ iru d glvfxvvlrq/
Ilvfkhu hw do1 +4<<8,1
4; Rssrvlwh vljqv rq uhdo edodqfhv dqg rq qrplqdo udwhv rqo| rewdlq li wkh hvwlpdwhg frlqwhjudwlqj yhfwru
ehwzhhq prqh|/ rxwsxw dqg lqwhuhvw udwhv |lhogv frh!flhqwv ri wkh vdph vljq rq 6R dqg o1
16                                                                                                      ECB Working Paper No 18 G April 2000
ri  lv qrw gldjrqdo/ wklv vkrfn fdq dovr fkdqjh lq dwlrq dqg qrplqdo udwhv +e| wkh vdph dprxqw,
lq wkh orqj uxq1
Wudqvlwru| Vkrfnv= Wudqvlwru| vkrfnv/ zklfk duh dvvxphg wr eh ruwkrjrqdo wr wkh shu0
pdqhqw vkrfnv dqg wr hdfk rwkhu/ zloo kdyh qr orqj0uxq hhfw rq dq| ri wkh yduldeohv1 Iroorzlqj
Phoodqghu/ Yuhglq dqg Zduqh +4<<5,/ wkh| fdq eh jlyhq dq hfrqrplf lqwhusuhwdwlrq dorqj wkh
olqhv ri wkh wudglwlrqdo YDU phwkrgrorj| wkdw lghqwlhv vkrfnv lq d uhfxuvlyh idvklrq1 L lghqwli|
wkuhh vhsdudwh/ wudglwlrqdo vrxufhv ri vkruw0uxq xfwxdwlrqv= d prqhwdu| srolf| vkrfn kdv qr lp0
phgldwh hhfw rq rxwsxw dqg FSL lq dwlrq/ exw fdq frqwhpsrudqhrxvo| dhfw uhdo edodqfhv +e|
gulylqj grzq qrplqdo prqh| vxsso|,/ lqwhuhvw udwhv dqg uhdo krxvh sulfhv +iru lqvwdqfh ehfdxvh
krxvh sulfhv/ dv dvvhw sulfhv/ uhdfw rq wkh qhzv4<,1
Xqolnh wkh prqhwdu| rqh/ d ghpdqg vkrfn kdv }hur lpsdfw hhfw rq FSL lq dwlrq/ exw
srwhqwldoo| dhfwv frqwhpsrudqhrxv JGS/ e| dhfwlqj lwv vshqglqj frpsrqhqwv +vhh Jdol/ 4<<5/
iru d uhodwhg srlqw,/ dv zhoo dv krxvh sulfhv/ uhdo prqh| edodqfhv/ dqg lqwhuhvw udwhv1
Wklv
glvwxuedqfh frxog uhsuhvhqw d vkrfn wkdw kdv lwv urrwv lq hslvrghv frqfhuqlqj wkh krxvlqj pdunhw/
vxfk dv whpsrudu| wd{ dgydqwdjhv wr krxvlqj lqyhvwphqw ru d vxgghq lqfuhdvh lq ghpdqg ixhoohg
e| vhoi0ixooolqj h{shfwdwlrqv ri dssuhfldwlrq lq krxvh sulfhv1
Wkh wklug dqg odvw vkrfn wudqvlwru| vkrfn +wkdw fdq frqwhpsrudqhrxvo| dhfw doo wkh ydul0
deohv, pljkw eh/ dv lq Furzghu/ Krpdq dqg Udvfkh +4<<<,/ d wudqvlwru| lq dwlrq vkrfn/ l1h1 d
whpsrudu| xszdug vkliw lq wkh djjuhjdwh vxsso| vfkhgxoh ri d edvlf DG2DV prgho= lqghhg/ dv zh
zloo vhh/ wkh lpsxovh uhvsrqvhv duh lq prvw ri wkh frxqwulhv frqvlvwhqw zlwk wkh uhvsrqvhv iurp dq
djjuhjdwh vxsso|2djjuhjdwh ghpdqg fxuyh prgho/ zlwk qr vkliw lq wkh djjuhjdwh ghpdqg fxuyh/
qr fkdqjh lq lq dwlrq h{shfwdwlrqv/ dqg qr vkliw lq wkh orqj0uxq djjuhjdwh vxsso| fxuyh531
7 Surshuwlhv ri wkh gdwd
714 Vrxufhv ri gdwd
Wkh gdwd frqvlvw ri txduwhuo| revhuydwlrqv rq rxwsxw/ d prqhwdu| djjuhjdwh/ frqvxphu sulfhv/
krxvh sulfhv dqg d qrplqdo vkruw0whup lqwhuhvw udwh lq vl{ Hxurshdq hfrqrplhv +Iudqfh/ Jhu0
pdq|/ Lwdo|/ Vsdlq/ Vzhghq dqg Xqlwhg Nlqjgrp,1 Zlwk wkh h{fhswlrq ri Vsdlq/ zkhuh d txdu0
whuo| krxvh sulfh zdv dydlodeoh rqo| vwduwlqj iurp 4<;:/ wkh gdwd fryhu d shulrg zklfk vsdqv
dssur{lpdwho| ryhu wkh odvw 58 |hduv1
4< Dq h{dpsoh 0 |hw qrw ri d prqhwdu| vkrfn 0 vkrzlqj wkdw krxvh sulfhv duh qrw dv vwlfn| dv frqvxphu sulfhv
dqg wkdw lpsrvlqj }hur lpsdfw uhvwulfwlrqv rq wkhp pljkw eh lqdssursuldwh +hyhq lq wlphv orz0lq dwlrq shulrgv,
lv surylghg e| Srwhued +4<<4,= krxvh sulfhv duh uhsruwhg wr kdyh ulvhq 8 shufhqw zlwklq d zhhn ri wkh vhohfwlrq ri
Ehuolq dv wkh qhz fdslwdo ri Jhupdq|1
53 Dq dowhuqdwlyh lqwhusuhwdwlrq lv wkdw wklv vkrfn pljkw eh dq h{fkdqjh udwh vkrfn/ wkdw udlvhv wkh sulfhv ri
lpsruwhg jrrgv wkxv whpsrudulo| ghsuhvvlqj rxwsxw1 L wkdqn Jxqwkhu Frhqhq iru wklv vxjjhvwlrq1
 ECB Working Paper No 18 G April 2000                                                                                                  17
Wkh txdolw| ri gdwd iru krxvh sulfhv/ zklfk zhuh froohfwhg iurp glhuhqw vrxufhv/ glhuv
iurp frxqwu| wr frxqwu|= krzhyhu/ vlqfh wkh sxusrvh ri wklv sdshu lv pruh wr surylgh hylghqfh
rq g|qdplfv ri krxvh sulfhv udwkhu wkdq frpsdulqj wkhlu ohyhov dfurvv frxqwulhv/ phdvxuhphqw
sureohpv vkrxog qrw eh ryhuvwdwhg1
Lw lv srvvleoh/ lq sulqflsoh/ wkdw wkh wlph vhulhv gr qrw
uh hfw dgmxvwphqwv iru wkh txdolw| ri krxvlqj vwrfn1 Qhyhuwkhohvv/ wklv vkrxog rqo| dhfw wkh
hvwlpdwh ri wkh frlqwhjudwlqj yhfwru ehwzhhq uhdo krxvh sulfhv dqg rxwsxw/ zlwkrxw dq| rwkhu
pdmru vlgh0hhfwv rq rwkhu/ vkruw0uxq/ g|qdplfv1
Iuhqfk gdwd iru krxvh sulfhv frph iurp wkh Edqtxh ri Iudqfh +4<<<,/ zklfk kdv uhfhqwo|
vwduwhg wr fdofxodwh d uhvlghqwldo krxvh sulfh lqgh{541 Jhupdq gdwd duh iurp wkh Dxqd Uhv0
lghqwldo Sulfh Lqgh{= wkh ruljlqdo vhulhv zdv dqqxdo/ dqg d txduwhuo| rqh zdv lqwhusrodwhg yld
lqwhusrodwlrq dvvxplqj dq DULPD+3/5/3, lq wkh ruljlqdo vhulhv551 Gdwd iru Lwdo| duh iurp wkh
uhvlghqwldo surshuw| sulfh lqgh{ fdofxodwhg e| wkh pdjd}lqh Lo Frqvxohqwh Lppreloduh +zlwk
hoderudwlrq e| wkh Edqn ri Lwdo|,> wkh ruljlqdo vhpl0dqqxdo iuhtxhqf| zdv frqyhuwhg lqwr txdu0
whuo| yld lqwhusrodwlrq1 Gdwd iru Vsdlq frph iurp wkh Uhvlghqwldo Surshuw| Sulfh Lqgh{ shu
Vtxduh Phwhu/ surylghg e| wkh Plqlvwhulr gh Hfrqrpld | Kdflhqgd1 Iru Vzhghq/ wkh gdwd zhuh
surylghg e| wkh Fhqwudo Vwdwlvwlfdo R!fh Krxvh Sulfh Lqgh{561 Ilqdoo|/ XN gdwd fdph iurp wkh
Qdwlrqzlgh Dqjold txduwhuo| krxvh sulfh lqgh{ iru doo surshuwlhv1 Doo wkh wlph vhulhv duh dydlodeoh
dssur{lpdwho| iurp wkh plg *:3v/ zlwk wkh h{fhswlrq ri Vsdlq +zkhuh wkh vhulhv ehjlqv lq 4<;:,
dqg XN +4<96,1 Wr pdnh uhvxowv pruh frpsdudeoh dfurvv frxqwulhv/ wkh hvwlpdwlrq shulrg iru
XN vwduwv lq 4<:61
Wkh uhvxowlqj vdpsohv wxuqhg rxw wr eh dv iroorzv= iru Iudqfh/ 4<:;=4 0 4<<:=7 +;3 re0
vhuydwlrqv,> iru Jhupdq|/ 4<:6=4 0 4<<;=6 +436 revhuydwlrqv,> iru Lwdo|/ 4<:6=4 0 4<<;=5 +435
revhuydwlrqv,> iru Vsdlq/ 4<;:=7 0 4<<;=7 +78 revhuydwlrqv,> iru Vzhghq/ 4<::=7 0 4<<;=7 +;8 re0
vhuydwlrqv,> iru Xqlwhg Nlqjgrp/ 4<:6=404<<;=6 +436 revhuydwlrqv,1 Wkh uhvxowlqj krxvh sulfh
lqglfhv/ wrjhwkhu +iru frpsdulvrq sxusrvhv, zlwk wkh frqvxphu sulfh lqglfhv/ duh vkrzq lq Iljxuh
41 Wkh Iljxuh surylghv hylghqfh ri wkh odujh vzlqjv lq krxvh sulfhv wkdw kdyh rffxuuhg lq doo
wkh frxqwulhv lq wkh odvw ghfdghv/ zlwk surorqjhg f|fohv ri lqfuhdvlqjo| ulvlqj sulfhv iroorzhg e|
voxpsv> rvfloodwlrqv lq uhdo krxvh sulfhv vhhp wr kdyh ehhq sduwlfxoduo| vwurqj lq Vzhghq dqg
54 Vlqfh 4<:;/ dq dqqxdo lqgh{ ri uhvlghqwldo surshuw| sulfhv kdv ehhq hvwlpdwhg lq Iudqfh rq wkh edvlv ri wkh
sruwirolr ri wkh IQDLP qdwlrqdo ihghudwlrq ri uhdo hvwdwh djhqwv/ zklfk frpsulvhv 553333 surshuwlhv1 Wkh Edqtxh
gh Iudqfh kdv wkhq wudqviruphg wklv lqgh{ lqwr d txduwhuo| rqh e| surolqj xvlqj wkh lqgh{ ri wkh Fkdpeuh
V|qglfdoh ghv qrwdluhv iru rog xqrffxslhg dsduwphqwv vrog lq Sdulv1
55 Wkh DXILQD2HUD lqgh{ vkrzv wkh dyhudjh sulfh iru d fxelf phwuh hqforvhg duhd iru d 6 |hdu rog krxvh
zlwk dq dyhudjh lqgh{1 Lw lv frqvwuxfwhg wkurxjk vxuyh|v frqgxfwhg e| DXILQD2HUD dfurvv uhdo hvwdwh djhqwv
lq wkh frxqwu|1
Lq wkh zrugv ri Kropdqv +4<<7,/ Jhupdq krxvh sulfh klvwru| lv idu iurp up1 Krzhyhu/ wkh vhulhv surylghg
e| Dxqd/ zklfk lv xvhg lq wklv sdshu/ lv vlplodu wr wkdw frqvwuxfwhg e| Kropdqv +4<<7, xvlqj flw|0ohyho gdwd
surylghg e| wkh hvwdwh djhqf| Ulqj Ghxwvfkhu Pdnohu1
56 Wkh Vzhglvk krxvh sulfh vhulhv lv frqvwuxfwhg dv zhljkwhg phdq ri sulpdu| dqg ohlvxuh krphv +L wkdqn Ekdudw
Edurw iru nlqgo| surylglqj ph zlwk wkh vhulhv,1
18                                                                                                      ECB Working Paper No 18 G April 2000
XN> shulrgv ri idoolqj qrplqdo krxvh sulfhv kdyh ehhq frpprq lq doo wkh frxqwulhv1
Wkh rwkhu vhulhv zhuh doo rewdlqhg iurp Lqwhuqdwlrqdo Ilqdqfldo Vwdwlvwlfv ri wkh LPI= | lv
phdvxuhg e| +orj ri, JGS dw frqvwdqw sulfhv/ vhdvrqdoo| dgmxvwhg> l lv d phdvxuh ri d vkruw0whup
lqwhuhvw udwh/ h{suhvvhg lq shufhqwdjhv/ qdpho| prqh| pdunhw udwh iru Lwdo|/ fdoo prqh| udwh iru
Iudqfh dqg Jhupdq|/ 6 prqwkv W0Eloo udwh iru Vsdlq/ Vzhghq dqg Xqlwhg Nlqjgrp> uhdo prqh|
ps lv wkh +gh dwhg e| wkh frqvxphu sulfh lqgh{, orj ri P5 iru Iudqfh/ Vsdlq dqg Vzhghq> P4
iru Jhupdq|/ Lwdo| dqg XN1 Wkh uhvxowv glg qrw ydu| pxfk xvlqj P5 lqvwhdg ri P4 iru wkh odvw
wkuhh frxqwulhv/ exw P4 surgxfhg pruh sodxvleoh hvwlpdwhv ri wkh frlqwhjudwlqj yhfwruv dqg ri
wkh uhvsrqvhv wr vkrfnv1 Lq dwlrq/ / lv phdvxuhg e| wkh dqqxdolvhg txduwhuo| fkdqjh ri wkh +orj
ri, frqvxphu sulfh lqgh{1
Iru hdfk frxqwu|/ wkh hvwlpdwhg YDU frqwdlqhg d odj ohqjwk ri 6 +Iudqfh/ Vsdlq/ Vzhghq,
ru 7 +Jhupdq|/ Lwdo|/ XN,/ ghshqglqj rq zklfk zdv vx!flhqw wr rewdlq qrlvholnh uhvlgxdov1
Wzr lpsxovh gxpplhv zhuh xvhg wr fruuhfw iru Jhupdq uhxqlfdwlrq +4<<3=6 dqg 4<<4=4,1 Dq
lpsxovh gxpp| yduldeoh iru XN iru 4<;:=4 zdv lqwurgxfhg wr fdswxuh d fryhudjh euhdn lq wkh
prqh|.txdvl0prqh| LIV vhulhv1
715 Xqlw urrw dqg Frlqwhjudwlrq Whvwv
Dv d suholplqdu| vwhs/ dqg lq rughu wr vshfli| wkh prgho fruuhfwo|/ wkh orqj0uxq surshuwlhv ri wkh
wlph0vhulhv lqyroyhg/ l1h1 wkhlu ghjuhh ri lqwhjudwlrq dqg wkh hyhqwxdo suhvhqfh ri frlqwhjudwlqj
uhodwlrqvklsv/ pxvw eh fkdudfwhulvhg1
71514 Xqlw urrw whvwv
Wzr xqlyduldwh xqlw0urrw whvwv zhuh frqgxfwhg/ wkh dxjphqwhg Glfnh|0Ixoohu whvw dqg wkh Skloolsv0
Shuurq +4<;;, whvw1 Wdeohv 714 dqg 715 uhsruw wkh uhvxowv iurp wkh whvwv1 Ryhudoo/ wkh slfwxuh
wkdw hphujhv iurp wkh whvwv klqwv wkdw wkh yduldeohv duh lqwhjudwhg ri rughu rqh/ dowkrxjk/ xvlqj
wkh Skloolsv0Shuurq whvw/ lq pdq| frxqwulhv wkh qxoo k|srwkhvlv ri d xqlw urrw lq wkh lq dwlrq udwh
lv uhmhfwhg lq idyrxu ri vwdwlrqdulw|1
71515 Frlqwhjudwlrq whvwv
Wklv vxe0vhfwlrq ghvfulehv wkh hvwlpdwlrq ri wkh frlqwhjudwlrq yhfwruv iru hdfk frxqwu| zlwk
wkh pxowlyduldwh frlqwhjudwlrq whfkqltxhv ghvfulehg e| Mrkdqvhq dqg Mxvholxv +4<<3,1 Wkh wkuhh
frlqwhjudwlqj yhfwruv fdq eh lqwhusuhwhg dv d prqh| ghpdqg vfkhgxoh/ d orqj uxq krxvlqj vxsso|
fxuyh dqg d Ilvkhu htxdwlrq1 Krzhyhu/ wkh yhfwruv vkrxog eh lqwhusuhwhg zlwk fduh/ dw ohdvw iru
wkuhh uhdvrqv= 4, wkh vshflfdwlrq ri wkh prqh| ghpdqg vfkhgxoh lv suredeo| xqghusdudphwulvhg/
 ECB Working Paper No 18 G April 2000                                                                                                     19
Wdeoh 714= Dxjphqwhg Glfnh|0Ixoohu xqlw urrw whvwv
IUDQFH
JHUPDQ\
LWDO\
VSDLQ
VZHGHQ
X1N1
+
03143
3147
05156
031<<
03195
0313<
6R
0415:
4143
031;;
03154
0513:
03147
R
05194
05169
05164
05197
0516<
04173

031<:
05195
0418<
03154
0419:
05164
Z
03198
05153
04194
0319;
041::
051:9
Dxjphqwhg Glfnh|0Ixoohu xqlw urrw whvwv vwdwlvwlfv iru wkh vhulhv/ zlwk d odj ohqjwk ri 6 iru Iudqfh/ Vsdlq dqg
Vzhghq/ 7 iru Jhupdq|/ Lwdo| dqg XN> - lqglfdwhv uhmhfwlrq ri wkh qxoo k|srwkhvlv ri xqlw urrw dw wkh <8(
frqghqfh ohyho/ -- dw wkh <<( ohyho 0 ghshqglqj rq wkh vdpsoh vl}h/ wkh <8( PdfNlqqrq +4<<4, fulwlfdo ydoxh
udqjhv iurp 051;< wr 051<5 01
Wdeoh 715= Skloolsv0Shuurq Xqlw urrw whvwv
IUDQFH
JHUPDQ\
LWDO\
VSDLQ
VZHGHQ
X1N1
+
03178
03176
05138
041::
03195
0313<
6R
0318;
31<;
04144
031;5
041<8
414<
R
05177
0615:-
041<7
0713;--
041:4
0316<

04146
0517;
041<3
0318<
041:6
0516;
Z
04186
071<;--
051<:-
06139-
071<4--
0717;--
Skloolsv0Shuurq xqlw urrw whvwv vwdwlvwlfv iru wkh vhulhv/ zlwk d odj ohqjwk ri 6 iru Iudqfh/ Vsdlq dqg Vzhghq/ 7 iru
Jhupdq|/ Lwdo| dqg XN> - lqglfdwhv uhmhfwlrq ri wkh qxoo k|srwkhvlv ri xqlw urrw dw wkh <8( frqghqfh ohyho/ --
dw wkh <<( ohyho 0 ghshqglqj rq vdpsoh vl}h/ wkh <8( fulwlfdo ydoxh udqjhv iurp 051;< wr 051<5 0 1
dv orqj0whup lqwhuhvw udwhv/ qdqfldo zhdowk dqg lq dwlrq duh h{foxghg iurp wkh vshflfdwlrq>
5, qdqfldo lqqrydwlrq lv olnho| wr dhfw wkh vwdelolw| ri prqh| ghpdqg ryhu wkh vdpsoh> 6,
frlqwhjudwlqj uhodwlrqvkls duh lghqwlhg rqo| xs wr d olqhdu frpelqdwlrq/ khqfh qr vlqjoh yhfwru
fdq eh hdvlo| lqwhusuhwhg dv ghvfulelqj d phdqlqjixo hfrqrplf uhodwlrqvkls571
Frlqwhjudwlrq whvwv zhuh uxq iru wkh vl{ frxqwulhv1 Dffruglqj wr wkh odpegd0pd{ vwdwlvwlf
+vhh Mrkdqvhq dqg Mxvholxv/ 4<<3/ iru d ghvfulswlrq,/ wkh qxoo k|srwkhvlv ri qr0frlqwhjudwlrq
yhuvxv rqh frlqwhjudwlrq yhfwru/ ri rqh frlqwhjudwlrq yhfwru yhuvxv wzr zdv uhmhfwhg dw wkh <3(
frqghqfh ohyho lq doo frxqwulhv1 Wkuhh frlqwhjudwlqj yhfwruv zhuh vxjjhvwhg lq Iudqfh/ Jhupdq|
dqg Vzhghq/ zkhuhdv wzr dsshdu pruh olnho| lq Jhupdq| dqg Lwdo|/ dqg irxu lq Vsdlq1 Krzhyhu/
wkhruhwlfdo uhdvrqv wr eholhyh wkdw d frlqwhjudwlqj udqn ri wkuhh ohdgv wr d sodxvleoh hfrqrplf
lqwhusuhwdwlrq ri wkh vkrfnv kdyh ohg ph wr edvh wkh uhvw ri wkh dqdo|vlv rq d udqn ri u @ 61
57 Wkh olwhudwxuh rq wklv lvvxh lv ri frxuvh hqruprxv1 Wr qdph d ihz vwxglhv/ vhh Idvh dqg Zlqghu +4<<;,/
Khqgu| +4<<8,/ Hulfvvrq +4<<;,1
20                                                                                                      ECB Working Paper No 18 G April 2000
Wdeoh 716= Sdudphwhu hvwlpdwhv ri wkh frlqwhjudwlrq yhfwruv
Frxqwu|
Shulrg
FY4
FY5
FY6
S0ydoxh
&fy <3(
+b0pd{,
Iudqfh
:;=7 0 <:=7
6R2 ' +n Dfee
Ef.e o
R '.
EfD +
| ' Z|
144
6
Jhupdq|
:6=4 0 <;=6
6R '2f.D
Ef2b +n D
E2.2 o
R 'fS
Ef2 +
| ' Z|
143
5
Lwdo|
:6=4 0 <;=5
6R ' ebD+n f
Eefb o
R '2e
EH. +
| ' Z|
186
5
Vsdlq
;:=7 0 <;=7
6R2 'SD
EH +3 S.
E2 o
R 'Sb
E2 +
| ' Z|
134
6
Vzhghq
::=7 0 <;=7
6R2 ' +n D.
EHe o
R 'HSe
EDb +
| ' Z|
137
6
XN
:6=4 0 <;=6
6R 'b2S
E2 +3 .f2
EDD o
R ' S
E +
| ' Z|
1;5
7
Sdudphwhu hvwlpdwhv ri wkh wkuhh frlqwhjudwlrq yhfwruv +vwdqgdug huuruv lq eudfnhwv,1 Wkh qh{w wr odvw froxpq
uhihuv wr wkh R0ydoxh ri wkh olnholkrrg udwlr whvw vwdwlvwlf iru ryhulghqwli|lqj uhvwulfwlrqv rq wkh frlqwhjudwlqj yhfwruv/
zkhuhdv wkh odvw froxpq uhihuv wr wkh qxpehu ri frlqwhjudwlqj yhfwruv vxjjhvwhg e| wkh odpegd0pd{ vwdwlvwlf dw
wkh <3( frqghqfh ohyho1
716 Frlqwhjudwlrq uhodwlrqv
Wdeoh 716 uhsruwv wkh hvwlpdwhg wkuhh frlqwhjudwlqj yhfwruv iru hdfk frxqwu| jlyhq rqh ryhu0
lghqwli|lqj uhvwulfwlrq rq wkh frlqwhjudwlqj vsdfh/ wrjhwkhu zlwk s0ydoxhv iru wkh ryhu0lghqwli|lqj
uhvwulfwlrq lpsrvhg xsrq wkh frlqwhjudwlqj yhfwruv1 Wkh uhvwulfwlrqv zhuh uhmhfwhg dw wkh <8(
frqghqfh ohyho rqo| lq Vzhghq dqg Vsdlq581 Vlqfh lw kdv ehhq vkrzq +Mdfrevrq/ Yuhglq dqg
Zduqh/ 4<<;,1 wkdw wkh olnholkrrg udwlr whvw iru k|srwkhvlv derxw wkh frlqwhjudwlrq yhfwruv iru
d jlyhq udqn whqgv wr eh ryhuvl}hg/ L suhihu wr suhvhqw iru uhdvrqv ri vsdfh rqo| wkh uhvwulfwhg
frlqwhjudwlqj yhfwruv/ zlwk vwdqgdug huuruv lq sduhqwkhvhv= wkh orvv ri lqirupdwlrq vkrxog qrw eh
juhdw/ dv xquhvwulfwhg dqg uhvwulfwhg yhfwruv +xsrq d frqyhqlhqw urwdwlrq ri wkh odwwhu, vkrxog eh
vlplodu1
D ihz frpphqwv duh lq rughu jlyhq wkh hylghqfh rq wkhvh frlqwhjudwlqj yhfwruv1
4, Wkh hvwlpdwhg lqfrph hodvwlflw| ri prqh| ghpdqg e+ lv dozd|v juhdwhu wkdq rqh lq wkh
fdvhv lq zklfk lv qrw uhvwulfwhg wr xqlw|1 Wklv pljkw eh wkh frqvhtxhqfh ri rplwwlqj zhdowk
yduldeohv lq wkh prqh| ghpdqg/ vxfk dv krxvlqj zhdowk/ zklfk lv srvlwlyho| fruuhodwhg zlwk
lqfrph1
5, Wkh hvwlpdwhg vhpl0hodvwlflw| ri prqh| ghpdqg zlwk uhvshfw wr wkh vkruw0whup lqwhuhvw
udwh/ e/ lv qhjdwlyho| vljqhg rqo| lq wzr fdvhv rxw ri vl{1 Iru Iudqfh dqg Vzhghq/ wkh lpsolhg
hodvwlflw| ri uhdo P5 lv vljqlfdqwo| srvlwlyh= |hw d srvlwlyh hodvwlflw| lv sodxvleoh rq wkhruhwlfdo
jurxqgv/ dv d qhjdwlyh frh!flhqw vkrxog eh h{shfwhg d sulrul rqo| rq +vrph phdvxuh ri, qduurz
prqh|/ dv glvfxvvhg iru lqvwdqfh e| Idvh dqg Zlqghu +4<<;, dqg Hulfvvrq +4<<;,1 Wklv vshfl0
fdwlrq lv wkdw lw lpsolhv wkh vrphkrz frxqwhuidfwxdo uhvxow wkdw wkh qrplqdo vkrfn |lhogv kljkhu
58 Lq Iudqfh dqg Vzhghq/ L lpsrvhg xqlw hodvwlflw| ri prqh| zlwk uhvshfw wr lqfrph/ dv wkh xquhvwulfwhg lqfrph
hodvwlflw| zdv phdvxuhg zlwk juhdw lpsuhflvlrq dqg ohg wr lpsodxvleoh hvwlpdwhv iru wkh prqh| ghpdqg hodvwlflwlhv1
ECB Working Paper No 18 G April 2000                                                                                                      21
qrplqdo udwhv dqg kljkhu lq dwlrq lq wkh orqj0uxq/ exw dovr orzhu uhdo prqh| edodqfhv1 Wklv
uhvxow grhv qrw dhfw wkh lqwhusuhwdwlrq ri wkh wudqvlwru| vkrfnv/ dqg frxog eh pruh jurxqghg
rq hfrqrplf wkhru| li zh odehoohg wkh glvwxuedqfh dv/ vd|/ d yhorflw| vkrfn udwkhu wkdq d
fuhglelolw| vkrfn1
6, Wkh hvwlpdwhg frlqwhjudwlrq yhfwru ehwzhhq uhdo krxvh sulfhv dqg JGS idyrxuv dq lqwhu0
suhwdwlrq ri wkh orqj0uxq xszdug wuhqg lq krxvh sulfhv wkdw/ ghvslwh wkh vkruw gdwdvhwv/ vhhpv
wr eh frqvlvwhqw dfurvv frxqwulhv591 Wkh srlqw hvwlpdwhv ri wkh frh!flhqw  udqjh iurp d orzhu
olplw ri 1396 iru Jhupdq| wr 419< iru Vsdlq1 Wkhvh hvwlpdwhv vkrxog lq dq| fdvh eh wuhdwhg zlwk
juhdw fduh/ dv wkh| duh yhu| vhqvlwlyh wr wkh shulrg wkh| fryhu= frlqwhjudwlrq ehwzhhq uhdo krxvh
sulfhv dqg rxwsxw fdq eh d vwdwlvwlfdo surshuw| ri wkh gdwd/ exw sxwwlqj vwuxfwxudo hpskdvlv rq
furvv0frxqwu| glhuhqfhv zrxog eh suredeo| wrr dpelwlrxv/ qrw ohdvw ehfdxvh wkh krxvh sulfh
lqglfhv duh qrw krprjhqrxv dfurvv frxqwulhv1
8 Hpslulfdo hylghqfh
814 Lpsxovh uhvsrqvhv
Wklv vhfwlrq orrnv dw wkh hfrqrphwulf uhvxowv ri wkh vshflfdwlrq1 Wkh sxusrvh ri wklv vhfwlrq lv
wkuhhirog=
4, Wr fkhfn zkhwkhu wkh lghqwlfdwlrq vfkhph ohdgv wr sodxvleoh hvwlpdwhv ri wkh vkrfnv> dv
Fkulvwldqr/ Hlfkhpedxp dqg Hydqv +4<<<, pdnh fohdu/ wkhuh lv qr frqyhujhqfh lq wkh olwhudwxuh
rq d sduwlfxodu vhw ri dvvxpswlrqv iru lghqwli|lqj wkh hhfwv ri dq h{rjhqrxv vkrfn wr prqhwdu|
srolf|1 Wkh vdph uhpdun dssolhv wr rwkhu vkrfnv wkdw gulyh hfrqrplf xfwxdwlrqv +Frfkudqh/
4<<7,1 \hw wkh lqihuhqfh xsrq wkh hhfwv ri pdq| ri wkhvh vkrfnv lv urexvw dfurvv d odujh vxevhw
ri lghqwlfdwlrq vfkhphv wkdw kdyh ehhq wulhg lq wkh olwhudwxuh= diwhu d frqwudfwlrqdu| prqhwdu|
vkrfn/ lqwhuhvw udwhv jr xs/ sulfh ohyho uhvsrqgv vorzo|/ rxwsxw dqg prqhwdu| djjuhjdwhv idoo1
Diwhu d srvlwlyh ghpdqg vkrfn/ rxwsxw/ lqwhuhvw udwhv dqg sulfhv lqfuhdvh/ dv lq Jdol +4<<5, dqg
Jhuodfk dqg Vphwv +4<<8,1
5, Wr frpsduh wkh uhvsrqvh ri hfrqrplhv iroorzlqj d vkrfn1
Zh zrxog h{shfw wkdw wkh
vdph lghqwlfdwlrq vfkhph |lhogv frqvlvwhqw hvwlpdwhv dfurvv hfrqrplhv1 Lw zrxog eh kdug wr
odeho d wudqvlwru| glvwxuedqfh prqhwdu| vkrfn li lw lpsolhv d vhw ri lpsxovh uhvsrqvhv wkdw lv
lqfrqvlvwhqw zlwk hyhu| hohphqw lq wkh vhw ri pdfurhfrqrplf prghov wkdw zh zlvk wr glvfulplqdwh
ehwzhhq1
59 Wklv lv eurdgo| lq olqh zlwk wkh hylghqfh wkdw wkh Nhqqhg| dqg Dqghuvrq +4<<7, vwxg| rq 48 frxqwulhv ryhu
wkh odvw 58 |hduv surylghv= d orrn dw wkh judskv iurp sdjh 65 wr 68 ri wkhlu sdshu vkrzv wkdw lq 46 rxw ri 48
qdwlrqv uhdo krxvh sulfhv zhuh kljkhu lq 4<<6 wkdq lq 4<:31 Vdph hylghqfh lv irxqg lq Fxwohu +4<<8, iru wkh J:
hfrqrplhv iurp 4<:3 wr 4<<51
22                                                                                                                                             ECB Working Paper No 18 G April 2000
Wdeoh 814= Orqj uxq lpsdfw ri wkh shupdqhqw vkrfnv
IUDQFH
JHUPDQ\
LWDO\
VSDLQ
VZHGHQ
XN
vxs1
qrp1
vxs1
qrp1
vxs1
qrp1
vxs1
qrp1
vxs1
qrp1
vxs1
qrp1
+
4154
3133
31<:
3133
31;;
3133
4134
3133
4155
3133
31;6
3133
Z
03135
317:
03154
3186
3134
3175
3138
3166
03153
3163
3143
3179
6R
413<
5169
41<7
314<
4177
4179
4183
04154
314;
4195
31::
06164
R
3185
3133
3139
3133
31<8
3133
41:4
3133
4139
3133
317;
3133
o
03135
317:
03154
3186
3134
3175
3138
3166
03153
3163
3143
3179
Orqj uxq lpsdfw ri wkh wzr shupdqhqw +vxsso| dqg qrplqdo, vkrfnv/ rqh vwdqgdug huuru lq vl}h +shufhqwdjh
fkdqjhv,1
6, Wr dvvhvv krz krxvh sulfhv uhvsrqg wr vkrfnv/ zkhwkhu wkh uhvsrqvhv duh frqvlvwhqw dfurvv
hfrqrplhv/ zkdw pljkw eh wkh uhdvrqv iru wkhvh uhvsrqvhv/ dqg zkhwkhu lw lv srvvleoh wr lqihu dq|
sduwlfxodu wudqvplvvlrq phfkdqlvp zlwk zklfk wkh lpsxovh uhvsrqvhv iru krxvh sulfhv pljkw eh
frqvlvwhqw1 Qhhgohvv wr vd|/ wklv lv d yhu| gl!fxow wdvn/ ehfdxvh ri wkh xqfhuwdlqw| vxuurxqglqj wkh
lpsxovh uhvsrqvhv dqg ehfdxvh wkh hpslulfdo surfhgxuh rqo| lghqwlhv htxloleulxp uhvsrqvhv
wr prqhwdu| vkrfnv1
81414 Shupdqhqw vkrfnv
Wdeoh 814 suhvhqwv wkh hvwlpdwhv ri wkh orqj0uxq lpsdfwv ri vxsso| dqg ghpdqg vkrfnv +fru0
uhvsrqglqj wr wkh S pdwul{ glvfxvvhg deryh, iru wkh 9 frxqwulhv dqdo|vhg1 Wklv wdeoh vkrzv/
iru lqvwdqfh/ wkdw wkh orqj0uxq hhfw ri d rqh0vwdqgdug ghyldwlrq vxsso| vkrfn udlvhv rxwsxw lq
Iudqfh e| 4154 shufhqwdjh srlqwv +wkh jxuh lq wkh wrs ohiw sdqho,/ uhdo edodqfhv +yld lqfuhdvhg
prqh| ghpdqg, e| 413< shufhqw/ uhdo krxvh sulfhv e| 3185 shufhqw/ dqg kdv d qhjoljleoh hhfw
+03135 shufhqw, rq lq dwlrq dqg lqwhuhvw udwhv1
Vxsso| vkrfnv
Wkh uvw urz ri Iljxuhv 5 wr : surylgh wkh hvwlpdwhg uhvsrqvh ri wkh hfrqrp|
wr d idyrxudeoh/ rqh0vwdqgdug ghyldwlrq vkrfn wr wkh djjuhjdwh vxsso| glvwxuedqfh/ dorqj zlwk
rqh0vwdqgdug huuru dv|pswrwlf frqghqfh edqgv5:1 Edvhg rq wkh vshflfdwlrq ri wkh frlqwh0
judwlrq yhfwruv dqg rq wkh pdwul{ ri frpprq wuhqgv/ wklv vkrfn kdv ehhq lghqwlhg xqghu wkh
dvvxpswlrq wkdw lw ohdgv wr dq lqfuhdvh ri rxwsxw lq wkh orqj0uxq/ dv zhoo dv wr dq lqfuhdvh lq uhdo
krxvh sulfhv/ zlwk sursruwlrqv glfwdwhg e| wkh frh!flhqw  phdvxulqj wkh orqj0uxq hodvwlflw| ri
uhdo krxvh sulfhv wr JGS1 D furvv frxqwu| frpsdulvrq ri wkh lpsxovh uhvsrqvhv fdq eh vhhq lq
Iljxuh ;/ zkhuh L dovr sorw wkh lpsolhg uhvsrqvhv ri frqvxphu +S,/ qrplqdo krxvh sulfhv +K,/
dqg h{ srvw uhdo lqwhuhvw udwhv +U  GS,1 L zloo uhshdw d vlplodu h{huflvh iru wkh rwkhu vkrfnv dv
5: Iru d glvfxvvlrq rq krz wr frpsxwh frqghqfh lqwhuydov iru wkh frpprq wuhqgv prgho/ vhh Zduqh +4<<6,
dqg Yoddu +4<<;,1
 ECB Working Paper No 18 G April 2000                                                                                                     23
zhoo1
Wkh lqlwldo hhfw rq rxwsxw lv srvlwlyh iru doo wkh frxqwulhv= lq wkh lpsdfw shulrg/ wkh srlqw
hvwlpdwh udqjhv iurp 3135 shufhqw lq Lwdo| wr 319 shufhqw lq Xqlwhg Nlqjgrp1
Diwhu derxw
wkuhh |hduv/ rxwsxw vwdelolvhv dw lwv kljkhu vwhdg| vwdwh ohyho kdylqj lqfuhdvhg e|/ rq dyhudjh/ 4
shufhqwdjh srlqw1 Lq doo wkh frxqwulhv exw Vsdlq frqvxphu sulfhv duh ehorz wkh edvholqh diwhu
rqh |hdu/ dv suhglfwhg e| d vlpsoh djjuhjdwh ghpdqg 0 djjuhjdwh vxsso| prgho1 Wkh qrplqdo
lqwhuhvw udwh kdugo| pryhv/ dv wkh lqfuhdvh lq prqh| ghpdqg lv vdwlvhg e| d whpsrudu| ghfuhdvh
lq wkh sulfh ohyho dqg e| lqfuhdvhg prqh| vxsso|1 Lq doo wkh frxqwulhv/ wkh orqj0uxq hhfw ri d
vxsso| vkrfn rq lq dwlrq dqg qrplqdo udwhv lv qhjoljleoh/ dowkrxjk wkhuh lv d qhjdwlyh orqj uxq
hhfw rq wkh ohyho ri frqvxphu sulfhv5;1
Lq doo frxqwulhv/ krxvh sulfhv jr grzq iru vrph txduwhuv ehiruh lqfuhdvlqj wr wkhlu qhz
vwhdg| vwdwh/ kljkhu ohyho1 Lq d shuihfw fdslwdo pdunhw/ rqh zrxog h{shfw ryhuvkrrwlqj ri krxvh
sulfhv iroorzhg wkhq e| d judgxdo dgmxvwphqw wrzdugv wkh orqj0uxq/ kljkhu htxloleulxp ohyho1
Rqh srvvleoh mxvwlfdwlrq iru wkh uhvxow lv wkh iroorzlqj= e| udlvlqj wkh uhwxuq wr fdslwdo/ wkh
vxsso| vkrfn jhqhudoo| lqfuhdvhv uhdo lqwhuhvw udwhv> wklv whpsrudu| hhfw uhgxfhv wkh ghpdqg
iru krxvhv> rqo| zkhq uhdo udwhv duh edfn wr wkh edvholqh/ wkh lqfrph hhfw ehfrphv juhdwhu
wkdq wkh vxevwlwxwlrq +xvhu frvw, hhfw/ dqg uhdo krxvh sulfhv jr xs1 Ylvxdo lqvshfwlrq ri Iljxuh
; vxjjhvwv d qhjdwlyh fruuhodwlrq ehwzhhq ehkdylrxu ri uhdo udwhv dqg ehkdylrxu ri uhdo krxvh
sulfhv1
Qrplqdo vkrfn
Wkh shupdqhqw qrplqdo lqqrydwlrq +vhfrqg urz ri Iljxuhv 5 wr :, udlvhv
lq dwlrq dqg qrplqdo udwhv e| wkh vdph dprxqw lq wkh orqj uxq1 Lw lv lqdgylvdeoh wr sxw wrr
pxfk vwuxfwxudo hpskdvlv rq wklv vkrfn/ hvshfldoo| ehfdxvh/ dv vkrzq lq Iljxuh </ wkhuh lv qrw
d krprjhqhrxv/ glvfhuqleoh sdwwhuq dfurvv hfrqrplhv lq wkh uhvsrqvh ri wkh yduldeohv1
Rqh
lqwhusuhwdwlrq lv wkdw ri d shupdqhqw lqqrydwlrq wr wkh h{shfwhg udwh ri lq dwlrq> wkhuhiruh wkh
dvvrfldwhg uhvsrqvhv lq krxvh sulfhv fdq whvw zkhwkhu krxvhv duh ylhzhg dv d khgjh djdlqvw
lq dwlrq1 Lq Vzhghq/ Lwdo| dqg Jhupdq| uhdo krxvh sulfhv jr xs/ dowkrxjk wkh huuru edqgv duh
vrphzkdw odujh1 Wklv lqfuhdvh lq h{shfwhg lq dwlrq dovr holflwv dq xszdug uhvsrqvh ri qrplqdo
lqwhuhvw udwhv/ zklfk lv vxjjhvwlyh ri dq dqwl0lq dwlrqdu| prqhwdu| srolf| iurp wkh prqhwdu|
dxwkrulw|= |hw wklv prqhwdu| srolf| uhdfwlrq grhv qrw eulqj derxw dq| vljqlfdqw hhfw lq wkh
krxvlqj pdunhw1
5; Vsdlq lv wkh rqo| h{fhswlrq1
24                                                                                                      ECB Working Paper No 18 G April 2000
81415 Whpsrudu| vkrfnv
Prqhwdu| vkrfn
L vhsdudwh wkh wkuhh whpsrudu| vkrfnv lpsrvlqj uhvwulfwlrqv rq wkhlu frqwhp0
srudqhrxv hhfwv lq d uhfxuvlyh idvklrq1 Iroorzlqj zlghvsuhdg wudglwlrq lq wkh YDU olwhudwxuh/
wkh prqhwdu| glvwxuedqfh lv lghqwlhg xqghu wkh dvvxpswlrq wkdw lw grhv qrw dhfw frqwhpsrud0
qhrxvo| rxwsxw dqg lq dwlrq1 Wkh lghqwlfdwlrq vfkhph vhhpv vxffhvvixo/ dv hylghqfh lq Iljxuh
43 +dqg wklug urz ri Iljxuhv 5 wr :, vkrzv wkdw wklv vkrfn holflwv xszdug suhvvxuh lq lqwhuhvw udwh/
d frqwudfwlrq lq wkh prqhwdu| djjuhjdwh5</ dqg d whpsrudu| ghfolqh lq rxwsxw/ wkdw erwwrpv
rxw dssur{lpdwho| ehwzhhq 7 dqg < txduwhuv diwhu wkh lpsxovh lq doo wkh frxqwulhv1 Wkhvh duh
jhqhudo lqglfdwlrqv ri d frqwudfwlrqdu| prqhwdu| srolf| vwdqfh1
Krz gr sulfhv uhvsrqgB Erwk frqvxphu sulfhv dqg krxvh sulfhv jr grzq/ zlwk vrph h{0
fhswlrq1 Iru lqvwdqfh/ frqvxphu sulfhv duh deryh wkh edvholqh iru rqh |hdu lq Xqlwhg Nlqjgrp/
Jhupdq| dqg Vzhghq1 Lq X1N1 dqg Vzhghq wklv sdwwhuq lv sodxvleoh/ dv yduldeoh udwh pruwjdjh
frvwv kdyh d odujh zhljkw lq krxvhkrog exgjhwv/ dv zhoo dv rq phdvxuhg lq dwlrq> iru Jhupdq|
wkh lqlwldo lqfuhdvh pljkw eh gxh wr wkh idfw wkdw sduw ri wkh lqqrydwlrq lq wkh lqwhuhvw udwh
fdswxuhv vrph uhvlgxdo v|vwhpdwlf uhvsrqvh wr xqdffrxqwhg glvwxuedqfhv jhqhudwlqj lq dwlrqdu|
suhvvxuhv631
\hw wkh vkruw uxq uhvsrqvh lq krxvh sulfhv lv pxfk pruh surqrxqfhg/ dqg uhdo krxvh sulfhv
vljqlfdqwo| ghfuhdvh lq yluwxdoo| doo wkh frxqwulhv1 D fruroodu| ri wklv lv wkdw krxvh sulfh lq dwlrq
lv pruh vhqvlwlyh wkdq frqvxphu sulfh lq dwlrq wr d prqhwdu| lqqrydwlrq1
Wkhuh duh pdq|
jhqhudo uhdvrqv wkdw pljkw mxvwli| wklv uhvxow/ ri frxuvh/ dqg L ghihu d glvfxvvlrq ri wklv wr wkh
qh{w vxevhfwlrq1 Lq zkdw iroorzv/ L wu| wr vhh zkhwkhu wkh glhuhqw uhvsrqvhv ri krxvh sulfhv fdq
eh mxvwlhg e| orrnlqj dw wkh glhuhqw krxvlqj pdunhwv lq wkh frxqwulhv dqdo|vhg dqg zkhwkhu
dqg krz wkhvh glhuhqfhv pljkw sod| d uroh lq wkh wudqvplvvlrq phfkdqlvp1
Wr eh fohdu/ d gluhfw frpsdulvrq ri wkh vwdqfh ri prqhwdu| srolf| lv pdgh kdug e| wkh idfw
wkdw d w|slfdo vkrfn ydulhv lq vl}h/ vkdsh dqg gxudwlrq dfurvv frxqwulhv/ dv zhoo dv e| wkh glhuhqw
vdpsoh vl}hv641 Khuh L suhvhqw wzr vhwv ri frpsdudwlyh uhvsrqvhv= lq wkh uvw rqh +Iljxuh 43, wkh
frqwudfwlrq lv rqh vwdqgdug huuru lq vl}h> lq wkh vhfrqg +Iljxuh 44,/ L uhvfdoh wkh lqlwldo lpsdfw
rq wkh lqwhuhvw udwh wr eh wkh vdph +83 edvlv srlqwv, iru doo wkh frxqwulhv1
5< Dowkrxjk uhdo edodqfhv whpsrudulo| lqfuhdvh lq Iudqfh dqg Xqlwhg Nlqjgrp/ wkh lpsolhg hhfw rq qrplqdo
edodqfhv lv xqdpeljxrxvo| qhjdwlyh1
63 Wklv lv d frpprq h{sodqdwlrq lq wkh olwhudwxuh wr mxvwli| wkh zhoo nqrzq sulfh sx}}oh/ l1h1 wkh idfw wkdw diwhu
d frqwudfwlrqdu| prqhwdu| srolf| vkrfn frqvxphu sulfh lqlwldoo| lqfuhdvh udwkhu wkdq ghfuhdvh +h1j1/ Vlpv/ 4<<5,1
64 Zkhq lw frphv wr frpsdudwlyh YDU vwxglhv/ wkh hylghqfh lv qrw yhu| frqfoxvlyh dv idu dv wkh lpsdfw ri
prqhwdu| dqg rwkhu vkrfnv lv frqfhuqhg1 Wdeohv E14 dqg E15 lq wkh Dsshqgl{ E surylgh d dyrxu ri wkh xqfhuwdlqw|
lqyroyhg lq hvwlpdwlqj +dqg frpsdulqj, wkh uhvsrqvhv ri vrph Hxurshdq hfrqrplhv wr dq lghqwlhg prqhwdu| srolf|
vkrfn1 Dowkrxjk wkh hvwlpdwhv uhihu wr glhuhqw wlph vsdqv dqg wr vkrfnv ri glhuhqw pdjqlwxgh/ d txlfn jodqfh dw
wkhvh Wdeohv vkrzv wkdw lw vhhpv dw ohdvw kd}dugrxv wr udqn wkh hfrqrplhv dffruglqj wr wkh vl}h ri wkhlu uhdfwlrq
wr d prqhwdu| h{sdqvlrq +zkhwkhu lw lv dq lqfuhdvh lq vrph prqhwdu| djjuhjdwh ru d ghfuhdvh lq wkh vkruw0whup
lqwhuhvw udwh,1
 ECB Working Paper No 18 G April 2000                                                                                                              25
Rqfh wkh lqwhuhvw udwh lqfuhdvh lv uhvfdohg +Iljxuh 44,/ lw vhhpv wkdw Lwdo| dqg Xqlwhg Nlqj0
grp h{shulhqfh eljjhvw krxvh sulfh xfwxdwlrqv zkhuhdv Iudqfh dqg Jhupdq| duh suredeo| dw
wkh rwkhu h{wuhph +lq Jhupdq|/ uhdo krxvh sulfhv lqlwldoo| lqfuhdvh diwhu wkh frqwudfwlrq,/ zlwk
Vsdlq dqg Vzhghq vrphzkhuh lq ehwzhhq1 Wr jlyh vrph txdqwlwdwlyh dyrxu/ vl{ txduwhuv diwhu
wkh prqhwdu| wljkwhqlqj qrplqdo krxvh sulfhv duh uhvshfwlyho| 416 dqg 418 shu fhqw ehorz wkh
edvholqh lq Lwdo| dqg XN/ zkhuhdv wkh| duh 319 dqg 314 shu fhqw ehorz lq Iudqfh dqg Jhupdq|1
Uhdo krxvh sulfhv/ ri frxuvh/ idoo d elw ohvv/ jlyhq wkh prghudwh ghfuhdvh lq frqvxphu sulfhv1 Lw
lv gl!fxow wr vd| zkhwkhu wkhvh uhvsrqvhv duh vljqlfdqwo| glhuhqw dfurvv frxqwulhv1 Krzhyhu/
diwhu vl{ txduwhuv wkh orzhu frqghqfh edqg +rqh v1h1, iru wkh idoo lq Jhupdq| lv deryh wkh kljkhu
rqh iru Xqlwhg Nlqjgrp/ wkxv vxjjhvwlqj wkdw wkhuh duh vrph vljqlfdqw glhuhqfhv ehwzhhq wkh
prvw h{wuhph fdvhv1
Wkh glhuhqw uhvsrqvhv fdq eh mxvwlhg dv iroorzv= frxqwulhv zlwk orz wudqvdfwlrq frvwv/ kljk
ordq0wr0ydoxh udwlrv/ d odujh rzqhu0rffxslhg vhfwru dqg d odujh sursruwlrq ri yduldeoh0lqwhuhvw
pruwjdjh ordqv vkrxog h{shulhqfh uhodwlyho| kljk uhdo krxvh sulfh yrodwlolw| dqg d juhdw uroh iru
krxvlqj lq wkh lqwhuhvw udwh wudqvplvvlrq phfkdqlvp +vhh PPV/ 4<<;,1 Wkh hylghqfh khuh vhhpv
wr frqup wklv frqmhfwxuh= wkh XN lv rqh ri wkh HX frxqwulhv zlwk orzhvw wudqvdfwlrq frvwv dv
d shufhqwdjh ri sulfh +5(,/ zlwk pruwjdjh udwhv lq prvw ri wkh fdvhv uhylhzdeoh ru uhqhjrwldeoh/
yhu| kljk ordq0wr0ydoxh udwlrv/ dqg d kljk rzqhu rffxslhg whqxuh udwh dv d shufhqwdjh ri wkh
krxvlqj vwrfn1 Lq Lwdo|/ dowkrxjk prvw ri wkh ixqglqj iru krxvh sxufkdvh frphv iurp rzq ixqgv/
wkh lpsdfw ri d prqhwdu| frqwudfwlrq lv olnho| wr dhfw krxvhkrogv zkr duh vwloo uhsd|lqj wkhlu
pruwjdjh= Eduudq/ Frxghuw dqg Prmrq +4<<9, uhsruw wkdw :8 shu fhqw ri pruwjdjh fuhglw lv dw
udwhv wkdw duh gluhfwo| lqgh{hg rq wkh vkruw whup udwh1 Krzhyhu/ ghvslwh wkh elj uhdfwlrq lq whupv
ri krxvh sulfh yrodwlolw|/ wkh uhvsrqvh lq rxwsxw lv qrw yhu| vwurqj= ryhudoo/ wkdw vxjjhvwv wkdw lq
Lwdo| krxvh sulfhv/ dowkrxjk yhu| yrodwloh/ gr qrw sod| d elj uroh lq wkh wudqvplvvlrq phfkdqlvp1
Wkh Xqlwhg Nlqjgrp lv wkh frxqwu| wkdw lv dhfwhg prvw li zh xvh dv d phwulf iru wkh lpsdfw
ri wkh vkrfn wkh frpelqhg hhfw rq rxwsxw dqg uhdo krxvh sulfhv1 Wr wklv dlp/ Iljxuh 45 vkrzv
d sorw ri wkh uhvsrqvh ri JGS dqg uhdo krxvh sulfhv wr d 83 edvlv srlqw xqh{shfwhg lqfuhdvh lq
wkh vkruw whup udwh1
Jhupdq| dqg Iudqfh +dqg/ wr vrph h{whqw/ Vsdlq/ dowkrxjk wkh vdpsoh fryhuv rqo| d vpdoo
shulrg vwduwlqj lq 4<;:, whqg wr eh dw wkh rssrvlwh vlgh ri wkh vshfwuxp1 Dv dujxhg e| PPV
+4<<;,/ lq Jhupdq| whqxuh udwhv duh uhodwlyho| orz dqg wudqvdfwlrq frvwv dv d iudfwlrq ri wkh sulfh
duh uhodwlyho| kljk1 Dovr/ wkh lqlwldo frqwudfwlrq pljkw vljqdo d fuhgleoh glvlq dwlrq srolf| e|
wkh fhqwudo edqn lq wkh ixwxuh/ wkxv orzhulqj h{shfwhg lq dwlrq dqg ixwxuh udwhv1 Vxusulvlqjo|/
wkrxjk/ wkh uhvsrqvh ri rxwsxw lv yhu| vwurqj/ dowkrxjk lw pljkw eh d frqvhtxhqfh ri wkh lpsrvhg
26                                                                                                          ECB Working Paper No 18 G April 2000
qrupdolvdwlrq1 Iru d frxqwu| vxfk dv Jhupdq| zlwk d orqj klvwru| ri orz dqg vwdeoh lq dwlrq
dqg lqwhuhvw udwhv dq lqfuhdvh ri wkh lqwhuhvw udwh ri 83 edvlv srlqwv lv d eljjhu glvwxuedqfh lq
uhodwlyh whupv/ dv Iljxuh 43/ vkrzlqj rqh0vwdqgdug ghyldwlrq lqqrydwlrqv/ vkrzv1
Lqwhuhvwlqjo|/ lq Iudqfh qrplqdo krxvh sulfhv vhhp wr mxps lpphgldwho| wr 0 dqg hyhq wr
ryhuvkrrw 0 wkhlu qhz orqj0uxq htxloleulxp ohyho/ dqg wkh lpsolhg g|qdplfv lq uhdo krxvh sulfhv
vhhp doo wr vwhp iurp wkh vorz dgmxvwphqw ri frqvxphu sulfhv1 Ryhudoo/ wkh lpsdfw rq krxvh
sulfhv ri wkh frqwudfwlrq lq Iudqfh lv qrw yhu| vwurqj/ dqg diwhu derxw 9 txduwhuv uhdo krxvh sulfhv
duh edfn wr wkh edvholqh diwhu wkh lqlwldo idoo1 Wkh uhvxow lv frqvlvwhqw zlwk hylghqfh suhvhqwhg lq
Eduudq/ Frxghuw dqg Prmrq +4<<9,/ zkr uhsruw wkdw lq Iudqfh doprvw <8 shu fhqw ri pruwjdjh
fuhglw lv rq frpsohwho| {hg udwhv1 Wkhuhiruh/ rqh zrxog h{shfw wkh lpsdfw ri wkh frqwudfwlrq wr
dhfw rqo| wkrvh zkr duh jrlqj wr ex| d krxvh/ udwkhu wkdq douhdg| lqghewhg krxvhkrogv/ zlwk
vpdoo zhdowk hhfwv iru wklv jurxs1
Wkh uhvsrqvhv iru Vsdlq dqg Vzhghq djdlq surylgh jhqhudo hylghqfh ri d prqhwdu| frqwudf0
wlrq1
Wzr uhpdunv duh lq rughu1 Wkh uvw lv uhodwhg wr wkh gl!fxow| ri frpsdulqj glhuhqw prqhwdu|
lqqrydwlrqv dfurvv frxqwulhv/ hvshfldoo| jlyhq wkdw wkh vkrfnv wdnh glhuhqw vkdshv dqg vl}hv lq
wkh revhuyhg sdwwhuq ri wkh lqwhuhvw udwh dqg qrplqdo prqh|/ wkh w|slfdo vkruw whup lqwhuphgldwh
wdujhwv wkh prqhwdu| srolf| dxwkrulw|1 Khuh L kdyh vkrzq wkh uhvsrqvhv kdylqj dqg qrw kdylqj
qrupdolvhg iru wkh lqlwldo lpsdfw rq wkh qrplqdo lqwhuhvw udwh651 Wkh uvw surfhgxuh +qrupdolvlqj,
kdv wkh yluwxh ri surylglqj d xvhixo ehqfkpdun li zh wklqn wkdw irxu ri wkhvh frxqwulhv duh qrz
xqghu d frpprq prqhwdu| srolf|> wkh vhfrqg +qrw qrupdol}lqj, frpsduhv lq doo wkh frxqwulhv d
w|slfdo ehqfkpdun vkrfn ryhu wkh shulrg lq txhvwlrq1
Wkh vhfrqg uhodwhv wr wkh revhuyhg g|qdplfv lq wkh krxvh sulfhv iroorzlqj d vkrfn1
D
vwdqgdug0prqhwdulvw prgho ri wkh krxvlqj pdunhw +dv ghvfulehg lq Srwhued/ 4<;7 ru Phow}hu/
4<<8, zrxog suhglfw wkdw wkhuh vkrxog eh d mxps iroorzhg e| d vprrwk dgmxvwphqw ri wkh dvvhw
sulfh wrzdugv wkh htxloleulxp1
Wkh hylghqfh khuh vkrzv wkdw wkh wlplqj ri wkh uhvsrqvh lq
uhdo krxvh sulfhv pdwfkhv wkdw ri rxwsxw/ zlwk d shdn lq uhdo krxvh sulfhv rffxuulqj hlwkhu
frqwhpsrudqhrxvo| ru d ihz txduwhuv ehiruh wkdw ri rxwsxw> dqg wkh dgmxvwphqw ri krxvh sulfhv
wr wkh qhz vwhdg| vwdwh wdnhv vhyhudo |hduv/ zlwk krxvh sulfhv idoolqj lq uhdo whupv iru derxw
rqh ru wzr |hduv ehiruh uhyhuwlqj wr wkh edvholqh1 Rqh zd| wr lqwhusuhw wklv hylghqfh lv wkdw
vrph eurdg fuhglw fkdqqho pljkw eh lq dfwlrq wrr= zlwk ghsuhvvhg dvvhw sulfhv/ frqvxpswlrq
65 Qrupdolvlqj iru wkh lqlwldo lpsdfw rq wkh lqwhuhvw udwh lv pruh sdflf li rqo| xqdqwlflsdwhg prqhwdu| srolf|
pdwwhuv +wkh vwdqgdug YDU lqwhusuhwdwlrq,1 Lq wklv fdvh zkdw kdsshqv wr wkh sdwk ri lqwhuhvw udwh dqg prqh|
diwhu d vkrfn lv luuhohydqw iru wkh uhvsrqvh ri wkh uhdo yduldeohv1 Li dqwlflsdwhg srolf| pdwwhuv wrr/ qrw rqo| wkh
lqlwldo lpsdfw exw dovr wkh wlph sdwk ri wkh srolf| yduldeohv duh lpsruwdqw lq ghwhuplqlqj wkh uhvsrqvh ri wkh uhdo
yduldeohv +wklv lpsruwdqw glvwlqfwlrq lv gxh wr Frfkudqh/ 4<<;> vhh dovr Ohlfkwhu dqg Zdovk/ 4<<</ iru d glvfxvvlrq
rq wkh Hxurshdq fdvh,1
 ECB Working Paper No 18 G April 2000                                                                                                         27
dqg lqyhvwphqw frxog vxhu wrr/ dqg wkh hhfwv pljkw uhlqirufh hdfk rwkhu/ dv lq wkh vwdqgdug
Nl|rwdnl0Prruh +4<<:, prgho1
Ryhudoo/ wkh uhvsrqvhv fdqqrw fohduo| khos lq glvwlqjxlvklqj ehwzhhq glhuhqw ylhzv ri wkh
prqhwdu| wudqvplvvlrq phfkdqlvp= exw lq wkh frqwh{w ri wkh suhvhqw prgho/ wkh hvwlpdwhg
g|qdplfv ri krxvh sulfhv vhhp wr klqw vrph uroh iru krxvlqj dqg fuhglw lqvwlwxwlrqv lq wkh glhuhqw
uhvsrqvh ri wkh krxvh sulfhv/ dqg iru krxvh sulfhv lq wxuq lq wkh sursdjdwlrq phfkdqlvp1 Wklv
lv frqvlvwhqw erwk d eurdg fuhglw fkdqqho ylhz ri wkh wudqvplvvlrq phfkdqlvp dqg zlwk d
prqhwdulvw ylhz/ dv ghvfulehg lq Phow}hu +4<<8,1
Zk| vkrxog krxvh sulfhv uhvsrqg pruh wkdq frqvxphu sulfhv wr d prqhwdu|
frqwudfwlrqB
Zkhq srolf| lv wljkwhqhg wkurxjk d ghfuhdvh lq uhvhuyh surylvlrq/ lqwhuhvw udwhv
ulvh1 Dv Pruulv dqg Vhoorq +4<<8, h{sodlq/ d ulvh lq lqwhuhvw udwhv ohdgv wr d uhgxfwlrq lq vshqglqj
lq sduwlfxodu lq lqwhuhvw0vhqvlwlyh vhfwruv ri wkh hfrqrp|/ vxfk dv sxufkdvhv ri gxudeoh jrrgv dqg
krxvlqj1 Wklv uhvxow frxog dsshdu dw uvw vljkw vxusulvlqj/ dv wkhuh vkrxog eh vrph d sulrul
uhdvrqv wr eholhyh wkdw wkh ghflvlrq wr ex| d krxvh ghshqgv pruh rq d orqj0whup lqwhuhvw udwh1
Lq sulqflsoh/ li fhqwudo edqn ixwxuh dfwlrqv diwhu wkh lqlwldo vkrfn duh shuihfwo| dqwlflsdwhg/ wkh
orqj0whup udwh vkrxog udlvh e| ohvv wkdq wkh vkruw udwh +lw frxog hyhq idoo/ li wkh prqhwdu|
wljkwhqlqj lv ylhzhg dv fuhgleoh dqg hhfwlyh,1 Ghvslwh wkdw/ wr wkh h{whqw wkdw pruwjdjh udwhv
+dw ohdvw rq qhz krxvlqj ordqv, ru rwkhu whupv ri wkh pruwjdjh frqwudfw +iru lqvwdqfh/ wkh dprxqw
ri grzqsd|phqw uhtxluhg, ghshqg dw ohdvw lq sduw rq wkh fxuuhqw vwdqfh ri wkh prqhwdu| srolf|/
rqh fdq h{shfw d xvhu frvw hhfw wr rshudwh dqg uhgxfh uhodwlyh ghpdqg iru krxvlqj661
Dg dgglwlrqdo fkdqqho wkurxjk zklfk prqhwdu| srolf| frxog lq xhqfh krxvh sulfhv lv wkh rqh
wkdw vhhv lw zrunlqj wkurxjk fuhglw +ohw xv fdoo lw fuhglw vxsso| hhfw,1 Li prqhwdu| srolf| zrunv
e| gluhfwo| frqvwudlqlqj wkh delolw| ri edqnv wr pdnh qhz ordqv/ pdnlqj fuhglw ohvv dydlodeoh
wr eruurzhuv zkr duh ghshqghqw rq edqn qdqflqj/ wklv dgglwlrqdo hhfw pljkw uhlqirufh dqg
dpsoli| wkh lqlwldo rqh wkdw rshudwhv wkurxjk wkh wudglwlrqdo xvhu frvw 0 ghpdqg vlgh fkdqqho
+iru lqvwdqfh/ vhh Ndvk|ds/ Vwhlq dqg Zlofr{/ 4<<6,1
Ixuwkhupruh/ wkh eljjhu uhvsrqvh lq krxvh sulfhv lv dovr frqvlvwhqw zlwk wkh idfw wkdw wkh
krxvlqj vxsso| fxuyh +fdoo lw lqhodvwlf krxvlqj vxsso| hhfw, lv vwhhshu wkdq wkh vxsso| fxuyh iru
doo rwkhu jrrgv lq wkh vkruw uxq671
66 Ehuqdqnh dqg Jhuwohu +4<<8, vkrz wkdw uhvlghqwldo lqyhvwphqw lv pxfk pruh vhqvleoh wr prqhwdu| wljkwhqlqj
wkdq rwkhu frpsrqhqwv ri vshqglqj1
67 Wkhuh lv dovr dqrwkhu uhdvrq zk| sulfh yrodwlolw| frxog dulvh lq wkh krxvlqj pdunhw= zkhq krxvh sulfhv duh
ulvlqj/ ghpdqg dsshduv wr ulvh/ dqg zkhq sulfhv duh idoolqj wkh frqyhuvh dsshduv wr eh wkh fdvh1 Lq rwkhu zrugv/
qrw rqo| pljkw wkh vxsso| fxuyh eh lqhodvwlf/ exw dovr wkh ghpdqg fxuyh pljkw eh xszdug vorslqj1
28                                                                                                                                                 ECB Working Paper No 18 G April 2000
Ghpdqg vkrfn
Wkh vhfrqg wudqvlwru| vkrfn uhvxowv lq vkruw0whup rxwsxw hhfwv zlwk frq0
vxphu sulfhv {hg lq wkh lpsdfw shulrg1 Iroorzlqj Furzghu/ Krpdq dqg Udvfkh +4<<<, dqg
Jhuodfk dqg Vphwv +4<<8,/ lw lv srvvleoh wr odeho wklv glvwxuedqfh wudqvlwru| ghpdqg vkrfn
vlqfh lw holflwv srvlwlyh rxwsxw dqg sulfh uhvsrqvhv dqg gxh wr lwv wudqvlwru| lpsulqw rq wkh uhdo
yduldeohv lq wkh v|vwhp1 \hw wklv grhv qrw lghqwli| dq| sduwlfxodu vrxufh ri djjuhjdwh ghpdqg
lqqrydwlrq1 Wkh idfw wkdw wkh uhvsrqvhv +vkrzq lq urz 7 ri Iljxuhv 5 wr : dqg/ rq d frpsdudwlyh
edvlv/ lq Iljxuh 46, glvsod| dq lqfuhdvh lq uhdo krxvh sulfhv wkdw shdnv diwhu derxw 5 |hduv dqg
glhv rxw rqo| diwhu 829 |hduv lv frqvlvwhqw zlwk wkh lghd wkdw wkh vkrfn pljkw eh wkh rxwfrph ri=
d, whpsrudu| wd{ lqfhqwlyhv wkdw jlyh dq dgydqwdjh wr ex| krxvhv>
e, lqfuhdvh lq krxvlqj ghpdqg vwhpplqj iurp rswlplvwlf frqvxphu ru lqyhvwru h{shfwdwlrqv/
wkdw dovr wudqvodwhv rqwr wkh zlghu hfrqrp|>
f, dq lqfuhdvh lq djjuhjdwh ghpdqg ghulylqj iurp rwkhu vrxufhv +vd|/ ghydoxdwlrq ri qdwlrqdo
fxuuhqf| xqghu d {hg h{fkdqjh udwh uhjlph, wkdw wudqvodwhv lqwr krxvh sulfh lq dwlrq zlwk vrph
odj1
Wkh uhvxowv lq Iljxuh 46 duh frqvlvwhqw zlwk d xszdug vkliw lq wkh LV fxuyh ri wkh hfrqrp|1
Qrplqdo dqg uhdo lqwhuhvw udwhv jr xs1 Rxwsxw ulvhv surwudfwhgo|1 Lq dwlrq jrhv xs wrr/ h{fhsw lq
Jhupdq|1 Uhdo krxvh sulfh lqfuhdvhv duh sduwlfxoduo| vwurqj lq XN dqg Vzhghq1 Wkh lqfuhdvh/
zkrvh wlplqj forvho| pdwfkhv wkdw ri rxwsxw/ lv surwudfwhg iru vhyhudo |hduv/ djdlq ohqglqj
vxssruw wr vrph eurdg fuhglw fkdqqho wkhru|1
Lq dwlrq vkrfn
Lq pdq| frxqwulhv/ wkh wd{ v|vwhp lv vxfk wkdw kljkhu lq dwlrq udwhv uhgxfh
krphrzqhuv* xvhu frvw ehfdxvh zkloh qrplqdo pruwjdjh lqwhuhvw sd|phqwv duh wd{ ghgxfwleoh/
wkh fdslwdo jdlqv iurp krxvh dssuhfldwlrq duh hvvhqwldoo| xqwd{hg1 D wudqvlwru| lq dwlrq vkrfn
vkrxog wkhuhiruh lqfuhdvh ghpdqg iru krxvhv/ wkxv udlvlqj wkhlu sulfh1 Rq wkh rwkhu kdqg/ dv
vkrzq lq Iljxuh 47 +dqg urz 8 ri Iljxuhv 5 wr :,/ lq dwlrq lqfuhdvhv dovr gulyh hqgrjhqrxv
pryhphqwv lq rxwsxw dqg lqwhuhvw udwh wkdw pljkw frxqwhuedodqfh wkh hhfw1 Iru lqvwdqfh/ lq doo
frxqwulhv exw Iudqfh rxwsxw jrhv whpsrudulo| grzq1
Wkh slfwxuh lv pdgh frpsolfdwhg e| wkh idfw wkdw wklv glvwxuedqfh pljkw lq uhdolw| phdq dw
ohdvw wkuhh wklqjv= 4, lqfuhdvh lq zruog frpprglw| sulfhv> 5, lpsruwhg lq dwlrq iroorzlqj ghydo0
xdwlrq ri wkh grphvwlf fxuuhqf|> 6, whpsrudu| qhjdwlyh vxsso| vkrfn1 Wkh vhfrqg lqwhusuhwdwlrq
lv frqvlvwhqw zlwk dq lqfuhdvh lq rxwsxw/ dv wkh lpsxovh uhvsrqvhv iru Iudqfh vkrz1
Lw lv dovr lqwhuhvwlqj wr qrwh wkh olqn ehwzhhq uhdo udwhv dqg krxvh sulfhv= zkhuh wkh vkrfn
ohdgv wr kljkhu yrodwlolw| lq wkh uhdo lqwhuhvw udwh/ dv lq XN iru lqvwdqfh/ zh dovr revhuyh d
ghfuhdvh lq uhdo krxvh sulfhv1
Dv iru wkh shupdqhqw qrplqdo glvwxuedqfh/ lw lv lqdgylvdeoh wrr sxw wr pxfk vwuxfwxudo
 ECB Working Paper No 18 G April 2000                                                                                                         29
hpskdvlv rq wklv vkrfn/ wkdw pljkw lqghhg eh d plvfhoodqhrxv ri glvwxuedqfhv frplqj iurp
pdq| glhuhqw vrxufhv1
815 Yduldqfh ghfrpsrvlwlrqv
Xs wr qrz wkh sdshu kdv irfxvhg rq dqvzhulqj wkh txhvwlrq= zkdw duh wkh g|qdplf hhfwv
ri vxsso|/ ghpdqg/ qrplqdo/ lq dwlrq dqg lq sduwlfxodu prqhwdu| vkrfnv rq krxvh sulfhvB D
uhodwhg exw glhuhqw txhvwlrq lv= lq zklfk sursruwlrq gr wkh glhuhqw lqqrydwlrqv frqwulexwh
wr wkh yrodwlolw| ri krxvh sulfhv dqg rwkhu pdfurhfrqrplf yduldeohvB Dqvzhulqj wklv txhvwlrq
lv lpsruwdqw/ ehfdxvh lw fdq jlyh d dyrxu ri zkdw duh wkh pdlq idfwruv gulylqj krxvh sulfh
 xfwxdwlrqv dw glhuhqw krul}rqv1
Iljxuh 48 sorwv wkh iudfwlrq ri wkh n0vwhs dkhdg iruhfdvw huuru yduldqfh iru uhdo krxvh sulfhv
h{sodlqhg e| wkh glhuhqw vkrfnv1 Iru uhdvrqv ri vsdfh/ L gr qrw uhsruw yduldqfh ghfrpsrvlwlrqv
iru wkh rwkhu yduldeohv681
Zkloh wkh uhvxowv kljkoljkw wkdw qrw pxfk ri yduldqfh ri rxwsxw +durxqg 48( ru ohvv, lv
dwwulexwdeoh wr prqhwdu| lqqrydwlrqv/ wkh| vhhp wr klqw vrph uroh iru prqhwdu| idfwruv lq
h{sodlqlqj krxvh sulfhv yduldelolw|/ dw ohdvw ryhu wkh vkruw uxq1 Diwhu/ vd|/ 9 txduwhuv/ d iudfwlrq
wkdw jrhv iurp 8( wr 73( ri wkh yrodwlolw| ri uhdo krxvh sulfhv frphv iurp wkh srolf| vkrfn
phdvxuh= wklv iudfwlrq lv vpdoohvw lq Jhupdq|1
Ghpdqg vkrfnv sod| d pdmru uroh ryhu wkh vkruw uxq wrr= zkhwkhu wkh| uhsuhvhqw vlpso|
djjuhjdwh ghpdqg 0 vd|/ vkliwv lq wkh LV fxuyh 0 ru krxvlqj pdunhwv vshflf glvwxuedqfhv +hyhq
exeeohv ixhoohg e| vhoi0ixooolqj h{shfwdwlrqv, lv lq dq| fdvh d txhvwlrq wkdw lw lv gl!fxow wr
dqvzhu lq wklv iudphzrun1 Iudqfh/ Vzhghq dqg XN duh/ lq wklv uhvshfw/ wkh frxqwulhv zkhuh
ghpdqg lqqrydwlrqv sod| d pdmru uroh lq wkh vkruw uxq1
Wkh XN uhvxow lv sduwlfxoduo| vwulnlqj 0 93( ri yrodwlolw| lq krxvh sulfhv frphv iurp wkh
ghpdqg vkrfn/ hyhq dw d 43 |hduv krul}rq$ 01 Wklv lv suredeo| lqgluhfw frqupdwlrq ri wkh
idfw wkdw lq d +doohjhgo|, vshfxodwlyh pdunhw/ vxfk dv wkh XN rqh69/ wudqvlwru| idfwruv sod| dq
lpsruwdqw uroh lq ghwhuplqlqj krxvh sulfh xfwxdwlrqv1 Dw wkh rwkhu vlgh ri wkh vshfwuxp lv
Jhupdq|1 Prvw ri wkh xqiruhfdvw yduldelolw| lq krxvh sulfhv iru Jhupdq| frphv iurp vxsso|
idfwruv1
Qrw vxusulvlqjo|/ lq dgglwlrq/ wkh yduldelolw| ri qrplqdo lqwhuhvw udwhv dqg prqh| edodqfhv
lv lq odujh sduw gxh wr prqhwdu| idfwruv1 Ri frxuvh/ wkh dvvxpswlrqv pdgh lq wkh lghqwlfdwlrq
vfkhph lpso| e| frqvwuxfwlrq wkdw wkh wzr shupdqhqw vkrfnv zloo grplqdwh wkh wudqvlwru| rqhv
68 Uhvxowv duh dydlodeoh iurp wkh dxwkru xsrq uhtxhvw1
69 Ohylq dqg Zuljkw +4<<:, suhvhqw vrph hylghqfh ri wkh surfhvv ri vshfxodwlrq dv d srvvleoh ghwhuplqdqw ri
krxvh sulfhv lq XN0zlgh krxvlqj pdunhw1
30                                                                                                          ECB Working Paper No 18 G April 2000  
dv wkh iruhfdvw krul}rq jurzv odujhu1
9 Dq lqirupdo lqwhusuhwdwlrq ri krxvh sulfh pryhphqwv
Iljxuhv 49 wr 54 surylgh iru hdfk frxqwu| wkh sorwv ri orj ri uhdo krxvh sulfhv6:/ lq dwlrq/ lqwhuhvw
udwhv dqg orj ri rxwsxw lq wkh uvw urz/ dqg hvwlpdwhv ri wkh yh vwuxfwxudo vkrfnv lq wkh vhfrqg1
Wr pdnh wkh judskv hdvlhu wr lqwhusuhw/ L frqvwuxfw 5 |hdu prylqj dyhudjhv iru hdfk ri wkh
rwkhuzlvh xqfruuhodwhg glvwxuedqfhv/ vr wkdw lw lv hdvlhu wr lghqwli| shulrgv lq zklfk vrph ri
wkhp zhuh sod|lqj d surplqhqw uroh6;1 L dovr irfxv rqo| rq vrph vshflf/ uhohydqw shulrgv ri
vljqlfdqw krxvh sulfhv pryhphqwv iru hdfk frxqwu|1 Wkh ryhudoo slfwxuh wkdw hphujhv lv wkdw qr
errp fdq eh hdvlo| dvvrfldwhg zlwk d vlqjoh vrxufh ri pdfurhfrqrplf xfwxdwlrqv1 Hdfk pdmru
yduldwlrq lq krxvh sulfhv dsshduv wr kdyh ehhq gulyhq e| d frpelqdwlrq ri idfwruv sxvklqj lq wkh
vdph gluhfwlrq6<1
IUDQFH
Iudqfh +Iljxuh 49, kdg d vljqlfdqw errp gxulqj wkh |hdu 4<;3/ zlwk sulfhv shdnlqj
dw wkh ehjlqqlqj ri wkh 4<;4 dqg idoolqj e| 48( lq uhdo whupv lq wkh iroorzlqj wzr |hduv> d vlplodu
surfhvv ri errp0exvw rffxuuhg iurp 4<;8 wr 4<;< +sulfhv shdnhg dw wkh hqg ri 4<;:,1 Diwhu d
shdn dw wkh ehjlqqlqj ri 4<<4/ sulfhv kdg idoohq lq uhdo whupv e| derxw 58( dw wkh ehjlqqlqj
ri |hdu 4<<:1 Ghpdqg vkrfnv vhhp wr kdyh sod|hg dq lpsruwdqw uroh lq gulylqj krxvh sulfh
 xfwxdwlrqv/ wrjhwkhu zlwk rwkhu wudqvlwru| idfwruv1 Wkh 4<;8 0 4<;: errp iroorzhg d shulrg
ri srvlwlyh vxsso| vkrfnv dqg h{sdqvlrqdu| prqhwdu| srolf|1 Prqh| dqg fuhglw jurzwk zhuh
ulvlqj +wkdqnv wr derolwlrq ri fuhglw frqwuro phdvxuhv nqrzq dv hqfdguhphqw gx fuhglw= vhh
Klfnrn dqg Rvohu/ 4<<7,1 Lqvwhdg/ wkh jurzwk ri sulfhv iurp 4<;< wr 4<<4 vhhp pruh gxh wr
ghpdqg vkrfnv= prqhwdu| srolf| dsshduv wr kdyh ehhq wljkw ryhu wkdw shulrg/ dqg pljkw kdyh
frqwulexwhg wr wkh idoo lq krxvh sulfhv rffxuuhg dw wkh ehjlqqlqj ri 4<<4 rqfh ghpdqg vwduwhg
wr vorz dqg wkh hfrqrp| hqwhuhg lqwr uhfhvvlrq1
JHUPDQ\
Wkh Jhupdq krxvh sulfh errp ri wkh odwh *;3v 0 zlwk wkh uhdo krxvh sulfh
lqgh{ xs 48( lq wkh 7 |hduv iurp 4<;9 wr 4<<3 +dv vkrzq lq Iljxuh 4:,/ exw pxfk eljjhu sulfh
lqfuhdvhv lq wkh elj flwlhv 0 vhhpv gxh lq sduwlfxodu wr lqfuhdvhv lq djjuhjdwh ghpdqg1 Vrph ri
wkhvh ghpdqg vkrfnv vhhp wr kdyh wkhlu urrwv qrw rqo| lq wkh errplqj hfrqrp| ri wkh odwh
6: Glvwdqfhv rq wkh yhuwlfdo d{lv fdq dffruglqjo| eh lqwhusuhwhg dv shufhqwdjh fkdqjhv1
6; Dv ylvxdo lqvshfwlrq ri wkh judskv vkrzv/ shulrgv ri kljkhu wkdq dyhudjh lqwhuhvw udwhv duh qrupdoo| dvvrfldwhg
zlwk frqwudfwlrqdu| prqhwdu| srolf|1 Dowkrxjk wklv srlqw lv lqwhuhvwlqj shu vh/ lw vkrxog qrw eh ryhuvwdwhg/ iru dw
ohdvw wzr uhdvrqv= 4, L lghqwli| prqhwdu| srolf| e| xvlqj vkruw dqg orqj uxq uhvwulfwlrqv/ vr wkhuh lv qrw d 4 wr 4
pdsslqj ehwzhhq kljk qrplqdo lqwhuhvw udwhv +ru orz prqh| vxsso|, dqg qhjdwlyh prqhwdu| vkrfnv> 5, prqhwdu|
+dqg rwkhu, vkrfnv rqo| uhihu wr xqh{shfwhg pryhphqwv lq wkh yduldeohv= wkhuhiruh v|vwhpdwlf prqhwdu| srolf|
wkdw udlvhv lqwhuhvw udwhv grhv qrw frqvwlwxwh d prqhwdu| vkrfn1
6< H{sdqvlrqdu| prqhwdu| srolflhv fruuhvsrqg wr wkh prqhwdu| vkrfn yduldeoh wdnlqj qhjdwlyh ydoxhv1
 ECB Working Paper No 18 G April 2000                                                                                                         31
*;3v/ exw dovr lq vshflf krxvlqj pdunhw hslvrghv wkdw pljkw kdyh lqfuhdvhg ghpdqg durxqg
wkdw shulrg1 Lq sduwlfxodu/ lq 4<;: fdslwdo jdlqv wd{ h{hpswlrqv zhuh lqwurgxfhg 0 surylghg wkh
surshuw| zdv qrw vrog zlwklq 5 |hduv ri sxufkdvh 0 dqg iurp 4<<4 lw zdv srvvleoh wr ghgxfw
lqwhuhvw sd|phqwv xs wr GP 45333 shu dqqxp iru wkh uvw wkuhh |hduv iurp wkh sxufkdvh ri d
qhzo|0exlow krxvh +Vplwk/ 4<<7,1 Lq dgglwlrq/ wkh elj flwlhv vdz/ dw wkh ehjlqqlqj ri wkh ghfdgh/
dq lq x{ ri zrunhuv iurp Hdvwhuq Jhupdq| wkdw errvwhg ghpdqg= Iudqnixuw lv uhsruwhg wr kdyh
vhhq d 77( sulfh ulvh lq 4<<30<4 +Wkh Hfrqrplvw/ 4<<5,1
LWDO\
Lwdo| kdv h{shulhqfhg juhdw yrodwlolw| lq krxvh sulfhv1 Wkh pdlq errpv dsshdu wr kdyh
rffxuuhg ehwzhhq 4<:< dqg 4<;4 dqg lq wkh odwh *;3v1 D vkdus gurs ehwzhhq 4<;5 dqg 4<;8/ zlwk
sulfhv idoolqj e| rqh0wklug lq uhdo whupv/ iroorzhg wkh uvw errp1 Diwhu wkh odwh *;3v lqfuhdvh/
sulfhv ihoo e| doprvw 48( lq uhdo whupv ehwzhhq 4<<6 dqg 4<<91 D orrn dw wkh vwuxfwxudo vkrfnv
lq Iljxuh 4; kljkoljkwv wkdw qrplqdo idfwruv dqg ghpdqg vkrfnv pljkw kdyh sod|hg d glvwlqfwlyh
uroh lq gulylqj krxvh sulfhv grzq iurp 4<<6 rqzdugv1 Lq sduwlfxodu/ dprqj wkh qhjdwlyh ghpdqg
vkrfnv/ d uroh frxog kdyh ehhq sod|hg e| srolflhv lq wkh odvw ghfdgh wkdw kdyh uhylvhg xszdug
wkh vfdo ydoxh +ydoruh fdwdvwdoh, ri wkh uhvlghqwldo surshuw|/ wkxv pdnlqj xqdwwudfwlyh wkh
lqyhvwphqw lq krxvlqj lq d shulrg ri hfrqrplf uhfhvvlrq/ orz krxvhkrog h{shfwdwlrqv derxw
ixwxuh lqfrphv/ dqg qhdu vdwxudwlrq ri wkh pdunhw/ zlwk whqxuh udwhv dv kljk dv :;(/ rqh ri wkh
kljkhvw ohyhov lq Hxursh +Fhqvlv/ 4<<9,1
VSDLQ
Srvlwlyh ghpdqg dqg vxsso| vkrfnv vhhp wr kdyh gulyhq wkh odwh *;3v errp +vhh Iljxuh
4<,1 Rqo| d vpdoo iudfwlrq ri wkh xfwxdwlrqv lq krxvh sulfhv vhhpv dwwulexwdeoh wr wkh prqhwdu|
srolf| vwdqfh/ zklfk zdv idluo| qhxwudo gxulqj wkdw shulrg1 Wkh ghfolqh lq uhdo krxvh sulfhv iru
prvw ri wkh *<3v vwduwhg zlwk wkh uhfhvvlrq lq 4<<5 dqg 4<<6 dqg zdv gulyhq e| erwk wljkwhu
prqhwdu| srolf| dqg qhjdwlyh ghpdqg vkrfnv1
VZHGHQ
Ghpdqg dqg prqhwdu| srolf| vkrfnv guryh wkh krxvlqj errp ri wkh odwh *;3v=
krxvh sulfhv zhqw xs 68( lq uhdo whupv ehwzhhq 4<;9 dqg 4<;</ dqg ihoo e| doprvw wkh vdph
dprxqw lq wkh |hduv iurp 4<<4 wr 4<<61 Orrvh vfdo srolf|/ gh0uhjxodwlrq ri wkh qdqfldo pdunhwv
+fhlolqjv rq edqn ohqglqj udwhv dqg txdqwlwdwlyh frqwurov rq edqn ordqv zhuh derolvkhg lq 4<;8,
dqg d wd{ v|vwhp wkdw hqfrxudjhg ghew0qdqfhg frqvxpswlrq vsxuuhg djjuhjdwh ghpdqg dqg
lqfuhdvhg dvvhw sulfhv1 Orrnlqj dw Iljxuh 53/ ghpdqg vkrfnv zhuh frqvlvwhqwo| srvlwlyh lq doo
|hduv xqwlo 4<<3/ zkhq d txlfno| ghhshqlqj uhfhvvlrq vhw lq1 Dv dujxhg e| Ehuj dqg Juùwwkhlp
+4<<:,/ wkh frpelqdwlrq ri dq lqwhuqdwlrqdo uhfhvvlrq/ d uhiruphg wd{ v|vwhp zklfk derolvkhg
lqyhvwphqw doorzdqfhv dqg idoolqj dvvhw sulfhv frqwulexwhg wr wkh vhyhulw| ri wkh grzqwxuq1
32                                                                                                                                                  ECB Working Paper No 18 G April 2000
XN
Ryhu wkh shulrg jrlqj iurp 4<:7 wr 4<<;/ wkh Xqlwhg Nlqjgrp kdv h{shulhqfhg wzr pdlq
krxvh sulfh errp0exvwv f|fohv/ wkh uvw iurp wkh 4<:; wr 4<;5/ wkh vhfrqg iurp 4<;6 wr 4<<51
Erwk f|fohv duh zlgho| grfxphqwhg dqg glvfxvvhg lq wkh olwhudwxuh +vhh iru lqvwdqfh Fxwohu/ 4<<8/
Kropdqv/ 4<<7/ dqg Fxuzhq/ 4<<:,1 Gxulqj wkh uvw +vpdoohu, f|foh/ krxvh sulfhv urvh lq uhdo
whupv e| 53(/ klw d shdn dw wkh hqg ri 4<:</ dqg wkhq ihoo e| 48(1 Lq wkh vhfrqg +eljjhu,
f|foh/ uhdo krxvh sulfhv urvh derxw 93(/ shdnhg lq 4<;</ dqg wkhq ihoo e| 7:(/ erwwrplqj
dw wkh hqg ri 4<<81
Orrnlqj dw Iljxuh 54/ wkh krxvh sulfh errp ri lq wkh vhfrqg kdoi ri
wkh *;3v vhhpv wr kdyh ehhq gulyhq e| d frpelqdwlrq ri wkuhh idfwruv= srvlwlyh vxsso| dqg
ghpdqg vkrfnv dqg h{sdqvlrqdu| prqhwdu| srolf|1 Wklv lv frqvlvwhqw zlwk wkh ylhz wkdw ulvlqj
krxvhkrog h{shfwdwlrqv derxw wkhlu ixwxuh lqfrphv/ srolflhv wr surprwh krxvlqj sxufkdvhv +vxfk
dv wkh dqqrxqfhphqw lq Pdufk 4<;; wkdw iurp Dxjxvw ri wkdw |hdu pruwjdjh wd{ uholhi zrxog eh
uhvwulfwhg wr Â63/333 shu uhvlghqfh uhjdugohvv ri wkh qxpehu ri eruurzhuv, dqg d orrvh prqhwdu|
srolf| wkdw iroorzhg wkh dssuhfldwlrq ri wkh srxqg iurp durxqg 4<;: doo sod|hg d uroh lq wkh
krxvlqj errp731
: Frqfoxvlrqv
Wklv sdshu kdv vkrzq wkdw wkh g|qdplfv ri krxvh sulfhv fdq eh ghdow zlwk xvlqj d wudfwdeoh
YDU iudphzrun lq d uhodwlyho| vwudljkwiruzdug zd|1 L kdyh ghyhorshg dqg hvwlpdwhg d vlpsoh
pdfurhfrqrphwulf prgho gulyhq e| yh h{rjhqrxv glvwxuedqfhv/ doo ri zklfk fdq srwhqwldoo|
kdyh hhfwv rq krxvh sulfh lq dwlrq1 Lq sduwlfxodu/ L kdyh vkrzq wkdw prqhwdu| srolf| vkrfnv 0
lghqwlhg xqghu wkh dvvxpswlrq wkdw wkh| gr qrw dhfw rxwsxw +dqg frqvxphu sulfh lq dwlrq,
lq wkh shulrg ri wkh vkrfn dqg lq wkh orqj uxq 0 fdq kdyh vhulrxv hhfwv rq krxvh sulfhv/ zklfk
pljkw lq wxuq sod| d uroh lq wkh sursdjdwlrq phfkdqlvp ri wkh vkrfnv1 Zkdw vhhpv vxssruwlyh
ri wkhvh qglqjv lv wkdw d vhw ri frpprq dqg vhqvleoh lghqwlfdwlrq dvvxpswlrqv |lhogv sodxvleoh
uhvxowv dv idu dv wkh lqwhuuhodwlrqvklsv ehwzhhq prqh|/ frqvxphu sulfhv dqg rxwsxw duh frqfhuqhg>
pruhryhu/ lw dggv d uhodwlyho| qhz slhfh ri hylghqfh/ vkrzlqj wkdw/ xqolnh frqvxphu sulfhv/ krxvh
sulfh lq dwlrq pljkw eh yhu| vhqvlwlyh wr wkh irufhv gulylqj hfrqrplf xfwxdwlrqv1 Dowkrxjk wklv
uhvxow lv qrw vxusulvlqj lq lwvhoi 0 diwhu doo/ krxvh sulfhv/ dv dvvhw sulfhv/ fdq eh h{shfwhg wr uh hfw
vkliwv lq h{shfwdwlrqv pruh txlfno| wkdq frqvxphu sulfhv 0/ lw lv hqfrxudjlqj wkdw lw kdv ehhq
rewdlqhg zlwk d kljko| vw|olvhg pdfurhfrqrplf prgho/ wkdw lq rwkhu uhvshfwv forvho| pdwfkhv wkh
73 Ilqdqfldo olehudolvdwlrq hslvrghv duh riwhq uhsruwhg lq wkh olwhudwxuh wr kdyh frqwulexwhg wr wkh krxvlqj errp
lq wkh 4<;3v= uhvwulfwlrqv rq edqn ohqglqj zhuh derolvkhg lq 4<;3/ hqdeolqj edqnv wr frpshwh zlwk exloglqj
vrflhwlhv> dyhudjh ordq0wr0ydoxh udwlrv iru uvw wlph ex|huv urvh iurp 1:7 lq 4<;3 wr 1;9 lq wkh plg 4<;3*v1 Krzhyhu/
wkh idfw wkdw wkh errp fdph vhyhudo |hduv diwhu wkh ghuhjxodwlrq vxjjhvwv wkdw qdqfldo olehudolvdwlrq lwvhoi fdqqrw
h{sodlq wkh errp1 Ghprjudsklf idfwruv duh dovr phqwlrqhg wrr 0 wkh srsxodwlrq lq wkh 5305< djh udqjh urvh e|
416 ploolrq ryhu wkh 4<;3v/ frpsduhg wr 14 ploolrq ryhu wkh suhylrxv ghfdgh 0/ exw wkh| fdq eh kdugo| odehoohg dv
vkrfnv 0 diwhu doo/ wklv skhqrphqrq zdv odujho| suhglfwdeoh dqg/ xqghu h!flhqw pdunhwv/ rqh zrxog h{shfw wkh
pdlq lpsdfw ri ghprjudsklf idfwruv wr eh rq txdqwlwlhv udwkhu wkdq sulfhv1
 ECB Working Paper No 18 G April 2000                                                                                                         33
suhglfwlrqv ri d vwdqgdug LV0OP0Skloolsv fxuyh sdudgljp/ wkxv surylglqj dq lpsruwdqw urexvwqhvv
fkhfn1
Ri frxuvh/ xqghuvwdqglqj zklfk duh wkh fkdqqhov xqghuo|lqj wkh revhuyhg sdwwhuqv iru wkh
glhuhqw uhvsrqvhv lq krxvh sulfhv uhpdlqv d nh| lvvxh lq wkh uhvhdufk djhqgd1 Dowkrxjk wkh
ghpdqg vkrfnv lghqwlhg lq wkh sdshu pljkw fdswxuh vrph fuhglw olehudolvdwlrq hslvrghv/ wkh
urohv ri qdqfldo olehudolvdwlrq dqg ri fuhglw lq gulylqj dvvhw sulfh xfwxdwlrqv kdyh qrw ehhq
gluhfwo| dgguhvvhg e| wklv sdshu1 Lq rwkhu zrugv/ zkloh L kdyh wulhg wr pdnh wkh eodfn er{ ri
wkh fkdqqhov ri wudqvplvvlrq odujhu/ L kdyh qrw wulhg wr rshq lw1
Wkh uhvxowv dovr klqw wkdw glhuhqw krxvlqj dqg fuhglw pdunhw lqvwlwxwlrqv sod| d uroh lq wklv
wudqvplvvlrq phfkdqlvp= vr orqj dv wkh| gr vr/ ri frxuvh/ wkh| dovr vxjjhvw wkdw wklv uhodwlrqvkls
lv xqolnho| wr uhpdlq lqyduldqw ryhu wlph1 Fkdqjhv lq vfdo/ uhjxodwru| dqg ohjdo vwuxfwxuh/ dv
zhoo dv wkh fkdqjh lq wkh prqhwdu| srolf| uhjlph zlwk wkh dgyhqw ri wkh prqhwdu| xqlrq/ duh
olnho| wr dhfw wklv uhodwlrqvkls1 Wklv zrxog eh dovr sduwlfxoduo| olnho| li wkh HFE ghflghg wr
wdujhw krxvh sulfhv dv sduw ri lwv prqhwdu| srolf| vwudwhj|741
Wkh ghedwh rq prqh|/ pdfurhfrqrp| dqg dvvhw sulfhv jrhv edfn wr dw ohdvw 4<44/ zkhq Luylqj
Ilvkhu dujxhg wkdw srolf|pdnhuv vkrxog dlp wr vwdelolvh d eurdg sulfh lqgh{ wkdw lqfoxghg vkduhv/
erqgv dqg surshuw| dv zhoo dv jrrg dqg vhuylfhv1 Dqg wkhuh duh jurzlqj frqfhuqv rq zkhwkhu
h{sdqvlrqdu| prqhwdu| srolflhv fdq ixho dvvhw sulfh exeeohv1 \hw wkh olqn ehwzhhq prqhwdu|
srolf| dqg dvvhw sulfhv lv idu iurp ehlqj fohdu1 Wkh hylghqfh suhvhqwhg lq wklv sdshu ryhudoo
vxjjhvwv wkdw wkh xqv|vwhpdwlf frpsrqhqw ri prqhwdu| srolf| +dqg rwkhu pdfur idfwruv, fdq
sod| dq lpsruwdqw uroh lq gulylqj dvvhw sulfh xfwxdwlrqv1
74 Wklv iroorzv gluhfwo| iurp Jrrgkduw*v Odz dqg wkh Oxfdv fulwltxh1
34                                                                                                                                                           ECB Working Paper No 18 G April 2000  
D Wkh Frpprq Wuhqgv Phwkrgrorj|
Wklv dsshqgl{ ghvfulehv wkh frpprq wuhqgv phwkrgrorj| iru wkh hfrqrphwulf prgho xvhg lq wkh
sdshu1 Wkh h{srvlwlrq iroorzv Zduqh +4<<6, dqg Ilvfkhu/ Idfnohu dqg Rughq +4<<8,1
D14 Frpprq wuhqgv dqg frlqwhjudwlrq
Wkh vshflf prgho fdq eh uhsuhvhqwhg e| d q  4 yhfwru ri hqgrjhqrxv yduldeohv [|/ zklfk kdv
wkh iroorzlqj irup=
I[| @ I[|3 . == . I&[|3& . I]| . x|
+4,
zkhuh [| dqg x| duh ri glphqvlrq +q  4,/ x| lv d yhfwru ri zklwh qrlvh dqg pxwxdoo| ru0
wkrjrqdo vwuxfwxudo vkrfnv/ n lv wkh odj ohqjwk/ ]| lv d yhfwru ri ghwhuplqlvwlf yduldeohv vxfk dv
frqvwdqwv dqg vhdvrqdo gxpplhv/ dqg I*v dqg  duh xqnqrzq frh!flhqwv1 Wkh uhgxfhg irup ri
wkh prgho lv=
[| @ D[|3 . === . D&[|3& . ]| . %|
+5,
zkhuh %| @ I 3x|/ D @ I 3I/ H%% @ I 3I 3 @  1 Wklv prgho fdq eh uhsdudphwulvhg
+lq uvw glhuhqfhv dqg zlwk dq huuru fruuhfwlrq whup, dv iroorzv=
[|
@
[|3  +D2 . === . D&, [|3  ===  D&[|3&n . ]| . %|
+6,
D +O, [|
@
[|3 . ]| . %|
+7,
zkhuh  @ D . === . D&  L1
Li wkh vhulhv duh qrq0vwdwlrqdu| dqg frlqwhjudwhg/ wkhq wkh iroorzlqj krogv= 3 ? u @ udqn  ?
q dqg wkh htxdwlrq +7, deryh lv wkh YHFP irup ri wkh prgho1
Dv vkrzq lq Mrkdqvhq +4<<4, dqg Zduqh +4<<6,/ iurp wkh vwrfkdvwlf sduw ri wkh uhgxfhg
irup ri uhvwulfwhg YDU +htxdwlrq 7 deryh, lw lv srvvleoh wr jhw wkh iroorzlqj prylqj dyhudjh
uhsuhvhqwdwlrq=
[| @ F+O,%|
+8,
Wklv lv rewdlqhg dv iroorzv1 Ghqh wkh wudqvirupdwlrq pdwul{
P 

S 

/ S @ 3
dqg wkh pdwulfhv
G +O, 
 L?3o
3
+4  O, Lo

>
Gz +O, 

+4  O, L?3o
3
Lo

, G +O, Gz +O, @ +4  O, L?
Dovr/ ohw W eh dq q  q pdwul{ vxfk wkdw=
W 
k
3?fE?3o
?fo
l
Lw fdq eh yhulhg wkdw=

[|
 @ W +Gz +O, P[|,
Suhpxowlso| erwk vlghv ri wkh YHFP lq +7, e| P=
PD +O, [| @ P
[|3
 . P]| . P%| @ PW +Gz +O, P[|3, . P]| . P%|
+9,
Wklv fdq eh uhzulwwhq dv=
PD +O, P3G +O, Gz +O, P[|  PWO +Gz +O, P[|,
@
P]| . P%|
+:,
P

D +O, P3G +O,  WO

[W
|
@
U +O, [W
| @ P]| . P%| +;,
 ECB Working Paper No 18 G April 2000                                                                                                    35
Wkh YDU kdv qrz ehhq wudqviruphg lq d YDU zlwk d qhz q glphqvlrqdo yduldeoh/ [W
|
75/
zkhuh=
[W
|  Gz +O, P[|
Lqyhuwlqj +;, |lhogv=
[W
| @ U +O,3 P]| . U +O,3 P%|
+<,
Qrwlqj wkdw [| @ P3G +O, [W
| / zh kdyh/ devwudfwlqj iru d prphqw iurp ghwhuplqlvwlf
frpsrqhqwv=
[| @ P3G +O, U +O,3 P%|
+43,
Wkhuhiruh=
F +O, @ P3G +O, U +O,3 P
+44,
D15 Lghqwlfdwlrq ri shupdqhqw dqg wudqvlwru| vkrfnv
Vxemhfw wr lghqwlfdwlrq/ dq revhuydwlrqdoo| htxlydohqw uhsuhvhqwdwlrq iru [| lv=
[| @  +O, x|
+45,
Zh nqrz wkdw +4, phdvxuhv wkh orqj0uxq hhfw ri wkh vwuxfwxudo vkrfnv1 Hqjoh dqg Judqjhu
+4<;:, kdyh vkrzq wkdw wkh froxpqv ri F+4, duh ruwkrjrqdo wr wkh frlqwhjudwlqj yhfwruv /
vr F +4, @ 31
Wkxv/ dq| edvlv iru q0glphqvlrqdo yhfwruv +q @ 8 lv qxpehu ri yduldeohv
lq wkh prgho, fdq eh glylghg lqwr d vsdfh vsdqqhg e| wkh u @ 6 frlqwhjudwlqj yhfwruv dqg
dq ruwkrjrqdo vsdfh vsdqqhg e| wkh q  u @ 5 olqhduo| lqghshqghqw froxpqv ri F+4,1 Vlqfh
F +4, @ 3/ iru dq|  wkhuh duh +qu,u @ 9 lqghshqghqw uhgxfhg0irup frh!flhqwv ri F+4,1 Wkh
I pdwul{ frqwdlqv q2 sdudphwhuv> iru jlyhq / wkhuh duh +q  u, q lqghshqghqw UI frh!flhqwv
lq F +4, > dv pdq| dv lq  +4,>   frqwdlqv lqirupdwlrq q +q . 4, @5 sdudphwhuv Khqfh zh qhhg
q2  +q . 4, q@5 @ q +q  4, @5 sdudphwhuv wr lghqwli| wkh prgho1
Vwuxfwxudo dqg uhgxfhg irup duh olqnhg dw O @ 4 e|=
F +4, @  +4, I
% @ I 3x
Wkh phwkrgrorj| vxjjhvwhg e| NSVZ jrhv wkurxjk wkh iroorzlqj vwhsv=
4, Sduwlwlrq +4, vr wkdw +4, @ ^S m 3`/ zkhuh S lv d q+qu, pdwul{ zkrvh froxpqv uhsuh0
vhqw wkh orqj0uxq uhvsrqvhv ri wkh yduldeohv wr shupdqhqw vkrfnv/ zkhuhdv wkh orqj0uxq uhvsrqvhv
wr wkh whpsrudu| vkrfnv duh dvvxphg wr eh }hur1 Wkhvh duh wkh vrxufhv ri wkh frpprq vwrfkdvwlf
wuhqgv dprqj wkh yduldeohv1 Iru wkh uhpdlqlqj u vkrfnv/ shupdqhqw hhfwv duh dvvxphg wr eh
}hur/ vr wkhvh vkrfnv kdyh rqo| whpsrudu| hhfwv1 Wklv lpsrvhv +qu,u lghqwli|lqj uhvwulfwlrqv1
5, Sduwlwlrq wkh vkrfnv dffruglqj wr=
x @
k x?3o
xo
l
zkhuh x?3o ghqrwhv vkrfnv zkrvh shupdqhqw hhfwv duh qrq}hur/ zkloh xo ghqrwhv vkrfnv
zkrvh shupdqhqw hhfwv duh }hur +wudqvlwru| vkrfnv,1
6, Sduwlwlrq I frqirupdeo| wr  +4, zlwk lwv uvw q  u dqg odvw u urzv dv I?3o dqg Io
uhvshfwlyho|1 Zh kdyh wkdw F+4, @  +4, I @ SI?3o dv zhoo dv=
F+4, F+4, @ SS 
75Lq rxu fdvh/ iru lqvwdqfh/ jlyhq f| ' d+
6R
R
o
Zo/ zh kdyh=
fW
| '
5
97
{+ n K+{6R n {R
3K{6R n { n {Z
3K++ n 6R n K
3+ n R
 3 Z
6
:8
36                                                                                                                                               ECB Working Paper No 18 G April 2000  
Wkhuh duh +q  u, +q  u . 4, @5 lqghshqghqw htxdwlrqv rq wkh OKV dqg +q  u,2 iuhh sdudp0
hwhuv lq S1 Khqfh zh qhhg +q  u, +q  u  4, @5 dgglwlrqdo uhvwulfwlrqv rq S/ zklfk fdq eh ghdow
zlwk dvvxplqj wkdw wklv pdwul{ lv orzhu wuldqjxodu1
7, F+4, kdv udqn q  u/ khqfh/ lq rughu wr ghfrpsrvh lw/ zh fdqqrw xvh vwdqgdug Fkrohvnl
ghfrpsrvlwlrq surfhgxuh iru F+4, F+4,1 Wr ghdo zlwk wklv lw lv srvvleoh iru lqvwdqfh ghqh S
e| S @ hS/ zkhuh hS*v froxpqv duh nqrzq frh!flhqwv vshflhg d sulrul dqg E?3oE?3o lv d
orzhu wuldqjxodu pdwul{ ri frh!flhqwv wr eh hvwlpdwhg1
8, Frqirupdeo| zlwk hS/ ohw G eh dq +q  u,  q pdwul{ vroylqj F+4, @ hSG/ vxfk dv
G @ + hS  hS,3 hS F+4,1 Jhw  zlwk d orzhu wuldqjxodu Fkrohvnl ghfrpsrvlwlrq ri G G/ wkhq xvh
 wr fdofxodwh S1
9, Jlyhq wkdw F +4, @ SI?3o @ hSI?3o @ hSG/ zh kdyh I?3o @ 3G/ khqfh zh fdq rewdlq
wkh vwuxfwxudo vkrfnv x zlwk shupdqhqw hhfwv e| suhpxowlso|lqj wkh uhgxfhg irup uhvlgxdov %
e| I?3o1
:, Khqfh=
I?3o[| @ I?3o[|3  ===  I?3oI&[|3&n . I?3o ]| . x?3oc|
Rqfh I?3o lv hvwlpdwhg/ wkh g|qdplf hhfwv rq [| ri wkh vkrfnv zlwk shupdqhqw hhfwv duh
rewdlqhg xvlqj=
 +O,?3o @ F +O,
k
I 3l
?3o @ F +O,  I 
?3o
zkhuh
I 3
?3o ghqrwhv wkh uvw q  u froxpqv ri I 31
;, Lghqwlfdwlrq ri wkh vwuxfwxudo sdudphwhuv dvvrfldwhg zlwk wkh vkrfnv zlwk rqo| wudqvlwru|
hhfwv fdq surfhhg iurp= ^3
Lo`of? @ ^Io I?3o
Io I 
o`1 Rqh srvvlelolw| wr lghqwli| Io lv
vshfli| d wuldqjxodu vwuxfwxuh lq lw/ dv lv grqh lq wklv sdshu1
 ECB Working Paper No 18 G April 2000                                                                                                           37
Wdeoh E14= Rxwsxw uhvsrqvh wr dq h{sdqvlrqdu| prqhwdu| vkrfn
DXWKRU+V,
JHUPDQ\
IUDQFH
X1N1
Ixqj Ndvxprylfk +4<<;,
01; 2 1; +9t,
148 2 15 +4t,
14 2 148 +:t,
Eduudq hw do1 +4<<9,
3 2 18 +:t,
3 2 178 +9t,
3 2 18 +;t,
Jhuodfk Vphwv +4<<8,
3 2 158 +9t,
3 2 1; +9t,
3 2 198 +:t,
Udpdvzdp| Vorn +4<<;,
3 2 1: +46t,
3 2 18 +;t,
3 2 1: +47t,
Odvwudshv +4<<;,
15 2 17 +8t,
4 2 4 +4t,
17 2 18 +6t,
Vlpv +4<<5,
3 2 1: +:t,
014 2 415 +9t,
3 2 18 +:t,
Nlp +4<<<,
3 2 16 +8t,
3 2 16 +7t,
Julool Urxelql +4<<9,
3 2 16 +6t,
3 2 14; +7t,
3 2 158 +7t,
DYHUDJH
17<
18;
177
Hvwlpdwhg rxwsxw uhvsrqvh lq shufhqwdjh wr dq h{sdqvlrqdu| prqhwdu| srolf| vkrfn 0 rqh vwdqgdug ghyldwlrq lq
vl}h 0 lq wkh zrunv ri wkh dxwkruv lq wkh uvw froxpq= wkh uvw jxuh lq hdfk fhoo uhihuv wr wkh shufhqwdjh lpsdfw
uhvsrqvh ri rxwsxw lq wkh shulrg ri wkh vkrfn/ wkh vhfrqg wr lwv pd{lpxp ghyldwlrq iurp wkh edvholqh +wkh txduwhu
lq zklfk wkh pd{lpxp lv uhdfkhg lv lq eudfnhwv,1 Wkh jxuh lq wkh odvw urz lv wkh dyhudjh dfurvv shdn uhvsrqvhv
Wdeoh E15= FSL uhvsrqvh wr dq h{sdqvlrqdu| prqhwdu| vkrfn
DXWKRU+V,
JHUPDQ\
IUDQFH
X1N1
Ixqj Ndvxprylfk +4<<;,
319
317
31:
Eduudq hw do1 +4<<9,
---
Jhuodfk Vphwv +4<<8,
3158
315
3
Udpdvzdp| Vorn +4<<;,
---
Odvwudshv +4<<;,
316
31:
4
Vlpv +4<<5,
3138
0315
3
Nlp +4<<<,
314
317
31;
Julool Urxelql +4<<9,
315
317
DYHUDJH
18;
177
Hvwlpdwhg FSL uhvsrqvh wr dq h{sdqvlrqdu| prqhwdu| vkrfn +4 v1h1, lq wkh zrunv ri wkh dxwkruv lq wkh uvw
froxpq= wkh jxuh lq hdfk fhoo uhihuv wr ghyldwlrq ri wkh FSL iurp wkh edvholqh diwhu ; txduwhuv> wkh jxuh lq wkh
odvw urz lv wkh dyhudjh dfurvv wkh uhvsrqvhv diwhu ; txduwhuv> --- lqglfdwhv wkdw wkh uhvxowv iru wkh FSL uhvsrqvh
duh qrw vkrzq lq wkh sdshu1
E Frpsdulqj prqhwdu| vkrfnv lq Hxursh
Frpsdulqj dfurvv frxqwulhv wkh hhfwv ri d prqhwdu| vkrfn lv qrw d vlpsoh h{huflvh/ dv hylghqfh
lv udwkhu pl{hg dfurvv vwxglhv dqg lghqwlfdwlrq vfkhphv +vhh Jxlvr hw do1/ 4<<</ dqg Hkupdqq/
5333,1 Wdeohv E14 dqg E15/ wkdw uhihu wr wkh uhvsrqvh ri rxwsxw dqg frqvxphu sulfhv wr dq
h{sdqvlrqdu| prqhwdu| vkrfn lq Iudqfh/ Jhupdq| dqg Xqlwhg Nlqjgrp/ vkrxog frqylqfh wkh
uhdghu zk| frpsdulqj wkh hhfw ri d prqhwdu| vkrfn dfurvv frxqwlhv lv dq kd}dugrxv wdvn1
Ryhudoo/ rqh zrxog eh whpswhg wr frqfoxgh wkdw wkh glhuhqfhv lq wkh wudqvplvvlrq phfkdqlvp
dfurvv Hxursh duh qrw odujh1
38                                                                                                        ECB Working Paper No 18 G April 2000  
Uhihuhqfhv
^4` Edqtxh gh Iudqfh +4<<<,/ Dvvhw Sulfhv ryhu Wzhqw| \hduv/ Pd|/ plphr1
^5` Eduudq/ I1/ Y1Frxghuw dqg E1Prmrq +4<<9,/ Wkh Wudqvplvvlrq ri wkh Prqhwdu| Srolf| lq
wkh Hxurshdq Frxqwulhv/ Orqgrq Vfkrro ri Hfrqrplfv/ Ilqdqfldo Pdunhwv Jurxs/ Vshfldo
Sdshu/ Qr1;91
^6` Ehuj/ F1/ dqg U1Juùwwkhlp +4<<:,/ Prqhwdu| Srolf| lq Vzhghq vlqfh 4<<5/ ELV Sxeolf
Srolf| sdshu qr151
^7` Ehuqdqnh/ E1/ dqg P1Jhuwohu +4<<8,/ Lqvlgh wkh Eodfn Er{= Wkh Fuhglw Fkdqqho ri Prqh0
wdu| Srolf| Wudqvplvvlrq/ Mrxuqdo ri Hfrqrplf Shuvshfwlyhv/ </ 7/ 5:07;1
^8` Ehuqdqnh/ E1/ dqg P1Jhuwohu +4<<<,/ Prqhwdu| Srolf| dqg Dvvhw Sulfh Yrodwlolw|/ Ihghudo
Uhvhuyh Edqn ri Ndqvdv Flw| Hfrqrplf Uhylhz/ 7/ 80451
^9` Ehuqdqnh/ E1/ P1Jhuwohu dqg V1Jlofkulvw +4<<<, Wkh Ilqdqfldo Dffhohudwru lq d Txdqwlwd0
wlyh Exvlqhvv F|foh Iudphzrun/ lq M1Wd|oru dqg P1Zrrgirug +hgv1,/ Kdqgerrn ri Pdfurh0
frqrplfv1
^:` Eodqfkdug/ R1 dqg G1Txdk +4<;<,/ Wkh G|qdplf Hhfwv ri Djjuhjdwh Ghpdqg dqg Vxsso|
Glvwxuedqfhv/ Dphulfdq Hfrqrplf Uhylhz/ :</ 7/ 98809:61
^;` Erpkr/ H1M1 +4<<7,/ Ilqdqfldo Iruhfdvwlqj iru Exvlqhvv dqg Hfrqrplfv/ Orqgrq/ Dfd0
ghplf Suhvv1
^<` Erulr/ Y1/ Q1 Nhqqhg| dqg V1 G1 Surzvh +4<<7,/ H{sorulqj Djjuhjdwh Dvvhw Sulfh Ioxfwx0
dwlrqv Dfurvv Frxqwulhv= Phdvxuhphqw/ Ghwhuplqdqwv dqg Prqhwdu| Srolf| Lpsolfdwlrqv/
ELV Hfrqrplf Sdshuv/ Qr1 731
^43` Fdvh/ N1/ dqg U1Vkloohu +4<;<,/ Wkh H!flhqf| ri wkh Pdunhw iru Vlqjoh0Idplo| Krphv/
Dphulfdq Hfrqrplf Uhylhz/ :</ 4/ 458046:1
^44` Fdvh/ N1/ dqg U1Vkloohu +4<<3,/ Iruhfdvwlqj Sulfhv dqg H{fhvv Uhwxuqv lq wkh Krxvlqj
Pdunhw/ DUHXHD Mrxuqdo/ 4;/ 58605:61
^45` Fhqvlv +4<<9,/ Wuhqwhvlpr Udssruwr vxood Vlwxd}lrqh Vrfldoh gho Sdhvh/ IudqfrDqjhol/ Pl0
odqr1
^46` Fkr/ P1 +4<<9,/ Krxvh Sulfh G|qdplfv= D Vxuyh| ri Wkhruhwlfdo dqg Hpslulfdo Lvvxhv/
Mrxuqdo ri Krxvlqj Uhvhdufk/ :/ 5/ 47804:41
^47` Fkulvwldqr/ O1/ P1Hlfkhpedxp dqg F1Hydqv +4<<<,/ Prqhwdu| Srolf| Vkrfnv= zkdw kdyh
zh Ohduqhg dqg wr zkdw HqgB/ lq M1Wd|oru dqg P1Zrrgirug +hgv1,/ Kdqgerrn ri Pdfurh0
frqrplfv1
^48` Frfkudqh/ M1 +4<<7,/ Vkrfnv/ Fduqhjlh Urfkhvwhu Frqihuhqfhv Vhulhv rq Sxeolf Srolf|/
74/ 5<806971
^49` Frfkudqh/ M1 +4<<;,/ Zkdw gr wkh YDUv PhdqB Phdvxulqj wkh Rxwsxw Hhfwv ri Prqhwdu|
Srolf|/ Mrxuqdo ri Prqhwdu| Hfrqrplfv/ 74/ 5/ 5::06331
^4:` Frhqhq/ J1/ dqg M0O1Yhjd +4<<<,/ Wkh Ghpdqg iru P6 lq wkh Hxur Duhd/ HFE Zrunlqj
Sdshu Qr1 91
^4;` Furzghu/ Z1M1/ G1Krpdq/ dqg U1Udvfkh +4<<<,/ Lghqwlfdwlrq/ Orqj0Uxq Uhodwlrqv/
dqg Ixqgdphqwdo Lqqrydwlrqv lq d Vlpsoh Frlqwhjudwhg V|vwhp/ Uhylhz ri Hfrqrplfv dqg
Vwdwlvwlfv/ ;4/ 4/ 43<04541
^4<` Fxuzhq/ S1 +4<<:,/ Xqghuvwdqglqj wkh XN Hfrqrp|/ Pdfploodq/ Krxqgploov/ Edvlqjvwrnh1
 ECB Working Paper No 18 G April 2000                                                                                                     39
^53` Fxwohu/ M1 +4<<8,/ Wkh Krxvlqj Pdunhw dqg wkh Hfrqrp|/ Edqn ri Hqjodqg Txduwhuo|
Exoohwlq/ 68/ 6/ 593059<1
^54` Hkupdqq/ P1 +5333,/ Frpsdulqj Prqhwdu| Srolf|/ iruwkfrplqj/ Uhylhz ri Zruog Hfr0
qrplfv1
^55` Hqjoh/ U1I1 dqg F1Z1M1 Judqjhu/ +4<;:,/ Fr0lqwhjudwlrq dqg Huuru Fruuhfwlrq= Uhsuhvhq0
wdwlrq/ Hvwlpdwlrq dqg Whvwlqj/ Hfrqrphwulfd/ 88/ 40;:1
^56` Hqjoxqg/ S1/ dqg \1P1Lrdqqlghv +4<<:,/ Krxvh Sulfh G|qdplfv= dq Lqwhuqdwlrqdo Hpslulfdo
Shuvshfwlyh/ Mrxuqdo ri Krxvlqj Hfrqrplfv/ 9/ 44<04691
^57` Hulfvvrq/ U1 +4<<;,/ Hpslulfdo Prghoolqj ri Prqh| Ghpdqg/ Hpslulfdo Hfrqrplfv/ 56/
6/ 5<806481
^58` Idvh/ P1/ dqg F1Zlqghu +4<<;,/ Zhdowk dqg wkh Ghpdqg iru Prqh| lq wkh Hxurshdq
Xqlrq/ Hpslulfdo Hfrqrplfv/ 56/ 6/ 83:08571
^59` Ilvkhu/ L1 +4<44,/ Wkh Sxufkdvlqj Srzhu ri Prqh|/ Wkh PdfPloodq Suhvv1
^5:` Ilvkhu/ L1 +4<66,/ Wkh Ghew Gh dwlrq Wkhru| ri Juhdw Ghsuhvvlrqv/ Hfrqrphwulfd/ 4/
66:068:1
^5;` Ilvfkhu/ O1/ S1Idfnohu dqg G1Rughq +4<<8,/ Orqj0Uxq Lghqwli|lqj Uhvwulfwlrqv iru dq Huuru0
fruuhfwlrq Prgho ri Qhz ]hodqg Prqh|/ Sulfhv dqg Rxwsxw/ Mrxuqdo ri Lqwhuqdwlrqdo
Prqh| dqg Ilqdqfh/ 47/ 45:047:1
^5<` Ixqj/ E1/ dqg P1Ndvxprylfk +4<<;,/ Prqhwdu| Vkrfnv lq wkh J9 Frxqwulhv= lv wkhuh d
Sx}}ohB/ Mrxuqdo ri Prqhwdu| Hfrqrplfv/ 75/ 8:808<51
^63` Jdol/ M1 +4<<5,/ Krz Zhoo Grhv wkh LV0OP Prgho Ilw Srvwzdu X1V1 GdwdB/ Txduwhuo|
Mrxuqdo ri Hfrqrplfv/ 43:/ 5/ :3<0:6;1
^64` Jhuodfk/ I1/ dqg I1Vphwv +4<<8,/ Wkh Prqhwdu| Wudqvplvvlrq Phfkdqlvp= Hylghqfh iurp
wkh J: Frxqwulhv/ FHSU Glvfxvvlrq Sdshu Qr1 454<1
^65` Julool/ Y1/ dqg Q1Urxelql +4<<9,/ Oltxlglw| Prghov lq Rshq Hfrqrplhv= Wkhru| dqg Hp0
slulfdo Hylghqfh/ Hxurshdq Hfrqrplf Uhylhz/ 73/ ss1;7:0;8</ 4<<91
^66` Jxlvr/ O1/ D1Ndvk|ds/ I1Sdqhwwd dqg G1Whuol}}hvh +4<<<,/ Zloo d Frpprq Hxurshdq Prq0
hwdu| Srolf| Kdyh Dv|pphwulf HhfwvB/ Ihghudo Uhvhuyh Edqn ri Fklfdjr Hfrqrplf Shu0
vshfwlyhv/ 4/ 890:81
^67` Kdplowrq/ M1/ dqg F1K1Zklwhpdq +4<;8,/ Wkh Revhuydeoh Lpsolfdwlrqv ri Vhoi0Ixooolqj
H{shfwdwlrqv/ Mrxuqdo ri Prqhwdu| Hfrqrplfv/ 49/ 6860:71
^68` Khqgu|/ G1/ +4<<8,/ G|qdplf Hfrqrphwulfv/ R{irug Xqlyhuvlw| Suhvv/ R{irug1
^69` Klfnrn/ V1/ dqg F1Rvohu +4<<7,/ Wkh Fuhglw Vorzgrzq Deurdg/ lq Vwxglhv rq Fdxvhv dqg
Frqvhtxhqfhv ri wkh 4<;<0<5 Fuhglw Vorzgrzq/ Ihghudo Uhvhuyh Edqn ri Qhz \run1
^6:` Kljjlqv/ P1/ dqg F1Rvohu +4<<:,/ Dvvhw Pdunhw Kdqjryhuv dqg Hfrqrplf Jurzwk= Wkh
RHFG Gxulqj 4<;70<6/ R{irug Uhylhz ri Hfrqrplf Srolf|/ 46/ 6/ 4430671
^6;` Kropdqv/ D1H1/ +4<<7,/ Krxvh Sulfhv/ Odqg Sulfhv/ wkh Krxvlqj Pdunhw dqg Krxvh Sxu0
fkdvh Ghew lq wkh XN dqg Rwkhu Frxqwulhv/ Hfrqrplf Prghoolqj/ 44/ 5/ 48:05331
^6<` Kxwfklvrq/ P1P1 +4<<7,/ Dvvhw Sulfhv Ioxfwxdwlrqv lq Mdsdq= Zkdw Uroh iru Prqhwdu|
Srolf|B/ ERM Prqhwdu| dqg Edqnlqj Vwxglhv/ 45/ 5/ 940;61
^73` Lwr/ W1/ dqg W1Lzdlvdnr +4<<8,/ H{sodqlqj Dvvhw Exeeohv lq Mdsdq/ QEHU Zrunlqj Sdshu
Qr1 886;1
40                                                                                                                                             ECB Working Paper No 18 G April 2000  
^74` Mdfrevrq/ W1/ D1Yuhglq/ D1Zduqh +4<<;,/ Duh Uhdo Zdjhv dqg Xqhpsor|phqw Uhodwhg/
Hfrqrplfd/ 98/ 9<0<91
^75` Mrkdqvhq/ V1/ +4<<4,/ Hvwlpdwlrq dqg K|srwkhvlv Whvwlqj ri Frlqwhjudwlrq Yhfwruv lq Jdxv0
vldq Yhfwru Dxwruhjuhvvlyh Prghov/ Hfrqrphwulfd/ 8</ 4884048;31
^76` Mrkdqvhq/ V1/ dqg N1Mxvholxv +4<<3,/ Pd{lpxp Olnholkrrg Hvwlpdwlrq dqg Lqihuhqfh rq
Frlqwhjudwlrq 0 zlwk Dssolfdwlrqv wr Ghpdqg iru Prqh|/ R{irug Exoohwlq ri Hfrqrplfv
dqg Vwdwlvwlfv/ 85/ 49<05431
^77` Ndvk|ds/ D1/ M1Vwhlq dqg G1Zlofr{ +4<<6,/ Prqhwdu| Srolf| dqg Fuhglw Frqglwlrqv= Hyl0
ghqfh iurp wkh Frpsrvlwlrq ri H{whuqdo Ilqdqfh/ Dphulfdq Hfrqrplf Uhylhz/ ;6/ :;0<;1
^78` Nhqqhg|/ Q1/ dqg S1Dqghuvrq +4<<7,/ Krxvhkrog Vdylqj dqg Uhdo Krxvh Sulfhv= Dq Lqwhu0
qdwlrqdo Shuvshfwlyh/ ELV Zrunlqj Sdshu Qr1 531
^79` Nhqq|/ J1 +4<<;,/ Wkh Krxvlqj Pdunhw dqg wkh Pdfurhfrqrp|= Hylghqfh iurp Luhodqg/
Edqn ri Luhodqg Zrunlqj Sdshu1
^7:` Nlp/ V1/ +4<<<,/ Gr Prqhwdu| Vkrfnv Pdwwhu lq wkh J0: FrxqwulhvB
Xvlqj Frpprq
Lghqwli|lqj Uhvwulfwlrqv derxw Prqhwdu| Srolf| dfurvv Frxqwulhv/ Mrxuqdo ri Lqwhuqdwlrqdo
Hfrqrplfv/ 7;/ 6;:07451
^7;` Nlqj/ U1/ F1Sorvvhu/ M1Vwrfn dqg P1Zdwvrq +4<<4,/ Vwrfkdvwlf Wuhqgv dqg Hfrqrplf Ioxf0
wxdwlrqv/ Dphulfdq Hfrqrplf Uhylhz/ ;4/ 7/ ;4<0;731
^7<` Nl|rwdnl/ Q1 dqg M1Prruh +4<<:,/ Fuhglw F|fohv/ Mrxuqdo ri Srolwlfdo Hfrqrp|/ 438/ 5440
57;1
^83` Odvwudshv/ Z1G1/ +4<<;,/ Lqwhuqdwlrqdo Hylghqfh rq Htxlw| Sulfhv/ Lqwhuhvw Udwhv/ dqg
Prqh|/ Mrxuqdo ri Lqwhuqdwlrqdo Prqh| dqg Ilqdqfh/ 4:/ 6::07391
^84` Ohlfkwhu/ M1/ dqg F1Zdovk +4<<<,/ Glhuhqw Hfrqrplhv/ Frpprq Srolf|= Srolf| Wudgh0rv
xqghu wkh HFE/ plphr/ Xqlyhuvlw| ri Fdoliruqld Vdqwd Fux}1
^85` Ohylq/ H1M1/ dqg U1H1Zuljkw +4<<:,/ Wkh Lpsdfw ri Vshfxodwlrq rq Krxvh Sulfhv lq wkh
Xqlwhg Nlqjgrp/ Hfrqrplf Prghoolqj/ 47/ 89:08;<1
^86` PdfNlqqrq/ M1J1 +4<<4,/ Fulwlfdo Ydoxhv iru Frlqwhjudwlrq Whvwv/ lq U1Hqjoh dqg
F1Judqjhu hgv1/ Orqj0Uxq Hfrqrplf Uhodwlrqvklsv/ R{irug Xqlyhuvlw| Suhvv/ R{irug1
^87` Pdfohqqdq/ G1/ M1Pxhooedxhu/ dqg P1Vwhskhqv +4<<;,/ Dv|pphwulhv lq Krxvlqj dqg Il0
qdqfldo Pdunhw Lqvwlwxwlrqv dqg HPX/ R{irug Uhylhz ri Hfrqrplf Srolf|/ 47/ 6/ 870;31
^88` Phoodqghu/ H1/ D1Yuhglq dqg D1Zduqh +4<<5,/ Vwrfkdvwlf Wuhqgv dqg Hfrqrplf Ioxfwxd0
wlrqv lq d Vpdoo Rshq Hfrqrp|/ Mrxuqdo ri Dssolhg Hfrqrphwulfv/ :/ 69<06<71
^89` Phow}hu/ D1K1 +4<<8,/ Prqhwdu|/ Fuhglw dqg +Rwkhu, Wudqvplvvlrq Surfhvvhv= D Prqhwdulvw
Shuvshfwlyh/ Mrxuqdo ri Hfrqrplf Shuvshfwlyhv/ </ 7/ 7<0:51
^8:` Plohv/ G1 +4<<5,/ Krxvlqj Pdunhwv/ Frqvxpswlrq dqg Ilqdqfldo Olehudolvdwlrq lq wkh Pdmru
Hfrqrplhv/ Hxurshdq Hfrqrplf Uhylhz/ 69/ 8/ 43<60 445:1
^8;` Plohv/ G1 +4<<8,/ Krxvlqj/ qdqfldo pdunhwv dqg wkh zlghu hfrqrp|/ Mrkq Zloh| dqg Vrqv/
Qhz \run1
^8<` Pruulv/ F1/ dqg J1Vhoorq +4<<8,/ Edqn Ohqglqj dqg Prqhwdu| Srolf|= Hylghqfh rq d Fuhglw
Fkdqqho/ Ihghudo Uhvhuyh ri Ndqvdv Flw| Hfrqrplf Uhylhz/ 5/ 8<0:81
^93` Pxhooedxhu/ M1/ dqg D1Pxusk| +4<<:,/ Errpv dqg Exvwv lq wkh XN Krxvlqj Pdunhw/
Hfrqrplf Mrxuqdo/ 43:1 4:3405:1
 ECB Working Paper No 18 G April 2000                                                                                                     41
^94` Ruwdor0Pdjqë/ I1/ dqg V1Udg| +4<<<,/ Errp lq/ Exvw rxw= \rxqj Krxvhkrogv dqg wkh
Krxvlqj Sulfh F|foh/ Hxurshdq Hfrqrplf Uhylhz/ 76/ :880991
^95` Skloolsv/ S1F1E1/ dqg S1 Shuurq +4<;;,/ Whvwlqj iru d Xqlw Urrw lq Wlph Vhulhv Uhjuhvvlrq/
Elrphwulnd/ :8/ 66806791
^96` Srwhued/ M1 +4<;7,/ Wd{ Vxevlglhv wr Rzqhu0Rffxslhg Krxvlqj= Dq Dvvhw Pdunhw Ds0
surdfk/ Txduwhuo| Mrxuqdo ri Hfrqrplfv/ <</ :5<0:851
^97` Srwhued/ M1 +4<<4,/ Krxvh Sulfh G|qdplfv= Wkh Uroh ri Wd{ Srolf| dqg Ghprjudsk|/
Eurrnlqjv Sdshuv rq Hfrqrplf Dfwlylw|/ 5/ 47605361
^98` Txljoh|/ M1 P +4<<5,/ Krxvlqj Pdunhwv lq M1 Hdwzhoo/ P1 Plojdwh dqg S1 Qhzpdq +hgv1,/
Wkh Qhz Sdojudyh= D Glfwlrqdu| ri Hfrqrplfv/ 6053/ Orqgrq/ Pdfploodq Suhvv1
^99` Udpdvzdp|/ U1/ dqg W1Vorn +4<<;,/ Wkh Uhdo Hhfwv ri Prqhwdu| Srolf| lq wkh Hxurshdq
Xqlrq= Zkdw Duh wkh GlhuhqfhvB/ LPI Vwd Sdshuv/ 78/ 5/ 6:706<91
^9:` Vhoorq/ J1/ dqg F1U1Exvndv +4<<<,/ Qhz Fkdoohqjhv iru Prqhwdu| Srolf|= D Vxppdu| ri
wkh Edqn*v 4<<< V|psrvlxp/ Ihghudo Uhvhuyh Edqn ri Ndqvdv Flw| Hfrqrplf Uhylhz/ 7/
80451
^9;` Vkljhpl/ \1/ +4<<8,/ Dvvhw Lq dwlrq lq Vhohfwhg Frxqwulhv/ ERM Prqhwdu| dqg Edqnlqj
Vwxglhv/ 46/ 5/ 4<<81
^9<` Vlpv/ F1/ +4<;3,/ Pdfurhfrqrplfv dqg Uhdolw|/ Hfrqrphwulfd/ 7;/ 407;1
^:3` Vlpv/ F1/ +4<<5,/ Lqwhusuhwlqj wkh Pdfurhfrqrplf Wlph0vhulhv idfwv= wkh Hhfwv ri Prqh0
wdu| Srolf|/ Hxurshdq Hfrqrplf Uhylhz/ 69/ <:8043441
^:4` Vlpv/ F1/ +4<<;,/ Frpphqw rq Johqq Uxghexvfk*v cGr Phdvxuhv ri Prqhwdu| Srolf| lq d
YDU Pdnh VhqvhB*/ Lqwhuqdwlrqdo Hfrqrplf Uhylhz/ 6</ 7/ <660<741
^:5` Vplwk/ H1R1 +4<<7,/ Wkh Jhupdq Hfrqrp|/ Urxwohgjh/ Orqgrq dqg Qhz \run1
^:6` Vwhlq/ M1 +4<<8,/ Sulfhv dqg Wudglqj Yroxphv lq wkh Krxvlqj Pdunhw= D prgho zlwk
Grzqsd|phqw Frqvwudlqwv/ Txduwhuo| Mrxuqdo ri Hfrqrplfv/ 443/ 6:<07391
^:7` Wd|oru/ P1 +4<<8,/ Wkh Prqhwdu| Wudqvplvvlrq Phfkdqlvp= Dq Hpslulfdo Iudphzrun/
Mrxuqdo ri Hfrqrplf Shuvshfwlyhv/ </ 7/ 440591
^:8` Wkh Hfrqrplvw/ D ihz Krph Wuxwkv/ 53wk Mxqh 4<<51
^:9` Yheohq/ W1 +4<37,/ Wkh Wkhru| ri Exvlqhvv Hqwhusulvh/ Vfuleqhu/ Qhz \run1
^::` Yoddu/ S1M1J1 +4<<;,/ Rq wkh Dv|pswrwlf Glvwulexwlrq ri Lpsxovh Uhvsrqvh Ixqfwlrqv
zlwk Orqj0uxq Uhvwulfwlrqv/ Gh Qhghuodqgvfkh Edqn/ Uhvhdufk Phprudqgxp ZR)H qu
86<2<;3</ Dpvwhugdp1
^:;` Zduqh/ D1 +4<<6,/ D Frpprq Wuhqgv Prgho= Lghqwlfdwlrq/ Hvwlpdwlrq dqg Lqihuhqfh/
vhplqdu sdshu Qr1888/ LLHV/ Vwrfnkrop1
42                                                                                                                                        ECB Working Paper No 18 G April 2000

---

*Note: This file was re-extracted from the ECB source PDF. 42 of 66 pages have clear text extraction. Pages 1, 3, and 44-65 use custom font encoding that could not be decoded. The garbled pages contain the acknowledgments, appendix details, references, and figures.*
