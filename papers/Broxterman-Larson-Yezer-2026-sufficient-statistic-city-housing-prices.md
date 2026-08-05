---
title: "Characteristics of a Sufficient Statistic to Measure City Housing Prices"
authors:
  - Daniel Broxterman (Florida State University)
  - William Larson (US Department of the Treasury)
  - Anthony Yezer (George Washington University)
year: 2026
venue: "NBER CRIW Conference on Measurement of Housing and the Housing Sector, Alexandria, VA, March 12–13, 2026"
publisher: "University of Chicago Press (Studies in Income and Wealth)"
nber_wp: w35144
nber_chapter: c15393
date: "March 2, 2026"
jel: [R14, R31]
keywords:
  - housing price change
  - repeat sales
  - standard urban model
  - spatial equilibrium
  - sufficient statistic
  - submarket aggregation
  - Laspeyres index
  - monocentric city
tags:
  - housing-price-index
  - spatial-aggregation
  - repeat-sales
  - hedonic
  - monocentric-city
  - supply-elasticity
  - intra-urban
  - Baum-Snow-Han-2024
  - Saiz-2010
  - Glaeser-Gyourko-2005
  - nber
  - criw
  - measurement
  - US
links:
  book_chapter: https://www.nber.org/books-and-chapters/measurement-housing-and-housing-sector/characteristics-sufficient-statistic-measure-city-housing-prices
  working_paper: https://www.nber.org/papers/w35144
  pdf_chapter: raw/papers/Broxterman-Larson-Yezer-2026-sufficient-statistic-city-housing-prices.pdf
  pdf_wp: raw/papers/Broxterman-Larson-Yezer-2026-w35144.pdf
---

# Characteristics of a Sufficient Statistic to Measure City Housing Prices

**Broxterman, Larson & Yezer (2026)** — NBER CRIW Conference, March 12–13, 2026

## Abstract

For a variety of empirical purposes, it is important to be able to characterize the levels of and changes to housing prices in cities, whether measured using rents or asset values. This task is complicated by the heterogeneity of the housing stock, the fact that neighborhood is consumed jointly with housing, and differences in accessibility. This paper concentrates on the issue of intra-city location which, based on economic theory, is systematically related to housing prices. The final conclusion is that a sufficient statistic to describe both the level of and change in the average housing price requires that prices be aggregated from relatively homogeneous market areas and weighted by characteristics such as units or interior space. Commonly used repeat-sales and hedonic measures of price change are generally not weighted in this fashion, but could be modified to do so.

**JEL:** R14, R31

## Key Contributions

1. **Derives sufficient-statistic conditions** for metropolitan house price indexes from the standard monocentric city model (Alonso–Mills–Muth). Spatial equilibrium implies two restrictions: one governing spatial aggregation of price changes within a city, and another governing the definition of the housing quantity to be indexed.

2. **Shows that both spatial aggregation and quantity definition (units vs. space)**, together with tenure heterogeneity, affect construction of theoretically consistent price indexes. Unit-based indexes understate effective supply responsiveness and may overstate price effects of demand shocks (Liu, 2018). A space-based index is more consistent with spatial equilibrium.

3. **Empirical illustrations** using American Housing Survey and FHFA data show that aggregation consistent with theory yields materially different measures of appreciation across metropolitan areas. Even modest differences in aggregation and quantity definition can meaningfully alter measured appreciation for individual cities.

## Core Theoretical Argument

### Spatial aggregation condition

In the standard monocentric city model with constant marginal commuting costs, the iso-utility condition implies that housing price changes vary systematically with distance from the city center. Unless highly restrictive preference assumptions are imposed, **appreciation rates cannot be spatially invariant**.

When transaction probabilities are correlated with location-specific appreciation, commonly estimated city-level indexes need not recover average citywide housing price change. Average citywide price change must be constructed as a **weighted aggregation of submarket price indexes** (Laspeyres indexes), where:
- Submarkets satisfy an **appreciation-homogeneity condition**
- Aggregation weights are proportional to each submarket's **share of the housing stock**

These restrictions follow from spatial equilibrium, not from adjustments to the estimation procedure.

### Quantity definition condition

Housing services are not directly observable → empirical work uses proxies. The prevailing practice of indexing **housing units** is problematic:
- Liu (2018): supply elasticity measured in square footage > elasticity measured in units
- Households trade off commuting costs against **price per unit of space**, not price per dwelling
- Unit-based indexes conflate price appreciation with shifts in the size distribution
- **Interior living space** is a better proxy: observable, central to production costs, tied to land use in urban models

## Empirical Evidence on Spatial Heterogeneity

- Ahlfeldt et al. (2023): housing prices and rents evolve very differently across locations, even over short distances
- Glaeser et al. (2012), Malone and Redfearn (2018), Bogin et al. (2019a,b), Edlund et al. (2022), Seagraves and Gatzlaff (2025): persistent differences in appreciation across central-city and suburban neighborhoods, faster growth and greater volatility in more central locations
- **Baum-Snow and Han (2024)**: substantial differences across census tracts in both appreciation rates and supply elasticity; estimates differ depending on whether based on housing units or interior space
- Contat and Larson (2024): alternative aggregation of tract-level repeat-sales indexes yields materially different citywide appreciation when submarket growth rates differ
- Ambrose et al. (2023): rent growth from new leases diverges sharply from surveys of existing tenants
- Anenberg and Laufer (2017): repeat-sales indexes from contract prices differ from closing prices

## Cross-References to Existing Wiki Papers

- **Baum-Snow & Han (2024)** — microgeography of supply elasticity and appreciation (cited extensively; tract-level variation in both appreciation and supply elasticity; units vs. space distinction)
- **Saiz (2010)** — supply elasticity used in empirical correlates (Table A.1–A.3)
- **Glaeser & Gyourko (2005)** — housing value relative to replacement costs (1990) used as correlate
- **Guren et al. (2021)** — sensitivity parameter γ used in cross-city analysis

## Structure

| Section | Content |
|---------|---------|
| 1 | Introduction |
| 2 | Sufficient statistics for a Laspeyres index |
| 3 | Hedonic and repeat-sales indexes: strengths and limitations |
| 4 | Spatial equilibrium and price change as function of distance from city center |
| 5 | Illustration of bias from ignoring spatial heterogeneity (AHS data) |
| 6 | Empirical comparisons with FHFA data |
| 7 | Conclusions |
| Appendix | Tables A.1–A.3: index differences across cities, correlates |

## Relevance to Russian Housing Market Research

This paper provides the **theoretical framework** for validating Russian supply elasticity estimates:
- The spatial aggregation condition directly applies to Russian city-level price indexes (Rosstat, DOM.RF) — within-city variation in appreciation across districts/microdistricts
- The units-vs-space distinction is critical for Russian supply elasticity estimation (Liu 2018 result: sq.m. elasticity > unit elasticity)
- Cross-references Baum-Snow & Han (2024) and Saiz (2010) — the same papers used in the supply-elasticity-estimation-design query
- The monocentric city framework can be adapted to Russian urban structure (Moscow, St. Petersburg, regional centers)
- Implications for how Russian CPI shelter component should be measured (connects to Loewenstein et al. Chapter 7)
