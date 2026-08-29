
%% qpm_term_structure.mod
%
% Term structure block of QPM for Russia
%

%% Variables' declaration

!transition_variables

 !for
  ?t = 1, 2, 3, 5, 7, 10
 !do
  'Nominal gov. bond (OFZ) ?tY zero coupon yield (%p.a.)'      RSG?t
  '?tY expectations of nominal interest rate (%p.a.)'          E?tY_RS  
  'Bias in ?tY expectations of nominal interest rate (p.p.)'   E?tY_RS_BIAS
  'Weighted ?tY expectations of nominal interest rate (%p.a.)' EW?tY_RS
  'Term premium in ?tY OFZ zero coupon yield (p.p.)'           TPREM?t
  'Eq. term premium in ?tY OFZ zero coupon yield (p.p.)'       TPREM?t_EQ
  'Slope factor in ?tY OFZ zero coupon yield (p.p.)'           SLOPE?t
  'Eq. slope factor in ?tY OFZ zero coupon yield (p.p.)'       SLOPE?t_EQ
  'Curvature factor in ?tY OFZ zero coupon yield (p.p.)'       CURV?t
  'Eq. curvature factor in ?tY OFZ zero coupon yield (p.p.)'   CURV?t_EQ
  '?tY expectations of real interest rate (%p.a.)'             E?tY_RR_EQ
  '?tY inflation expectations (%YoY)'                          E?tY_PIE?tY
  'Weighted ?tY inflation expectations (%YoY)'                 EW?tY_PIE?tY
  'Real gov. bond (OFZ) ?tY zero coupon yield (%p.a.)'         RRG?t
  'Eq. real gov. bond (OFZ) ?tY zero coupon yield (%p.a.)'     RRG?t_EQ
  'Gov. bond (OFZ) ?tY zero coupon yield gap (p.p)'            RRG?t_GAP
  'Neutral nom. gov. bond (OFZ) ?tY zero coupon yield (%p.a.)' RSG?t_EQ
  'Long-term neutr. nom. gov. bond (OFZ) ?tY ZC yield (%p.a.)' RSG?t_NEUTRAL_TAR  
 !end
  %
  'Sovereign risk premium in OFZ in short maturities (p.p.)'   GPREM_SM
  'Sovereign risk premium in OFZ in long maturities (p.p.)'    GPREM_LM
  'Term premium in long maturity OFZ (p.p.)'                   TPREM_LM
  'Eq. term premium in long maturity OFZ (p.p.)'               TPREM_LM_EQ
  'Term premium in long maturity OFZ gap (p.p.)'               TPREM_LM_GAP
  'Shock in term premium in long maturity OFZ gap (p.p.)'      SHCK_TPREM_LM_GAP
  'Slope common factor in OFZ (p.p.)'                          SLOPE
  'Eq. slope common factor in OFZ (p.p.)'                      SLOPE_EQ
  'Slope common factor in OFZ gap (p.p.)'                      SLOPE_GAP
  'Curvature common factor in OFZ (p.p.)'                      CURV
  'Eq. curvature common factor in OFZ (p.p.)'                  CURV_EQ
  'Curvature common factor in OFZ gap (p.p.)'                  CURV_GAP
  %
  'Nominal credit rate up to 1Y (%p.a.)'                       RSM1
  'Nominal credit rate above 1Y (%p.a.)'                       RSM3 
  'Credit premium in rates up to 1Y (p.p.)'                    CPREM1
  'Eq. credit premium in rates up to 1Y (p.p.)'                CPREM1_EQ
  'Long-run credit premium in rates up to 1Y (p.p.)'           CPREM1_LR
  'Credit premium gap in rates up to 1Y (p.p.)'                CPREM1_GAP  
  'Credit premium in rates above 1Y (p.p.)'                    CPREM3
  'Eq. credit premium in rates above 1Y (p.p.)'                CPREM3_EQ
  'Long-run credit premium in rates above 1Y (p.p.)'           CPREM3_LR
  'Credit premium gap in rates above 1Y (p.p.)'                CPREM3_GAP
  'Real credit rate up to 1Y (%p.a.)'                          RRM1
  'Eq. real credit rate up to 1Y (%p.a.)'                      RRM1_EQ
  'Real credit rate gap up to 1Y (%p)'                         RRM1_GAP
  'Real credit rate above 1Y (%p.a.)'                          RRM3
  'Eq. real credit rate above 1Y (%p.a.)'                      RRM3_EQ
  'Real credit rate gap above 1Y (%p)'                         RRM3_GAP
  'Borrower financial conditions latent variable (p.p.)'       ETA_BRW
  'Lender financial conditions latent variable (p.p.)'         ETA_LND
  'Monetary conditions gap (%)'                                RRA_GAP

  AUX_RES_EW1Y_PIE1Y
  
%

%% Government bond yields' transition equations

!transition_equations

  %- term structure
  !for
    ?t = 1, 2, 3
  !do
     RSG?t = EW?tY_RS + GPREM_SM + TPREM?t + RES_RSG?t;
  !end
  
  !for
    ?t = 5, 7, 10
  !do
    RSG?t = EW?tY_RS + GPREM_LM + TPREM?t + RES_RSG?t;
  !end   
  
  %- sovereign risk premia
    GPREM_SM = rho_gprem_sm*GPREM_SM{-1} + g_prem_sm*PREM_GAP + g_eta*ETA_LND + RES_GPREM_SM; 
    GPREM_LM = rho_gprem_lm*GPREM_LM{-1} + g_prem_lm*PREM_GAP + ...
        g_debt*DEBT_FED_ACCR_ARAT + g_eta*ETA_LND + RES_GPREM_LM;  
  
  %- term premia
  !for
    ?t = 1, 2, 3, 5, 7, 10
  !do       
    TPREM?t    = TPREM_LM - SLOPE?t - CURV?t;
    TPREM?t_EQ = TPREM_LM_EQ - SLOPE?t_EQ - CURV?t_EQ;
    
    SLOPE?t    = SLOPE * (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12);
    SLOPE?t_EQ = SLOPE_EQ * (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12);
    
    CURV?t     = CURV * ( (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12) - exp(-ns_decay*?t*12) );
    CURV?t_EQ  = CURV_EQ * ( (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12) - exp(-ns_decay*?t*12) );
  !end
    
    TPREM_LM     = TPREM_LM_EQ + TPREM_LM_GAP;
    TPREM_LM_EQ  = TPREM_LM_EQ{-1} + RES_TPREM_LM_EQ;
    TPREM_LM_GAP = rho_tprem_lm_gap*TPREM_LM_GAP{-1} + t_premf*TPREMF10_GAP + SHCK_TPREM_LM_GAP;
        SHCK_TPREM_LM_GAP = rho_shck_tprem_lm_gap*SHCK_TPREM_LM_GAP{-1} + RES_TPREM_LM_GAP;

    SLOPE     = SLOPE_EQ + SLOPE_GAP;
    SLOPE_EQ  = rho_slope_eq*SLOPE_EQ{-1} + (1-rho_slope_eq)*SLOPE_SS + RES_SLOPE_EQ;
    SLOPE_GAP = rho_slope_gap*SLOPE_GAP{-1} + RES_SLOPE_GAP;
    
    CURV     = CURV_EQ + CURV_GAP;
    CURV_EQ  = rho_curv_eq*CURV_EQ{-1} + (1-rho_curv_eq)*CURV_SS + RES_CURV_EQ;
    CURV_GAP = rho_curv_gap*CURV_GAP{-1} + RES_CURV_GAP;
  
  %- inflation expectations & real interest rates
  !for
    ?q = 4, 8, 12, 20, 28, 40
  !do
    EW$[?q/4]$Y_RS = rho_exp*EW$[?q/4]$Y_RS{-1} + (1-rho_exp)*E$[?q/4]$Y_RS + E$[?q/4]$Y_RS_BIAS;
    
    E$[?q/4]$Y_RS = gamma1*movavg(RS{-1}, ?q) + (1-gamma1)*( E$[?q/4]$Y_RR_EQ + movavg(E3_PIE_C4, ?q) + gamma2*movavg(E3_PIE4_DEV, ?q) + gamma3*movavg(Y_GAP, ?q) ) + RES_RS/?q;
    E$[?q/4]$Y_RS_BIAS = rho_e_rs_bias * E$[?q/4]$Y_RS_BIAS{-1} + RES_E$[?q/4]$Y_RS_BIAS;
        
    E$[?q/4]$Y_PIE$[?q/4]$Y  = movavg(PIE, ?q);
        
    RRG$[?q/4]$        = RSG$[?q/4]$ - EW$[?q/4]$Y_PIE$[?q/4]$Y;    
    RRG$[?q/4]$        = RRG$[?q/4]$_EQ + RRG$[?q/4]$_GAP;
    RRG$[?q/4]$_EQ     = E$[?q/4]$Y_RR_EQ + TPREM$[?q/4]$_EQ;
    RSG$[?q/4]$_EQ     = RRG$[?q/4]$_EQ + EW$[?q/4]$Y_PIE$[?q/4]$Y;
    E$[?q/4]$Y_RR_EQ   = lappa*E$[?q/4]$Y_RR_EQ{-1} + (1-lappa)*( movavg(RRF_EQ, ?q) + movavg(PREM_EQ, ?q) + E1_DOT_LZ_EQ );    
  !end
  
  %- inflation expectations

    EW1Y_PIE1Y = rho_exp_pie_1y*EW1Y_PIE1Y{-1} + (1-rho_exp_pie_1y)*( ...
                 (1/4)*EW1_PIE_C + (1-1/4)*( ( 4*movavg(PIE_C, 4) - PIE_C{+1} )/(4-1) ) ) + RES_EW1Y_PIE1Y;
             AUX_RES_EW1Y_PIE1Y = RES_EW1Y_PIE1Y;
             
    EW2Y_PIE2Y = rho_exp_pie_2y*EW2Y_PIE2Y{-1} + (1-rho_exp_pie_2y)*( (1/2)*EW1Y_PIE1Y + (1-1/2)*( ( 8*movavg(PIE_C, 8) - 4*movavg(PIE_C, 4) )/(8-4) ) ) + RES_EW2Y_PIE2Y;
    EW3Y_PIE3Y = rho_exp_pie_3y*EW3Y_PIE3Y{-1} + (1-rho_exp_pie_3y)*( (2/3)*EW2Y_PIE2Y + (1-2/3)*( ( 12*movavg(PIE_C, 12) - 8*movavg(PIE_C, 8) )/(12-8) ) ) + RES_EW3Y_PIE3Y;
    EW5Y_PIE5Y = rho_exp_pie_5y*EW5Y_PIE5Y{-1} + (1-rho_exp_pie_5y)*( (3/5)*EW3Y_PIE3Y + (1-3/5)*( ( 20*movavg(PIE_C, 20) - 12*movavg(PIE_C, 12) )/(20-12) ) ) + RES_EW5Y_PIE5Y;
    EW7Y_PIE7Y = rho_exp_pie_7y*EW7Y_PIE7Y{-1} + (1-rho_exp_pie_7y)*( (5/7)*EW5Y_PIE5Y + (1-5/7)*( ( 28*movavg(PIE_C, 28) - 20*movavg(PIE_C, 20) )/(28-20) ) ) + RES_EW7Y_PIE7Y;
    EW10Y_PIE10Y = rho_exp_pie_10y*EW10Y_PIE10Y{-1} + (1-rho_exp_pie_10y)*( (7/10)*EW7Y_PIE7Y + (1-7/10)*( ( 40*movavg(PIE_C, 40) - 28*movavg(PIE_C, 28) )/(40-28) ) ) + RES_EW10Y_PIE10Y;
       

  %- neutral nominal yield curve
  !for
    ?t = 1, 2, 3, 5, 7, 10
  !do
    RSG?t_NEUTRAL_TAR = (RR_EQ + PIE_TAR) + TPREM_LM_EQ - (SLOPE_EQ * (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12)) ...
                         - (CURV_EQ * ( (1 - exp(-ns_decay*?t*12)) / (ns_decay*?t*12) - exp(-ns_decay*?t*12) ));  
  !end
   
  
%
    
%% Government bond yields' parameters     

!parameters
    rho_gprem_sm = 0.40;
    rho_gprem_lm = 0.30;
    g_prem_sm    = 0.70;
    g_prem_lm    = 1.00;
    g_debt    = 0.20;
    g_eta     = 0.10;
    t_premf   = 0.75;     
    %
    rho_tprem_lm_gap = 0.50;
    rho_shck_tprem_lm_gap = 0.75;
    ns_decay  = 0.05;
    rho_slope_eq  = 0.80;
    rho_slope_gap = 0.70;
    SLOPE_SS  = 0; 
    rho_curv_eq  = 0.80;
    rho_curv_gap = 0.80;
    CURV_SS   = 0; 
    %
    std_RES_GPREM_SM     = 0.25;
    std_RES_GPREM_LM     = 0.25;
    std_RES_TPREM_LM_EQ  = 0.10;
    std_RES_TPREM_LM_GAP = 0.25;
    std_RES_SLOPE_EQ     = 0.10;
    std_RES_SLOPE_GAP    = 0.50;
    std_RES_CURV_EQ      = 0.10;
    std_RES_CURV_GAP     = 0.50;
    %
  !for
    ?t = 1, 2, 3, 5, 7, 10
  !do
    RSG?t_SS             = 0;
    std_RES_RSG?t        = 1.5;
    std_RES_E?tY_RS_BIAS = 0.75;
    std_RES_EW?tY_PIE?tY = 0.10;
  !end 
  
  rho_exp        = 0.25; 
  rho_e_rs_bias  = 0.25;
  rho_exp_pie_1y = 0.25;
  rho_exp_pie_2y = 0.30;
  rho_exp_pie_3y = 0.40;
  rho_exp_pie_5y = 0.50;
  rho_exp_pie_7y = 0.50;
  rho_exp_pie_10y = 0.50;
    

  
%

%% Market credit rates' transition equations

!transition_equations

  %- term structure
  !for
    ?t = 1, 3
  !do
     RSM?t = rho_rsm?t*RSM?t{-1} + (1-rho_rsm?t)*(RSG?t + CPREM?t) + RES_RSM?t;
     
     CPREM?t     = CPREM?t_EQ + CPREM?t_GAP;
     CPREM?t_EQ  = rho_cprem?t_eq*CPREM?t_EQ{-1} + (1-rho_cprem?t_eq)*CPREM?t_LR + RES_CPREM?t_EQ;
     CPREM?t_LR  = CPREM?t_LR{-1} + RES_CPREM?t_LR;
     CPREM?t_GAP = rho_cprem?t_gap*CPREM?t_GAP{-1} + psi_eta_brw*ETA_BRW + psi_eta_lnd*ETA_LND + RES_CPREM?t_GAP;
     
     RRM?t    = RSM?t - EW?tY_PIE?tY;
     RRM?t    = RRM?t_EQ + RRM?t_GAP;
     RRM?t_EQ = RRG?t_EQ + CPREM?t_EQ;
  !end
  
  %- financial accelerator
  ETA_BRW = rho_eta_brw*ETA_BRW{-1} - psi_y*Y_GAP - psi_e_y*E1_Y_GAP;
  
  ETA_LND = rho_eta_lnd*ETA_LND{-1} + psi_rr*RS_GAP;
  
  %- monetary conditions
  RRA_GAP = w_ir_1y*RRM1_GAP + w_ir_3y*RRM3_GAP + w_ir_5y*RRG5_GAP + w_ir_10y*RRG10_GAP;

%

%% Market credit rates' parameters

!parameters
  !for
    ?t = 1, 3
  !do
    rho_cprem?t_eq  = 0.75;
    rho_cprem?t_gap = 0.50
    %
    std_RES_RSM?t       = 1.50;
    std_RES_CPREM?t_EQ  = 0.30;
    std_RES_CPREM?t_LR  = 0.20;
    std_RES_CPREM?t_GAP = 0.75;
  !end
  %
  rho_rsm1 = 0.25;
  rho_rsm3 = 0.40;
  %
  psi_eta_brw = 0.15;
  rho_eta_brw = 0.40;
  psi_y       = 0.10;
  psi_e_y     = 0.40;
  %
  psi_eta_lnd = 0.15;
  rho_eta_lnd = 0.30;   
  psi_rr      = 0.15;
  %
  w_ir_1y  = 0.33;
  w_ir_3y  = 0.42;
  w_ir_5y  = 0.14;
  w_ir_10y = 0.11;
  
%

%% Transition shocks

!transition_shocks

 !for
  ?t = 1, 2, 3, 5, 7, 10
 !do
  RES_RSG?t
  RES_E?tY_RS_BIAS
  RES_EW?tY_PIE?tY
 !end
 
  RES_PIE_MP_EXP

  RES_GPREM_SM
  RES_GPREM_LM
  RES_TPREM_LM_EQ
  RES_TPREM_LM_GAP
  
  RES_SLOPE_EQ
  RES_SLOPE_GAP
  RES_CURV_EQ
  RES_CURV_GAP
  
 !for
  ?t = 1, 3
 !do
   RES_RSM?t     
   RES_CPREM?t_EQ
   RES_CPREM?t_LR
   RES_CPREM?t_GAP
 !end    

%

%% Measurement variables: observables

!for
  ?t = 1, 2, 3, 5, 7, 10
!do

  !measurement_variables
  OBS_RSG?t
  
  !measurement_equations
  OBS_RSG?t = RSG?t;
  
!end

!for
  ?t = 1, 3
!do

  !measurement_variables
  OBS_RSM?t
  
  !measurement_equations
  OBS_RSM?t = RSM?t;
  
!end

%

%% Measurement variables: tunes

!for
  ?t = 1, 2, 3, 5, 7, 10
!do

  !measurement_variables
  TUNE_EW?tY_PIE?tY
  
  !measurement_equations
  TUNE_EW?tY_PIE?tY = EW?tY_PIE?tY;
  
!end


!measurement_variables
TUNE_TPREM_LM_EQ
TUNE_SHCK_TPREM_LM_GAP

!measurement_equations
TUNE_TPREM_LM_EQ = TPREM_LM_EQ;
TUNE_SHCK_TPREM_LM_GAP = SHCK_TPREM_LM_GAP;
