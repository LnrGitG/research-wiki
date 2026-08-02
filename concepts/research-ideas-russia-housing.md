# Research Ideas: Russian Housing Market & Developer Financial Health

*Created: 2026 | Status: Idea bank for future research projects*

---

## 1. Developer Financial Health Panel (SPARK + Macro)

### Core Idea
Build a longitudinal panel of Russian developer financials (large, medium, small) from SPARK/Interfax disclosures, linked to macro factors, to model:
- **Financial distress prediction** for developers
- **Supply elasticity** conditional on financial constraints
- **Transmission mechanism** from monetary policy → developer balance sheets → housing supply

### Data Sources
| Source | Coverage | Frequency | Key Variables |
|--------|----------|-----------|---------------|
| SPARK (Interfax) | All registered developers | Annual/Quarterly | Revenue, EBITDA, Net debt, Assets, Equity, Cash flow, Project finance, Escrow balances |
| EISZhS (ЕИСЖС) | Project-level declarations | Monthly/Quarterly | Construction volume, Sales, Prices, Completion dates, Regions |
| CBR Form 101/135 | Bank lending to construction | Monthly | Loan volumes, Rates, NPLs, Collateral types |
| Rosstat | Macro/regional | Monthly/Annual | GRP, Employment, Wages, Migration, Construction permits, Housing input |
| CBR | Macro | Monthly | Key rate, Inflation, Mortgage rates, Money supply |
| NOSTROY | Industry surveys | Periodic | Labor shortages, Cost indices, Expectations |

### Developer Size Stratification
| Tier | Criteria (annual construction volume) | Est. Count | Key Research Questions |
|------|--------------------------------------|------------|------------------------|
| Large (Public) | >500k sqm, listed on MOEX | 5-10 | Market leadership, Access to capital markets, Systemic risk |
| Large (Private) | >500k sqm, not listed | 20-30 | Private equity backing, Opacity, Leverage strategies |
| Medium | 100k-500k sqm | 100-200 | Regional dominance, Bank dependence, Growth vs. stability |
| Small | <100k sqm | 2000+ | Niche markets, Survival rates, Informal financing |

### Key Macro-Financial Linkages to Test

#### A. Monetary Policy Transmission
```
Key Rate → Mortgage Demand → Developer Revenue → Debt Service Capacity → New Project Starts
                ↓
         Project Finance Cost → Marginal Project Viability → Supply Elasticity
```

#### B. Financial Constraint Channel
```
Net Debt/EBITDA > threshold → Credit rationing → Reduced starts → Lower supply elasticity
Interest Coverage < threshold → Forced asset sales / distressed M&A → Market concentration
Escrow Coverage < 100% → Bank reluctance → Project delays → Supply lags
```

#### C. Balance Sheet Channel (Bernanke-Gertler-Gilchrist for developers)
```
Asset prices (land, WIP) ↑ → Collateral value ↑ → Borrowing capacity ↑ → Investment ↑
Key rate ↑ → Discount rate ↑ → NPV of projects ↓ → Investment ↓
```

---

## 2. Supply Elasticity Estimation: Micro-to-Macro

### Building on CMWP (Regional) + Baum-Snow & Han (Tract) + MACON (Firm-level)

| Level | Spatial Unit | Method | Elasticity Estimate | This Research Adds |
|-------|--------------|--------|---------------------|-------------------|
| Macro | 85 Regions (CMWP) | IV-FE Panel | 0.62-0.91 (SR) | Financial constraints as heterogeneity source |
| Meso | 200+ Cities | Bartik IV + Firm FE | ? | Developer-level financial health as supply shifter |
| Micro | 10k+ Tracts (BSH-style) | Microgeography | 0.74 (unit), 2.53 (quality-adj) | Russian cadastral + developer registry match |
| Firm | 2000+ Developers | Panel + IV | ? | **NEW: Financial health → project-level supply response** |

### Novel Identification Strategies
1. **Developer-level Bartik**: Bank-specific lending shocks × developer-bank relationships
2. **Escrow release timing**: Exogenous cash flow shocks from escrow account releases
3. **Mortgage policy changes**: Family mortgage / IT mortgage / regional programs as demand shifters
4. **Land auction wins**: Quasi-random land acquisition → supply response conditional on leverage

---

## 3. Developer Distress & Market Structure

### Research Questions
1. **Distress prediction**: Can we build an early-warning model for developer default using SPARK + project data?
2. **Fire-sale externalities**: When distressed developers liquidate inventory, what's the price impact on competitors?
3. **Market concentration**: Is high leverage driving consolidation? (PIK delisting, Samolet restructuring, Etalon CRE spin-off)
4. **Strategic default**: Do developers strategically delay projects when underwater? (Option value of waiting)

### Data Requirements
- SPARK financials (5+ years for survival analysis)
- ЕИСЖС project declarations (start/completion/sales)
- Arbitration court records (bankruptcy filings, enforcement proceedings)
- Bank exposure data (CBR 101/135 forms, if accessible)
- M&A transactions (land bank purchases, strategic investments)

---

## 4. Construction Input-Output & Cost Pass-Through

### Linking MAХ ЖБИ + MACON + Rosstat + Developer Reports

| Input | Price Trend (2024-2026) | Developer Cost Share | Pass-Through Mechanism |
|-------|------------------------|---------------------|------------------------|
| Cement | ? | ~15-20% | Contract indexation clauses |
| Rebar/Steel | ? | ~10-15% | Fixed-price vs. cost-plus contracts |
| Labor (migrant) | +35-38% (3yr) | ~25-30% | Wage-pressure → cost overruns |
| Energy/Logistics | ? | ~5-10% | Regional variation |
| Land | +? | ~15-25% | Upfront sunk cost, affects project IRR |

### Research Angle
- **Cost pass-through asymmetry**: Do developers pass cost increases to prices fully? (Depends on demand elasticity, competitive structure)
- **Input substitution**: Can developers substitute materials/techniques when input prices spike?
- **Contract structure**: Share of fixed-price vs. cost-plus contracts determines risk allocation

---

## 5. Demographic × Financial × Spatial Model

### Integrating CMWP 2040 Forecast + Developer Panel + Regional Elasticity

```
Demand_t(r) = f(Population_t(r), Headship_t(r), Income_t(r), Affordability_t, MortgageRate_t)
Supply_t(r) = g(Price_t(r), Elasticity(r), DeveloperHealth_t(r), LandAvailability(r), Regulation(r))
Price_t(r) = Equilibrium(Demand_t, Supply_t)
DeveloperHealth_t+1 = h(Profit_t, CashFlow_t, DebtService_t, Macro_t)
```

### Policy Counterfactuals
1. **Mortgage subsidy redesign**: Target by region elasticity (low η → supply-side, high η → demand-side)
2. **Key rate path**: 13% → 10% → 7% scenarios on developer survival & housing output
3. **Migration policy**: Central Asia vs. India labor supply → construction cost → viability
4. **Escrow reform**: 100% coverage mandate → bank lending → project starts

---

## 6. Practical Implementation Roadmap

### Phase 1: Data Infrastructure (Months 1-3)
- [ ] SPARK API / bulk download setup for developer financials (2015-2025)
- [ ] ЕИСЖС project registry download & parsing
- [ ] Rosstat regional macro database construction
- [ ] CBR mortgage/key rate/credit statistics compilation
- [ ] Spatial join: Developer → Projects → Regions → Macro

### Phase 2: Descriptive & Validation (Months 3-5)
- [ ] Developer universe characterization (size, age, geography, leverage)
- [ ] Financial ratio trends by tier (Debt/EBITDA, Interest Coverage, Escrow Coverage, ROE)
- [ ] Project-level outcomes: Completion rates, Delays, Price growth, Sell-through
- [ ] Macro correlation heatmaps

### Phase 3: Causal Estimation (Months 5-9)
- [ ] IV-FE panel: Supply elasticity with financial constraint interactions
- [ ] Event studies: Mortgage policy changes, Key rate moves, Escrow releases
- [ ] Distress prediction: Survival models (Cox, Random Survival Forests)
- [ ] Spatial spillovers: Distressed developer liquidation → competitor prices

### Phase 4: Structural Model & Policy (Months 9-12)
- [ ] Dynamic equilibrium model: Demand-Supply-Developer Health
- [ ] Counterfactual simulations
- [ ] Policy briefs for Minstroy/CBR/Duma

---

## 7. Related Work in Repo (Cross-References)

| Document | Relevance |
|----------|-----------|
| `queries/supply-elasticity-estimation-design.md` | 4-level methodology design |
| `papers/cmwp_1drfkt7eb9.md` | CMWP regional elasticity (IV-FE, Bartik) |
| `papers/baum-snow-han-2024-microgeography-housing-supply.md` | Tract-level microgeography benchmark |
| `papers/macon_4f2149e2.md` | Public developer financials 2023-2025 |
| `papers/cmwp_5i532x0wrc.md` | Demographic forecast to 2040 |
| `papers/cmwp_trends_may2026.md` | Real-time macro monitoring |
| `papers/alfabank_april2026.md` | Bank forecast, public developer outlook |
| `raw/papers/max_zbi_q1_2026.txt` | Construction materials crisis |
| `raw/papers/stroygaz_labor_crisis_2026.txt` | Labor shortage, wage growth |
| `raw/papers/cmwp_debt_burden_2026.txt` | Sector debt/EBITDA 481% |
| `raw/papers/veb_china_real_estate_2026.txt` | China crisis as structural benchmark |

---

## 8. Potential Collaborators / Data Partners

| Organization | Potential Contribution |
|--------------|------------------------|
| ЦМАКП РАНХиГС | Macro modeling, demographic forecasts, regional panel expertise |
| MACON Consulting | Developer financial analysis, project-level data, market knowledge |
| НОСТРОЙ | Industry surveys, labor market data, policy access |
| ЦБ РФ / Банк России | Mortgage statistics, credit registry, macro data |
| Росстат / ЕИСЖС | Construction permits, housing input, project declarations |
| Дом.РФ / АИЖК | Subsidized mortgage data, developer support programs |
| СПБУ / ВШЭ / НИУ ВШЭ | Academic collaboration, PhD student involvement |

---

## 9. Funding / Publication Targets

### Grants
- РФФИ / РНФ (Russian Science Foundation)
- HSE Basic Research Program
- Minstroy / Dom.RF applied research calls

### Journals
- **Top field**: JUE, RED, JHRES, JHE
- **Russian**: Вопросы экономики, Экономическая политика, Региональная экономика
- **Policy**: ЦМАКП working papers, MACON reports, CBR working papers

---

## 10. Immediate Next Steps (This Week)

1. [ ] **SPARK access**: Check if corporate subscription available or need to negotiate
2. [ ] **ЕИСЖС bulk download**: Test API / request bulk export
3. [ ] **Data schema design**: Define panel structure (developer-year-project-region)
4. [ ] **Literature gap map**: Systematic review of Russian developer finance literature
5. [ ] **Proposal draft**: 2-page concept for internal review / funding application

---

*Last updated: 2026 | This is a living document — add ideas as they emerge from new data/reports*