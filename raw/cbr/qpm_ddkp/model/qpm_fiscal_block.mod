
%% qpm_fiscal_block.mod
%
% Fiscal block of QPM for Russia
%

%% Variables' declaration

!transition_variables

%- General government
  'General government revenue ratio (%GDP,MA)'                    REV_GEN_ARAT
  'General government expenditure ratio (%GDP,MA)'                EXP_GEN_ARAT
  %
  'General government deficit ratio (%GDP,MA)'                    DEF_GEN_ARAT
  'General government non-oil deficit ratio (%GDP,MA)'            DEF_NO_GEN_ARAT
  'General government primary non-oil deficit ratio (%GDP,MA)'    DEFP_NO_GEN_ARAT
  
%- Federal government
  'Federal government revenue ratio (%GDP,MA)'                    REV_FED_ARAT
  'Federal government non-oil revenue ratio (%GDP,MA)'            REV_NO_FED_ARAT
  'Oil&gas revenue ratio (%GDP,MA)'                               REV_O_ARAT
  'Fed. gov. welfare-fund-financed revenue ratio (%GDP,MA)'       REV_WF_FED_ARAT
  'Federal government effective non-oil tax rate (%GDP,MA)'       TAU_NO_FED
  'Federal government eq. effective non-oil tax rate (%GDP,MA)'   TAU_NO_FED_EQ
  'Fed. gov. implied target effective non-oil tax rate (%GDP,MA)' TAU_NO_FED_TAR
  'Federal government effective non-oil tax rate gap (%GDP,MA)'   TAU_NO_FED_GAP
  'Base oil&gas revenue ratio (%GDP,MA)'                          REV_O_BASE_ARAT
  'Error in base oil&gas revenue ratio equation (%GDP,MA)'        ERR_REV_O_BASE_ARAT
  'Extra oil&gas revenue ratio (%GDP,MA)'                         REV_O_EXTRA_ARAT
  'Error in extra oil&gas revenue ratio equation (%GDP,MA)'       ERR_REV_O_EXTRA_ARAT  
  'Base oil price, USD/bbl (100*log)'                             LPOIL_USD_BASE
  'Base oil price shock (p.p.)'                                   SHCK_LPOIL_USD_BASE  
  'Fiscal oil price, USD/bbl (100*log)'                           LPOIL_USD_FISC
  'Fiscal oil price gap, USD/bbl (%)'                             LPOIL_USD_FISC_GAP    
  'Change in base oil price (%QoQ @ar)'                           DOT_LPOIL_USD_BASE
  'Change in base oil price (%YoY)'                               DOT4_LPOIL_USD_BASE  
  %
  'Federal government expenditure ratio (%GDP,MA)'                EXP_FED_ARAT
  'Federal government primary expenditure ratio (%GDP,MA)'        EXPP_FED_ARAT
  'Federal government debt service expenditure ratio (%GDP,MA)'   EXP_DEBT_FED_ARAT
  'Fed. gov. rule-based primary expenditure ratio (%GDP,MA)'      EXPP_RULE_FED_ARAT
  'Fed. gov. statutory discr. primary expend. ratio (%GDP,MA)'    EXPP_DISC_FED_ARAT
  'Fed. gov. structural primary expenditure ratio (%GDP,MA)'      EXPP_STR_FED_ARAT
  %
  'Federal government deficit ratio (%GDP,MA)'                    DEF_FED_ARAT
  'Federal government primary deficit ratio (%GDP,MA)'            DEFP_FED_ARAT
  'Federal government non-oil deficit ratio (%GDP,MA)'            DEF_NO_FED_ARAT  
  'Federal government primary non-oil deficit ratio (%GDP,MA)'    DEFP_NO_FED_ARAT
  'Fed. gov. structural primary non-oil deficit ratio (%GDP,MA)'  DEFP_NO_STR_FED_ARAT
  'Federal government base deficit ratio (%GDP,MA)'               DEF_BASE_FED_ARAT  
  'Federal government primary base deficit ratio (%GDP,MA)'       DEFP_BASE_FED_ARAT
  %
  'Fed. gov. deficit financing via debt (%GDP,MA)'                DEF_FIN_FED_DEBT_ARAT  
  'Fed. gov. deficit financing via other sources (%GDP,MA)'       DEF_FIN_FED_OTH_ARAT
  'Fed. gov. deficit financing via (net) new debt (%GDP,MA)'      DEF_FIN_FED_NEW_DEBT_ARAT  
  'Federal government debt ratio (%GDP,MA)'                       DEBT_FED_ARAT
  'Error in federal government debt ratio equation (%GDP,MA)'     ERR_DEBT_FED_ARAT
  'Federal government target debt ratio (%GDP,MA)'                DEBT_FED_TAR_ARAT
  'Federal government debt ratio deviation (%GDP,MA)'             DEBT_FED_DEV_ARAT
  'Federal government debt ratio accrual (%GDP,MA)'               DEBT_FED_ACCR_ARAT
  
%- Regional government
  'Regional government revenue ratio (%GDP,MA)'                   REV_REG_ARAT
  'Regional government effective non-oil tax rate (%GDP,MA)'      TAU_REG
  'Regional government eq. effective non-oil tax rate (%GDP,MA)'  TAU_REG_EQ
  'Reg. gov. implied target effective non-oil tax rate (%GDP,MA)' TAU_REG_TAR
  'Regional government effective non-oil tax rate gap (%GDP,MA)'  TAU_REG_GAP
  %
  'Regional government expenditure ratio (%GDP,MA)'               EXP_REG_ARAT
  'Regional government primary expenditure ratio (%GDP,MA)'       EXPP_REG_ARAT
  'Regional government debt service expenditure ratio (%GDP,MA)'  EXP_DEBT_REG_ARAT
  'Reg. gov. structural primary expenditure ratio (%GDP,MA)'      EXPP_STR_REG_ARAT
  'Reg. gov. implied target primary expenditure ratio (%GDP,MA)'  EXPP_TAR_REG_ARAT
  %
  'Regional government deficit ratio (%GDP,MA)'                   DEF_REG_ARAT
  'Regional government primary deficit ratio (%GDP,MA)'           DEFP_REG_ARAT
  'Reg. gov. structural primary deficit ratio (%GDP,MA)'          DEFP_STR_REG_ARAT  
  
%- Fiscal impulse and stimulus
  'Fiscal stimulus (%GDP)'                                        FISC_STIM
  'Fiscal stimulus from federal budget (%GDP)'                    FISC_STIM_FED
  'Fiscal stimulus from regional budget (%GDP)'                   FISC_STIM_REG
  %
  'Fiscal impulse from fed. gov. revenue (%GDP)'                  FISC_IMP_REV_FED
  'Fiscal impulse from fed. gov. expenditure (%GDP)'              FISC_IMP_EXP_FED
  'Fiscal impulse from discret. fed. gov. non-oil revenue (%GDP)' FISC_IMP_REV_FED_DISC
  'Fiscal impulse from struct. fed. gov. non-oil revenue (%GDP)'  FISC_IMP_REV_FED_STR
  'Cumulated fisc. imp. shock from struct. fed. gov. non-oil revenue (%GDP)'  SHCK_TAU_NO_FED_TAR_CUM
  'Fisc. imp. shock from struct. fed. gov. non-oil revenue (%GDP)'            SHCK_TAU_NO_FED_TAR
  'Fiscal impulse from discret. fed. gov. expenditure (%GDP)'     FISC_IMP_EXP_FED_DISC
  'Fiscal impulse from struct. fed. gov. expenditure (%GDP)'      FISC_IMP_EXP_FED_STR
  'Cumulated fisc. imp. shock from base oil&gas revenue (%GDP)'   SHCK_REV_O_BASE_CUM
  'Fiscal impulse shock from base oil&gas revenue (%GDP)'         SHCK_REV_O_BASE
  %
  'Fiscal impulse from reg. gov. revenue (%GDP)'                  FISC_IMP_REV_REG
  'Fiscal impulse from reg. gov. expenditure (%GDP)'              FISC_IMP_EXP_REG
  'Fiscal impulse from discret. reg. gov. revenue (%GDP)'         FISC_IMP_REV_REG_DISC
  'Fiscal impulse from struct. reg. gov. revenue (%GDP)'          FISC_IMP_REV_REG_STR
  'Cumulated fisc. imp. shock from struct. reg. gov. revenue (%GDP)'     SHCK_TAU_REG_TAR_CUM
  'Fisc. imp. shock from struct. fed. gov. revenue (%GDP)'        SHCK_TAU_REG_TAR
  'Fiscal impulse from discret. reg. gov. expenditure (%GDP)'     FISC_IMP_EXP_REG_DISC
  'Fiscal impulse from struct. reg. gov. expenditure (%GDP)'      FISC_IMP_EXP_REG_STR
  'Cumulated fisc. imp. shock from struct. reg. gov. expenditure (%GDP)' SHCK_EXPP_TAR_REG_CUM
  'Fisc. imp. shock from struct. fed. gov. expenditure (%GDP)'    SHCK_EXPP_TAR_REG

%

%% Fiscal block transition equations

!transition_equations

% --- General government --------------------------------------------------

    REV_GEN_ARAT = REV_FED_ARAT + REV_REG_ARAT;
    EXP_GEN_ARAT = EXP_FED_ARAT + EXP_REG_ARAT;
    
    DEF_GEN_ARAT     = EXP_GEN_ARAT - REV_GEN_ARAT;
    DEF_NO_GEN_ARAT  = DEF_GEN_ARAT + REV_O_ARAT;
    DEFP_NO_GEN_ARAT = DEF_NO_GEN_ARAT - EXP_DEBT_FED_ARAT - EXP_DEBT_REG_ARAT;

    
% --- Federal government --------------------------------------------------

  'Total revenue'
    REV_FED_ARAT = REV_NO_FED_ARAT + REV_O_ARAT + REV_WF_FED_ARAT;
    
    '- non-oil revenue'
    REV_NO_FED_ARAT = TAU_NO_FED;
    TAU_NO_FED      = TAU_NO_FED_EQ + TAU_NO_FED_GAP;
    TAU_NO_FED_EQ   = rho_tau_fed_eq*TAU_NO_FED_EQ{-1} + (1-rho_tau_fed_eq)*TAU_NO_FED_TAR ...
                      + RES_TAU_NO_FED_EQ;
    TAU_NO_FED_TAR  = TAU_NO_FED_TAR{-1} + RES_TAU_NO_FED_TAR;
    TAU_NO_FED_GAP  = rho_tau_fed_gap*TAU_NO_FED_GAP{-1} + RES_TAU_NO_FED_GAP;
    
    '- oil revenue'
    REV_O_ARAT = REV_O_BASE_ARAT + REV_O_EXTRA_ARAT;

    %- base oil revenue
    REV_O_BASE_ARAT = REV_O_BASE_ARAT{-1} + REV_O_BASE_ARAT_SS * (  ...
                      + (DOT4_LPOIL_USD_BASE - PIEF_SS) + (DOT4_LS_USD - DOT4_LS_EQ) ...
                      - (DOT4_Y_NOM - DOT4_Y_NOM_EQ) ) / 4 + ERR_REV_O_BASE_ARAT;  
    %       
    ERR_REV_O_BASE_ARAT = rho_err_rev_o_base*ERR_REV_O_BASE_ARAT{-1} + RES_REV_O_BASE_ARAT;

    LPOIL_USD_BASE = LPOIL_USD - LTOT_GAP + SHCK_LPOIL_USD_BASE;
    SHCK_LPOIL_USD_BASE = rho_shck_poil_base*SHCK_LPOIL_USD_BASE{-1} + RES_LPOIL_USD_BASE;
    
    %- extra oil revenue
    REV_O_EXTRA_ARAT     = phi_rev_o_extra*LPOIL_USD_FISC_GAP + ERR_REV_O_EXTRA_ARAT;    
    ERR_REV_O_EXTRA_ARAT = rho_err_rev_o_extra*ERR_REV_O_EXTRA_ARAT{-1} + RES_REV_O_EXTRA_ARAT;  

    LPOIL_USD_FISC_GAP = LPOIL_USD_FISC - LPOIL_USD_BASE;
    LPOIL_USD_FISC     = w_oil_fisc_lag*(LPOIL_USD{-1} + 0.25*PIEF) + (1-w_oil_fisc_lag)*LPOIL_USD;
            
    '- revenue from spending welfare fund'
    REV_WF_FED_ARAT = RES_REV_WF_FED_ARAT;
    
  'Expenditure'
    EXP_FED_ARAT  = EXPP_FED_ARAT + EXP_DEBT_FED_ARAT;
    
    EXPP_FED_ARAT = rho_expp_fed*EXPP_FED_ARAT{-1} ...
                    + (1-rho_expp_fed)*(EXPP_RULE_FED_ARAT + EXPP_DISC_FED_ARAT) ...
                    - phi_cycl_fed*Y_GAP_MA + RES_EXPP_FED_ARAT;
      
    EXPP_RULE_FED_ARAT = EXPP_STR_FED_ARAT + (TAU_NO_FED_GAP + REV_WF_FED_ARAT);
    %
    EXPP_STR_FED_ARAT = rho_expp_str_fed*EXPP_STR_FED_ARAT{-1} ...
                        + (1-rho_expp_str_fed)*(TAU_NO_FED_EQ + REV_O_BASE_ARAT) ...
                        - phi_debt_dev*DEBT_FED_DEV_ARAT + RES_EXPP_STR_FED_ARAT;
               
    EXPP_DISC_FED_ARAT = rho_rw*EXPP_DISC_FED_ARAT{-1} + RES_EXPP_DISC_FED_ARAT;
    
  'Deficit measures'
    DEF_FED_ARAT     = EXP_FED_ARAT - REV_FED_ARAT;
    DEFP_FED_ARAT    = DEF_FED_ARAT - EXP_DEBT_FED_ARAT;
    DEF_NO_FED_ARAT  = DEF_FED_ARAT + REV_O_ARAT;
    DEFP_NO_FED_ARAT = DEF_NO_FED_ARAT - EXP_DEBT_FED_ARAT;
    %
    DEF_BASE_FED_ARAT    = DEFP_BASE_FED_ARAT + EXP_DEBT_FED_ARAT;
    DEFP_NO_STR_FED_ARAT = EXPP_STR_FED_ARAT - (REV_NO_FED_ARAT + REV_WF_FED_ARAT);
    DEFP_BASE_FED_ARAT   = DEFP_NO_STR_FED_ARAT - REV_O_BASE_ARAT;
    
  'Deficit financing'
    DEF_FED_ARAT = DEF_FIN_FED_DEBT_ARAT - REV_O_EXTRA_ARAT + DEF_FIN_FED_OTH_ARAT;
    
    DEF_FIN_FED_DEBT_ARAT     = EXP_DEBT_FED_ARAT + EXPP_DISC_FED_ARAT + DEF_FIN_FED_NEW_DEBT_ARAT;
    DEF_FIN_FED_NEW_DEBT_ARAT = w_debt_fin*(DEF_FED_ARAT - EXP_DEBT_FED_ARAT - EXPP_DISC_FED_ARAT + REV_O_EXTRA_ARAT);
  
  'Debt dynamics'    
    DEBT_FED_ARAT = rho_auto*DEBT_FED_ARAT{-1} ...
                    - rho_auto*DEBT_FED_ARAT_SS * (DOT4_Y_NOM - DOT4_Y_NOM_EQ)/4 ...
                    + DEF_FIN_FED_DEBT_ARAT/4 + ERR_DEBT_FED_ARAT;
    %
    ERR_DEBT_FED_ARAT = rho_err_debt_fed*ERR_DEBT_FED_ARAT{-1} + RES_DEBT_FED_ARAT;
    
    DEBT_FED_TAR_ARAT  = rho_rw*DEBT_FED_TAR_ARAT{-1} + (1-rho_rw)*DEBT_FED_ARAT_SS + RES_DEBT_FED_TAR_ARAT;
    DEBT_FED_DEV_ARAT  = DEBT_FED_ARAT - phi_debt_tar*DEBT_FED_TAR_ARAT;
    DEBT_FED_ACCR_ARAT = DEBT_FED_ARAT - DEBT_FED_ARAT{-1};
        
    
% --- Regional government -------------------------------------------------

  'Revenue'
    REV_REG_ARAT = TAU_REG;
    TAU_REG      = TAU_REG_EQ + TAU_REG_GAP;
    TAU_REG_EQ   = rho_tau_reg_eq*TAU_REG_EQ{-1} + (1-rho_tau_reg_eq)*TAU_REG_TAR + RES_TAU_REG_EQ;
    TAU_REG_TAR  = TAU_REG_TAR{-1} + RES_TAU_REG_TAR;
    TAU_REG_GAP  = rho_tau_reg_gap*TAU_REG_GAP{-1} + RES_TAU_REG_GAP;
    
  'Expenditure'
    EXP_REG_ARAT      = EXPP_REG_ARAT + EXP_DEBT_REG_ARAT;
    EXP_DEBT_REG_ARAT = EXP_DEBT_REG_ARAT{-1} + RES_EXP_DEBT_REG_ARAT;
    
    EXPP_REG_ARAT = rho_expp_reg*EXPP_REG_ARAT{-1} + (1-rho_expp_reg)*EXPP_STR_REG_ARAT ...
                    - phi_cycl_reg*Y_GAP_MA + RES_EXPP_REG_ARAT;
               
    EXPP_STR_REG_ARAT = rho_expp_str_reg*EXPP_STR_REG_ARAT{-1} ...
                        + (1-rho_expp_str_reg)*EXPP_TAR_REG_ARAT + RES_EXPP_STR_REG_ARAT;
    %
    EXPP_TAR_REG_ARAT = EXPP_TAR_REG_ARAT{-1} + RES_EXPP_TAR_REG_ARAT;
    
  'Deficit measures'
    DEF_REG_ARAT     = EXP_REG_ARAT - REV_REG_ARAT;
    DEFP_REG_ARAT    = DEF_REG_ARAT - EXP_DEBT_REG_ARAT;
    %
    DEFP_STR_REG_ARAT = EXPP_STR_REG_ARAT - REV_REG_ARAT;
  
    
% --- Fiscal impulse and stimulus -----------------------------------------

    FISC_STIM = FISC_STIM_FED + FISC_STIM_REG;

  'Federal budget fiscal stimulus and impulse'
    FISC_STIM_FED = phi_rev*FISC_IMP_REV_FED + phi_exp*FISC_IMP_EXP_FED;
    
    '- revenue impulse'
    FISC_IMP_REV_FED = FISC_IMP_REV_FED_DISC + FISC_IMP_REV_FED_STR;
    FISC_IMP_REV_FED_DISC = -RES_TAU_NO_FED_GAP;
    FISC_IMP_REV_FED_STR = -RES_TAU_NO_FED_EQ + (1-rho_tau_fed_eq)*(-SHCK_TAU_NO_FED_TAR_CUM);
           
    SHCK_TAU_NO_FED_TAR_CUM = SHCK_TAU_NO_FED_TAR + rho_fisc*SHCK_TAU_NO_FED_TAR{-1} + (rho_fisc^2)*SHCK_TAU_NO_FED_TAR{-2} + (rho_fisc^3)*SHCK_TAU_NO_FED_TAR{-3};
    SHCK_TAU_NO_FED_TAR = TAU_NO_FED_TAR - movavg(TAU_NO_FED_TAR{-1}, -8);
    
    '- expenditure impulse'
    FISC_IMP_EXP_FED = FISC_IMP_EXP_FED_DISC + FISC_IMP_EXP_FED_STR;
    FISC_IMP_EXP_FED_DISC = RES_EXPP_FED_ARAT + (1-rho_expp_fed)*(RES_EXPP_DISC_FED_ARAT ...
                            + RES_TAU_NO_FED_GAP + RES_REV_WF_FED_ARAT);
    FISC_IMP_EXP_FED_STR = (1-rho_expp_fed)*( RES_EXPP_STR_FED_ARAT + (1-rho_expp_str_fed)*( ...
                           RES_TAU_NO_FED_EQ + (1-rho_tau_fed_eq)*SHCK_TAU_NO_FED_TAR_CUM ...
                           + SHCK_REV_O_BASE_CUM) );
                       
    SHCK_REV_O_BASE_CUM = SHCK_REV_O_BASE + rho_fisc*SHCK_REV_O_BASE{-1} + (rho_fisc^2)*SHCK_REV_O_BASE{-2} + (rho_fisc^3)*SHCK_REV_O_BASE{-3};
    SHCK_REV_O_BASE = REV_O_BASE_ARAT - movavg(REV_O_BASE_ARAT{-1}, -8);                       
                        
  'Regional budget fiscal stimulus and impulse'
    FISC_STIM_REG = phi_rev*FISC_IMP_REV_REG + phi_exp*FISC_IMP_EXP_REG;
    
    '- revenue impulse'
    FISC_IMP_REV_REG = FISC_IMP_REV_REG_DISC + FISC_IMP_REV_REG_STR;
    FISC_IMP_REV_REG_DISC = -RES_TAU_REG_GAP + RES_FISC_IMP_REV_REG_DISC;    
    FISC_IMP_REV_REG_STR = -RES_TAU_REG_EQ + (1-rho_tau_reg_eq)*(-SHCK_TAU_REG_TAR_CUM);

    SHCK_TAU_REG_TAR_CUM = SHCK_TAU_REG_TAR + rho_fisc*SHCK_TAU_REG_TAR{-1} + (rho_fisc^2)*SHCK_TAU_REG_TAR{-2} + (rho_fisc^3)*SHCK_TAU_REG_TAR{-3};
    SHCK_TAU_REG_TAR = TAU_REG_TAR - movavg(TAU_REG_TAR{-1}, -8);      
    
    '- expenditure impulse'
    FISC_IMP_EXP_REG = FISC_IMP_EXP_REG_DISC + FISC_IMP_EXP_REG_STR;
    FISC_IMP_EXP_REG_DISC = RES_EXPP_REG_ARAT + RES_FISC_IMP_EXP_REG_DISC;
    FISC_IMP_EXP_REG_STR = (1-rho_expp_reg)*(RES_EXPP_STR_REG_ARAT ... 
                            + (1-rho_expp_str_reg)*SHCK_EXPP_TAR_REG_CUM);

    SHCK_EXPP_TAR_REG_CUM = SHCK_EXPP_TAR_REG + rho_fisc*SHCK_EXPP_TAR_REG{-1} + (rho_fisc^2)*SHCK_EXPP_TAR_REG{-2} + (rho_fisc^3)*SHCK_EXPP_TAR_REG{-3};
    SHCK_EXPP_TAR_REG = EXPP_TAR_REG_ARAT - movavg(EXPP_TAR_REG_ARAT{-1}, -8);
    
    
  'Identities'
        DOT_LPOIL_USD_BASE = 4*(LPOIL_USD_BASE - LPOIL_USD_BASE{-1});
        DOT4_LPOIL_USD_BASE = LPOIL_USD_BASE - LPOIL_USD_BASE{-4};
        
%

%% Parameters 

!parameters

  'Federal gov. non-oil revenue'
    rho_tau_fed_eq  = 0.85;
    rho_tau_fed_gap = 0.50;
    
  'Federal gov. oil revenue'
    REV_O_BASE_ARAT_SS  = 0;
    rho_err_rev_o_base  = 0.85; 
    rho_shck_poil_base  = 0.9999;     
    phi_rev_o_extra     = 0.05;
    rho_err_rev_o_extra = 0.80;
    w_oil_fisc_lag      = 0.50;
    
  'Federal gov. expenditure'
    rho_expp_fed = 0.50;
    phi_cycl_fed = 0.20; 
    rho_expp_str_fed = 0.85; 
    phi_debt_dev = 0.10;
    
  'Federal gov. debt'
    rho_auto;
    DEBT_FED_ARAT_SS = 0; 
    rho_err_debt_fed = 0.55;
    w_debt_fin = 0.82;
    rho_rw     = 0.99999;
    
  'Regional gov. revenue'
    rho_tau_reg_eq  = 0.75;
    rho_tau_reg_gap = 0.60; 
    
  'Regional gov. expenditure'
    rho_expp_reg = 0.65;
    phi_cycl_reg = 0.075; 
    rho_expp_str_reg = 0.80;
    
  'Fiscal stimulus'
    phi_rev = 0.80;
    phi_exp = 0.55; 
    rho_fisc = 0.30;
    
  'Standard deviations'    
    std_RES_TAU_NO_FED_EQ  = 0.25; 
    std_RES_TAU_NO_FED_TAR = 0.10;
    std_RES_TAU_NO_FED_GAP = 0.60;    
    std_RES_REV_O_BASE_ARAT   = 0.05;
    std_RES_REV_O_EXTRA_ARAT  = 0.75;
    std_RES_LPOIL_USD_BASE    = 5;  
    %    
    std_RES_EXPP_FED_ARAT      = 1.00;
    std_RES_EXPP_STR_FED_ARAT  = 0.25;
    std_RES_EXPP_DISC_FED_ARAT = 0.10;
    %
    std_RES_DEBT_FED_ARAT = 0.70;
    std_RES_DEBT_FED_TAR_ARAT = 0.10;
    %
    std_RES_TAU_REG_EQ  = 0.20;
    std_RES_TAU_REG_TAR = 0.10;
    std_RES_TAU_REG_GAP = 0.60;
    %
    std_RES_EXP_DEBT_REG_ARAT = 0.05;
    std_RES_EXPP_REG_ARAT     = 0.65;
    std_RES_EXPP_STR_REG_ARAT = 0.20;
    std_RES_EXPP_TAR_REG_ARAT = 0.10;
    %
    std_RES_FISC_IMP_REV_REG_DISC = 0.10;
    std_RES_FISC_IMP_EXP_REG_DISC = 0.10;
    
!links
    rho_auto = exp(-(DOT_Y_SS + PIE_TAR_SS)/4/100);  

%

%% Transition shocks
        
!transition_shocks

  'Federal government eq. effective non-oil tax rate shock'   RES_TAU_NO_FED_EQ
  'Fed. gov. implied target effective non-oil tax rate shock' RES_TAU_NO_FED_TAR
  'Federal government effective non-oil tax rate gap shock'   RES_TAU_NO_FED_GAP
  'Fed. gov. welfare-fund-financed revenue ratio shock'       RES_REV_WF_FED_ARAT
  'Base oil&gas revenue ratio shock'                          RES_REV_O_BASE_ARAT
  'Extra oil&gas revenue ratio shock'                         RES_REV_O_EXTRA_ARAT  
  'Base oil price shock'                                      RES_LPOIL_USD_BASE
  'Federal gov. debt service expenditure ratio shock'         RES_EXP_DEBT_FED_ARAT  
  'Federal government primary expenditure ratio shock'        RES_EXPP_FED_ARAT
  'Fed. gov. structural primary expenditure ratio shock'      RES_EXPP_STR_FED_ARAT
  'Fed. gov. statutory discr. primary expend. ratio shock'    RES_EXPP_DISC_FED_ARAT
  'Federal government debt ratio shock'                       RES_DEBT_FED_ARAT
  'Federal government target debt ratio shock'                RES_DEBT_FED_TAR_ARAT
   %
  'Regional government eq. effective non-oil tax rate shock'  RES_TAU_REG_EQ
  'Reg. gov. implied target effective non-oil tax rate shock' RES_TAU_REG_TAR
  'Regional government effective non-oil tax rate gap shock'  RES_TAU_REG_GAP
  'Regional gov. debt service expenditure ratio shock'        RES_EXP_DEBT_REG_ARAT
  'Regional government primary expenditure ratio shock'       RES_EXPP_REG_ARAT
  'Reg. gov. structural primary expenditure ratio shock'      RES_EXPP_STR_REG_ARAT
  'Reg. gov. implied target primary expenditure ratio shock'  RES_EXPP_TAR_REG_ARAT
  'Fiscal impulse from discret. reg. gov. revenue shock'      RES_FISC_IMP_REV_REG_DISC
  'Fiscal impulse from discret. reg. gov. expenditure shock'  RES_FISC_IMP_EXP_REG_DISC

%
      
!transition_equations

  
  
    EXP_DEBT_FED_ARAT = EXP_DEBT_FED_ARAT{-1} + RES_EXP_DEBT_FED_ARAT;   

     
    
!parameters
 
    phi_debt_tar = 1.00;



  
%

%% Measurement variables: observables

!measurement_variables

  'Observed REV_FED_ARAT'      OBS_REV_FED_ARAT
  'Observed REV_NO_FED_ARAT'   OBS_REV_NO_FED_ARAT
  'Observed REV_O_ARAT'        OBS_REV_O_ARAT
  'Observed REV_O_BASE_ARAT'   OBS_REV_O_BASE_ARAT
  'Observed LPOIL_USD_BASE'    OBS_LPOIL_USD_BASE
  'Observed REV_WF_FED_ARAT'   OBS_REV_WF_FED_ARAT
  'Observed EXP_FED_ARAT'      OBS_EXP_FED_ARAT
  'Observed EXP_DEBT_FED_ARAT' OBS_EXP_DEBT_FED_ARAT
  'Observed DEBT_FED_ARAT'     OBS_DEBT_FED_ARAT
  %
  'Observed REV_REG_ARAT'      OBS_REV_REG_ARAT
  'Observed EXP_REG_ARAT'      OBS_EXP_REG_ARAT
  'Observed EXP_DEBT_REG_ARAT' OBS_EXP_DEBT_REG_ARAT

!measurement_equations

    OBS_REV_FED_ARAT      = REV_FED_ARAT;
    OBS_REV_NO_FED_ARAT   = REV_NO_FED_ARAT;
    OBS_REV_O_ARAT        = REV_O_ARAT;
    OBS_REV_O_BASE_ARAT   = REV_O_BASE_ARAT;
    OBS_LPOIL_USD_BASE    = LPOIL_USD_BASE;
    OBS_REV_WF_FED_ARAT   = REV_WF_FED_ARAT;
    OBS_EXP_FED_ARAT      = EXP_FED_ARAT;
    OBS_EXP_DEBT_FED_ARAT = EXP_DEBT_FED_ARAT;
    OBS_DEBT_FED_ARAT     = DEBT_FED_ARAT;
    %
    OBS_REV_REG_ARAT      = REV_REG_ARAT;
    OBS_EXP_REG_ARAT      = EXP_REG_ARAT;
    OBS_EXP_DEBT_REG_ARAT = EXP_DEBT_REG_ARAT;
   
%

%% Measurement variables: tunes

!measurement_variables

  TUNE_TAU_NO_FED_EQ
  TUNE_TAU_NO_FED_TAR
  TUNE_TAU_NO_FED_GAP
  TUNE_REV_O_ARAT
  TUNE_REV_O_BASE_ARAT
  TUNE_REV_O_EXTRA_ARAT
  TUNE_DOT_LPOIL_USD_BASE
  TUNE_LPOIL_USD_BASE
  TUNE_EXPP_DISC_FED_ARAT
  TUNE_DEBT_FED_TAR_ARAT
  TUNE_TAU_REG_EQ
  TUNE_TAU_REG_TAR
  TUNE_EXPP_STR_REG_ARAT
  TUNE_EXPP_TAR_REG_ARAT
  TUNE_FISC_IMP_REV_REG_DISC
  TUNE_FISC_IMP_EXP_REG_DISC

!measurement_equations

    TUNE_TAU_NO_FED_EQ         = TAU_NO_FED_EQ;
    TUNE_TAU_NO_FED_TAR        = TAU_NO_FED_TAR + RES_TUNE_TAU_NO_FED_TAR;
    TUNE_TAU_NO_FED_GAP        = TAU_NO_FED_GAP;
    TUNE_REV_O_ARAT            = REV_O_ARAT;
    TUNE_REV_O_BASE_ARAT       = REV_O_BASE_ARAT;
    TUNE_REV_O_EXTRA_ARAT      = REV_O_EXTRA_ARAT;
    TUNE_DOT_LPOIL_USD_BASE    = DOT_LPOIL_USD_BASE;
    TUNE_LPOIL_USD_BASE        = LPOIL_USD_BASE;
    TUNE_EXPP_DISC_FED_ARAT    = EXPP_DISC_FED_ARAT;
    TUNE_DEBT_FED_TAR_ARAT     = DEBT_FED_TAR_ARAT;
    TUNE_TAU_REG_EQ            = TAU_REG_EQ;
    TUNE_TAU_REG_TAR           = TAU_REG_TAR + RES_TUNE_TAU_REG_TAR;
    TUNE_EXPP_STR_REG_ARAT     = EXPP_STR_REG_ARAT;
    TUNE_EXPP_TAR_REG_ARAT     = EXPP_TAR_REG_ARAT + RES_TUNE_EXPP_TAR_REG_ARAT;
    TUNE_FISC_IMP_REV_REG_DISC = FISC_IMP_REV_REG_DISC;
    TUNE_FISC_IMP_EXP_REG_DISC = FISC_IMP_EXP_REG_DISC;

!measurement_shocks

  RES_TUNE_TAU_NO_FED_TAR
  RES_TUNE_TAU_REG_TAR
  RES_TUNE_EXPP_TAR_REG_ARAT
   
!parameters

  std_RES_TUNE_TAU_NO_FED_TAR    = 0.10;
  std_RES_TUNE_TAU_REG_TAR       = 0.10;
  std_RES_TUNE_EXPP_TAR_REG_ARAT = 0.10;   
%
