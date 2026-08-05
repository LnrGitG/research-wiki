---
title: "NBER CRIW 2026: Measurement of Housing and the Housing Sector — Chapters 2–11"
volume: "Measurement of Housing and the Housing Sector"
editors:
  - Thesia Garner (BLS)
  - Joseph Gyourko (Wharton)
  - Sonya R. Porter (US Census Bureau)
publisher: "University of Chicago Press (Studies in Income and Wealth)"
conference: "CRIW Conference, Alexandria, VA, March 12–13, 2026"
year: 2026
tags:
  - nber
  - criw
  - measurement
  - housing-price-index
  - housing-starts
  - satellite-imagery
  - hedonic
  - repeat-sales
  - supply-elasticity
  - land-supply
  - CPI-shelter
  - flood-risk
  - intergenerational-mobility
  - rental-ownership
  - US
  - MICE
  - imputation
  - spatial-aggregation
links:
  book: https://www.nber.org/books-and-chapters/measurement-housing-and-housing-sector
---

# NBER CRIW 2026: Measurement of Housing and the Housing Sector
## Chapters 2–11 — Summaries

> Full volume edited by Thesia Garner, Joseph Gyourko & Sonya R. Porter.
> See also: Chapter 1 (Broxterman, Larson & Yezer) in `Broxterman-Larson-Yezer-2026-sufficient-statistic-city-housing-prices.md`.

---

## Chapter 2: A Blended Data Approach to Measuring Monthly Housing Starts
### Czaplicki, Shevlin, Ferronato, Smith, Nayam, Peng, Springer, Walker (US Census Bureau / Reveal Global Consulting)

**NBER WP:** w35113 | **Chapter PDF:** c15395 (rev1) | **Pages:** 47

**Abstract:** As part of the Construction Re-engineering Initiative at the U.S. Census Bureau, alternative data sources are being considered to supplement or replace current data collection. For the Survey of Construction (SOC), this includes observing housing starts from satellite imagery in place of field representative interviews. Satellite images are obtained monthly for a subset of places in the SOC sample. Convolutional neural network models predict likely new residential construction (current focus: single-family). Post-prediction processing: exclusions based on intersections with known buildings/roads, treatments for cloud cover, adjustments for time between consecutive images. Place-level estimates are combined with building permit survey data to produce estimates of West South Central division level housing starts — an experimental Census Bureau product.

**Key points:**
- CNN on satellite imagery to detect single-family housing starts
- Blended with existing building permit + SOC survey data
- Proof of concept; future work on cost control via different sensing technologies
- Cloud cover, image resolution, and model validation are key limitations

**Relevance to Russian research:** Directly relevant to Russian housing starts measurement (ЕИСЖС, ДОМ.РФ). Satellite-based approaches could supplement Russian construction statistics, especially for informal/individual housing starts (ИЖС).

---

## Chapter 3: Measuring Housing Quality Using Revealed Preference — A Geographic PageRank Approach
### Alex Bell (Georgia State), Sophie Calder-Wang (Wharton), Shusheng Zhong

**Chapter PDF:** c15397 (rev1) | **Pages:** 45 | **JEL:** R32, R31, C39

**Abstract:** Introduces Geographic PageRank (GPR), a measure of place quality based on migration decisions, employing a recursive algorithm that leverages the full network of migration flows. Constructs GPR rankings for U.S. counties and metropolitan areas using public data sources. Extends rankings to capture changes over time and differences for population subgroups. As an application, shows GPR can serve as an "anti-instrument" for unobserved housing quality when pricing environmental amenities, recovering a correctly signed implicit price of air pollution in line with quasi-experimental benchmarks.

**Key innovation:** Adapts PageRank algorithm from webpages to places — migration flows as revealed preference. Data available for visualization and download at https://sophieqzwang.github.io/geopagerank/

**Relevance:** Methodology for measuring place quality — could be applied to Russian internal migration data (Rosstat) to rank Russian cities/regions by attractiveness.

---

## Chapter 4: The Positive Spillovers to Risky Investments in Vacant, Abandoned, and Disinvested Properties
### Edward W. Chen (Princeton), Reagan L. Lengefeld (Georgia Tech), Omar Isaac Asensio (Georgia Tech)

**Chapter PDF:** c15399 (rev0) | **Pages:** 33

**Abstract:** Disadvantaged communities disproportionately vulnerable to climate risk on property values. High concentration of vacant, abandoned, and disinvested (VAD) properties. Infill development as publicly funded redevelopment strategy — up to 21% of new housing construction in 209 largest U.S. metro areas over past two decades. Examines positive externalities of infill: increases in surrounding property and land values. Uses record-linked property and tax data in Savannah, GA.

**Key findings:** Spillover effects are highly localized — largest for immediately neighboring properties and blocks with high density of redevelopment activity. Public redevelopment generates localized benefits beyond direct housing provision.

---

## Chapter 5: Rental Prices and the Cost of Living in the United States, 1914–2006
### Ronan C. Lyons (Trinity College Dublin), Allison Shertzer (Pittsburgh), Rowena Gray (UC Davis)

**Chapter PDF:** c15401 (rev0) | **Pages:** 39

**Abstract:** The BLS Rent of Primary Residence (RoPR) series implies nominal rental prices increased just 2.6%/year from 1914–2006 while overall prices grew 3.3%/year — a "falling real rents" puzzle. Shows this puzzle is explained by the evolving treatment of shelter in the CPI. Constructs a new, methodologically consistent shelter price series using the Historical Housing Prices (HHP) Project rental index. Also constructs revised shelter weights back to 1914. The HHP shelter price series increases by a factor of 28.4 (vs. 10.7 in RoPR) and lifts average CPI growth from 3.3% to 3.6%/year. Eliminates the long-run decline in real rents in the CPI.

**Key quantitative results:**
- RoPR: 2.6%/year nominal rent growth (1914–2006)
- HHP series: factor of 28.4 increase vs. RoPR's 10.7
- Revised CPI: 3.6%/year vs. official 3.3%/year
- "Falling real rents" puzzle is a measurement artifact of shelter treatment changes

**Relevance:** Directly relevant to Russian CPI shelter component measurement — Russian Rosstat CPI also faces similar issues with rent/OER treatment.

---

## Chapter 6: The Effect of Land Supply for New Homes on Residential Investment and House Prices
### Justin Katz (Harvard / FRB Boston), Paul S. Willen (FRB Boston & NBER)

**Chapter PDF:** c15403 (rev0) | **Pages:** 37 | **Date:** February 2026

**Abstract:** Uses parcel-level data to provide new facts on the level and distribution of land available for residential development, focusing on New England housing markets between 2007 and 2021. Most buildable parcels are small; large buildable parcels are scarce in most geographic markets. Large buildable parcels are less available in more populous markets, become more scarce as populations grow, and have become more scarce over time. Markets with fewer large parcels experience higher price growth and lower residential development relative to price growth. Evidence consistent with developer returns to scale in parcel size — fragmentation of buildable land across small, disjoint parcels increases house prices by lowering construction productivity and making development less responsive to demand. Counterfactual simulations: recombining small buildable parcels into larger ones (holding total buildable land fixed) would increase supply, raise construction productivity, and reduce house price growth.

**Key findings:**
- Parcel-level data on buildable land in New England, 2007–2021
- Large buildable parcels are scarce, increasingly so over time
- Fragmentation → lower construction productivity → higher prices → dampened supply response
- Physical land fragmentation constrains supply **even apart from formal regulation**
- Counterfactual: recombining parcels raises supply + productivity, reduces price growth

**Relevance to Russian research:** **Most directly relevant chapter** to supply elasticity work. Parallels Russian context where land fragmentation (межевание, земельные участки) is a major constraint on housing supply. Cross-references Glaeser & Gyourko (2005), Saiz (2010), and the broader land-use regulation literature. The Katz-Willen framework can be applied to Russian parcel-level data (ЕИСЖС, Rosreestr) to test whether physical fragmentation constrains supply independently of zoning.

---

## Chapter 7: Nonresponse Imputations and Related Measurement Issues in the CPI for Shelter
### Lara Loewenstein, Hugh Montag, Randal Verbrugge (FRB Cleveland / BLS)

**NBER WP:** w35250 | **Chapter PDF:** c15405 | **Pages:** 61 | **Date:** April 14, 2026

**Abstract:** Shelter is the largest component of U.S. CPI. Nonresponse in the BLS Housing Survey has increased and now represents ~40% of observations. Missing rents are imputed using a class-mean approach based on rent tier, likely leading to upward-biased imputations. Studies alternative imputation methods using variables correlated with nonresponse and rent growth (structure type, tenure length). While a simple model shows different methods could yield sharply different index biases, in practice alternative methods yield similar shelter inflation indexes — suggesting any index bias may be modest.

**Key quantitative findings:**
- ~40% of BLS Housing Survey observations now imputed
- Current class-mean imputation has theoretical upward-bias potential
- Several alternative methods produce similar aggregate shelter inflation
- Central empirical finding is **reassuring**: bias may be modest in practice

**Relevance:** Russian CPI shelter measurement (Rosstat) faces similar nonresponse challenges; imputation methodology comparisons are directly transferable.

---

## Chapter 8: Flood Risk, Insurance, and Housing in the United States
### Suvy Qin (UC Berkeley), John Voorheis (US Census Bureau)

**NBER WP:** w35204 | **Chapter PDF:** c15407 | **Pages:** 53 | **Date:** May 2026

**Abstract:** Combines parcel-level flood risk with confidential linked survey and administrative data at the US Census Bureau. Although net migration to Census blocks in floodplains has increased, there has been essentially no net migration to parcels with flood risk or change in the overall share of households living in floodplains. Income gradients in flood risk are highly non-linear at the household level: slightly negative for the bottom 90 percentiles, dwarfed by disproportionate exposure in the top decile (especially with multiple property ownership). Nonlinearity driven by building type and homeownership within narrow income groups. **In contrast to aggregate-data literature**, household-level analysis suggests floodplain households are less disadvantaged and increasingly protected — though a vulnerable subpopulation of low-income, uninsured homeowners remains.

**Key methodological point:** Aggregate data can imply floodplain exposure is concentrated among disadvantaged households; parcel-linked household microdata reveal a different pattern. The choice of geographic unit of measurement is not neutral.

---

## Chapter 9: Filling the Gaps with MICE — Addressing Missing Data in Real Estate Price Indices
### Miriam Steurer, Sabrina Spiegel

**NBER WP:** w35139 | **Chapter PDF:** c15409 (rev0) | **Pages:** 58 | **Date:** April 13, 2026

**Abstract:** Missing data are common in micro-level transaction data for hedonic real estate price indices. Missingness arises in property characteristics (not prices), central to quality adjustment. Standard complete-case analysis can distort price dynamics through sample-selection and composition effects. Proposes multiple imputation (MICE) as a flexible framework. Develops alternative aggregation procedure based on pooled growth rates (Rubin's rules are inconsistent with multiplicative chaining structure of price indices). Two empirical applications: Vienna apartment transactions (large, uniform market) and Austrian office unit transactions (small, heterogeneous market).

**Key findings:**
- Large/uniform market: hedonic indices robust to missing data; differences between complete-case and MICE are minimal, though MICE generally performs best
- Small/heterogeneous market: imputation can significantly affect index dynamics
- Standard Rubin's rules don't work for chained price indices → new aggregation procedure needed

**Relevance:** Directly applicable to Russian hedonic price indices where property characteristics are often missing from transaction records (Rosstat, DOM.RF data).

---

## Chapter 10: Lands of Opportunity — Differences in the Geography of Wealth and Income Mobility
### Ariel Binder (CES/Census/IZA), Max Risch (CMU), John Voorheis (CES/Census)

**NBER WP:** w35219 | **Chapter PDF:** c15411 | **Pages:** 40 | **Date:** May 2026 | **JEL:** E24, O18, R31, D31

**Abstract:** New county-level estimates of intergenerational mobility covering multiple economic concepts: total income, labor income, homeownership, housing wealth, and total wealth. Uses small-area estimation and linked survey/administrative data covering millions of U.S. children born 1978–1986. Relative mobility in wealth concepts shows less spatial clustering and more spatial variation than in income concepts. Many cities/suburbs exhibit lower relative mobility (higher intergenerational persistence) in wealth than in income. Strong negative association between local severity of the Great Recession and child income, regardless of parent income position. But negative association between recession severity and wealth only exists among children from poorer families. **Public-use data package on census.gov.**

**Key finding:** Geography of opportunity looks different when measured by wealth and homeownership rather than income alone. Housing is the largest asset for many families; homeownership mediates wealth transmission across generations. A geography that appears relatively open by earnings may look less open by asset accumulation.

---

## Chapter 11: Toward a Methodology for Measuring Rental Property Ownership in the United States
### Stephanie Kestelman, Rebecca Diamond, John Eric Humphries, Kate Pennington, Winnie van Dijk, John Voorheis

**Chapter PDF:** c15413 (rev0) | **Pages:** 38 | **Date:** May 2026

**Abstract:** ~1/3 of U.S. households rent, yet measuring who owns rental property is difficult — ownership is obscured by LLCs, partnerships, and intermediary entities. Develops a method that traces ownership through administrative records: deeds + property assessments + Census Bureau Business Register + IRS Schedule K-1 filings + SEC filings on REITs. Identifies ultimate owners and constructs property portfolios across the full landlord size distribution. Applied to 11 large CBSAs: individual landlords own a large majority of rental units, though share varies across markets. The widely used mailing-address aggregation approach both under- and over-states portfolio size in systematic ways. Method designed to scale to national coverage.

**Key findings:**
- Individual landlords own majority of rental units (share varies by market)
- Mailing-address aggregation is systematically biased (both under- and over-counts)
- Ownership tracing through LLCs requires linking multiple administrative data sources
- Method has current limitations: missing entities, incomplete ownership chains

**Relevance:** Russian rental market has similar opacity issues — individual landlords dominate but ownership is often hidden behind legal entities. Methodology applicable to Russian context with Rosreestr + tax data.

---

## Cross-Reference Summary

| Chapter | Key Cross-References | Relevance to Russian Housing Research |
|---------|---------------------|--------------------------------------|
| Ch1 (Broxterman) | Baum-Snow & Han 2024, Saiz 2010, Glaeser & Gyourko 2005, Guren et al. 2021 | Supply elasticity estimation design; spatial aggregation theory |
| Ch2 (Czaplicki) | Census SOC, CNN/satellite | Housing starts measurement (ЕИСЖС, ДОМ.РФ) |
| Ch6 (Katz & Willen) | Glaeser & Gyourko 2005, Molloy et al. 2020 | **Land supply fragmentation** — direct parallel to Russian land parcels |
| Ch7 (Loewenstein) | BLS Housing Survey, CPI shelter | CPI shelter measurement (Rosstat CPI) |
| Ch5 (Lyons) | BLS RoPR, HHP Project, CPI | Long-run rent measurement; CPI shelter treatment |
| Ch9 (Steurer) | MICE, hedonic indices | Hedonic price indices with missing data |