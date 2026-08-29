
%% external_model.mod
%
% Terms of trade & external economy model
%

%% Terms of trade modelrh

!transition_variables
  'Oil price, basket (100*log)'                     LPOIL
  'Oil price, USD (100*log)'                        LPOIL_USD
  'USD oil price approximation error (p.p.)'        ERR_LPOIL_USD   
  'Change in oil price (%QoQ @ar)'                  DOT_LPOIL
  'Change in oil price (%YoY)'                      DOT4_LPOIL
  'Equilibirum oil price, basket (100*log)'         LPOIL_EQ
  'Change in eq. oil price (%QoQ @ar)'              DOT_LPOIL_EQ
  'Change in eq. oil price (%YoY)'                  DOT4_LPOIL_EQ
  'Change in USD oil price (%QoQ @ar)'              DOT_LPOIL_USD  
  'Change in USD oil price (%YoY)'                  DOT4_LPOIL_USD
  'Terms of trade, 100*log'                         LTOT 
  'Change in terms of trade (%QoQ @ar)'             DOT_LTOT
  'Expected 1q ahead terms of trade'                E1_LTOT        
  'Equilibrium terms of trade (100*log)'            LTOT_EQ
  'Change in equilibrium terms of trade (%QoQ @ar)' DOT_LTOT_EQ  
  'Terms of trade gap (%)'                          LTOT_GAP
  'EUR/USD exchange rate (100*log)'                 L_EUR_USD
  'EUR/USD exchange rate depreciation (% QoQ ann.)' DOT_L_EUR_USD  
  
!transition_shocks
  'Growth in eq. terms of trade shock (p.p.)'       RES_DOT_LTOT_EQ
  'Terms of trade gap shock (p.p.)'                 RES_LTOT_GAP
  'Approximation error in LPOIL_USD'                RES_LPOIL_USD
  'EUR/USD exchange rate depreciation shock (p.p.)' RES_DOT_L_EUR_USD  
  
!transition_equations
  'Terms of trade'
    LTOT    = LPOIL - LCPIF;    
    LTOT    = LTOT_EQ + LTOT_GAP;
    DOT_LTOT_EQ = rho_tot_eq*DOT_LTOT_EQ{-1} + (1-rho_tot_eq)*DOT_LTOT_SS + RES_DOT_LTOT_EQ;
    LTOT_GAP    = rho_tot_gap*LTOT_GAP{-1} + RES_LTOT_GAP;     
    
    DOT_LPOIL_EQ = DOT_LTOT_EQ + PIEF_SS;
    
    LPOIL_USD = LPOIL + (1-w_usd)*L_EUR_USD + ERR_LPOIL_USD;
    ERR_LPOIL_USD = ERR_LPOIL_USD{-1} + RES_LPOIL_USD;
    
        DOT_LPOIL   = 4*(LPOIL - LPOIL{-1});
        DOT_LTOT    = 4*(LTOT - LTOT{-1});
        DOT_LTOT_EQ = 4*(LTOT_EQ - LTOT_EQ{-1});
        DOT_LPOIL_EQ = 4*(LPOIL_EQ - LPOIL_EQ{-1});
        DOT4_LPOIL_EQ = LPOIL_EQ - LPOIL_EQ{-4};        
        DOT4_LPOIL = LPOIL - LPOIL{-4};
        DOT_LPOIL_USD = 4*(LPOIL_USD - LPOIL_USD{-1});        
        DOT4_LPOIL_USD = LPOIL_USD - LPOIL_USD{-4};
        E1_LTOT = LTOT{+1};    
    
  'EUR/USD exchange rate'
    DOT_L_EUR_USD = rho_eur_usd*DOT_L_EUR_USD{-1} + RES_DOT_L_EUR_USD;

        DOT_L_EUR_USD = 4*(L_EUR_USD - L_EUR_USD{-1});       
    
!parameters  
    DOT_LTOT_SS = 0;
    rho_tot_eq  = 0.90;
    rho_tot_gap = 0.80;
    w_usd       = 0.55;  
    rho_eur_usd = 0;   

    std_RES_DOT_LTOT_EQ   = 2;
    std_RES_LTOT_GAP      = 20;   
    std_RES_LPOIL_USD     = 0.95;
    std_RES_DOT_L_EUR_USD = 15.00;    
    
    
!measurement_variables
'Observed LPOIL'     OBS_LPOIL
'Observed LPOIL_USD' OBS_LPOIL_USD
'Observed L_EUR_USD' OBS_L_EUR_USD

'Tuned LTOT_EQ'      TUNE_LTOT_EQ
'Tuned DOT_LTOT_EQ'  TUNE_DOT_LTOT_EQ
'Tuned LTOT_GAP'     TUNE_LTOT_GAP

!measurement_equations
OBS_LPOIL        = LPOIL;
OBS_LPOIL_USD    = LPOIL_USD;
OBS_L_EUR_USD    = L_EUR_USD;

TUNE_LTOT_EQ     = LTOT_EQ;
TUNE_DOT_LTOT_EQ = DOT_LTOT_EQ;
TUNE_LTOT_GAP    = LTOT_GAP;


%% External economy model: transition variables

!transition_variables
  'Foreign output (100*log)'                           YF
  'Foreign potential output (100*log)'                 YF_EQ
  'Foreign supply shock (p.p.)'                        SHCK_YF_EQ
  'Effective eq. foreign output growth (%QoQ @ar)'     DOT_YF_EQ_EFF  
  'Foreign output gap (%)'                             YF_GAP  
  'Exp. 1Q ahead foreign output gap (%)'               E1_YF_GAP
  'Foreign output growth (% QoQ, ann.)'                DOT_YF
  'Foreign output growth (% YoY)'                      DOT4_YF
  'Foreign potential output growth (% QoQ, ann.)'      DOT_YF_EQ
  'Foreign potential output growth (% YoY)'            DOT4_YF_EQ
  %
  'Foreign level of CPI (100*log)'                     LCPIF
  'Foreign level of core CPI (100*log)'                LCPIF_C
  'Foreign CPI inflation (% QoQ ann.)'                 PIEF
  'Foreign CPI inflation (% YoY)'                      PIEF4  
  'Foreign core CPI inflation (% QoQ ann.)'            PIEF_C
  'Foreign core CPI inflation (% YoY)'                 PIEF_C4
  'Exp. 4Q ahead core CPIF inflation(% YoY)'           E4_PIEF_C4
  %
  'Foreign relative price (100*log)'                   LRPF
  'Eq. foreign relative price (100*log)'               LRPF_EQ
  'Foreign relative price gap (%)'                     LRPF_GAP
  'Growth of eq. foreign relative price (%)'           DOT_LRPF_EQ
  %
  'Foreign nominal interest rate (% p.a.)'             RSF
  'Neutral foreign nominal interest rate (% p.a.)'     RSF_NEUTRAL
  'Foreign CPI inflation target (% QoQ ann.)'          PIEF_TAR
  'Foreign CPI inflation target (% YoY)'               PIEF_TAR4
  'Exp. 3Q ahead core CPIF inflation (% YoY)'          E3_PIEF_C4  
  'Exp. 3Q ahead foreign CPI inflation target (% YoY)' E3_PIEF_TAR4
  'Foreign real interest rate (% p.a.)'                RRF
  'Exp. 1Q ahead foreign CPI inflation (% p.a.)'       E1_PIEF  
  'Exp. 1Q ahead foreign core CPI inflation (% p.a.)'  E1_PIEF_C
  'Eq. foreign real interest rate (% p.a.)'            RRF_EQ
  'Foreign real interest rate gap (% p.a.)'            RRF_GAP
  'Z-factor of eq. foreign RR (% p.a.)'                ZF
  %
  'Foreign 1Y nominal interest rate (% p.a.)'          RSF1
  'Foreign 1Y real interest rate (% p.a.)'             RRF1
  'Eq. foreign 1Y real interest rate (% p.a.)'         RRF1_EQ
  'Foreign 1Y real interest rate gap (p.p.)'           RRF1_GAP
  'Foreign 10Y nominal gov. bonds yield (% p.a.)'      RSGF10 
  'Exp. 10Y ahead foreign nom. interest rate (% p.a.)' E10Y_RSF
  'Term premium in foreign 10Y gov. bonds (p.p.)'      TPREMF10
  'Eq. term premium in foreign 10Y gov. bonds (p.p.)'  TPREMF10_EQ
  'Term premium gap in foreign 10Y gov. bonds(p.p.)'   TPREMF10_GAP
  'Foreign 10Y real gov. bonds yield (% p.a.)'         RRGF10 
  'Eq. foreign 10Y real gov. bonds yield (% p.a.)'     RRGF10_EQ
  'Foreign 10Y real gov. bonds yield gap (p.p.)'       RRGF10_GAP
  'Exp. 10Y ahead foreign eq. real IR (% p.a.)'        E10Y_RRF_EQ  
  'Exp. 10Y ahead foreign core CPI inflation (% p.a.)' E10Y_PIEF_C10Y
  'Foreign average real interest rate gap (p.p.)'      RRAF_GAP

%

%% External economy model: transition shocks

!transition_shocks

%- Foreign economy
  'Foreign output gap shock (p.p.)'                            RES_YF_GAP
  'Foreign potential output level shock'                       RES_YF_EQ  
  'Foreign potential GDP growth shock (p.p.)'                  RES_DOT_YF_EQ
  'Foreign core CPI inflation shock (p.p.)'                    RES_PIEF_C
  'Eq. foreign relative price shock (p.p.)'                    RES_DOT_LRPF_EQ
  'Foreign relative price gap shock (p.p.)'                    RES_LRPF_GAP
  'Foreign monetary policy shock (p.p.)'                       RES_RSF
  'Foreign CPI inflation target shock (p.p.)'                  RES_PIEF_TAR
  'Foreign z-factor shock (p.p.)'                              RES_ZF
  'Shock in foreign 10Y gov. bonds yield (p.p.)'               RES_RSGF10
  'Shock in eq. term premium in foreign 10Y gov. bonds (p.p.)' RES_TPREMF10_EQ
  'Shock in term premium gap in foreign 10Y gov. bonds (p.p.)' RES_TPREMF10_GAP
 
%

%% External economy model: transition equations

!transition_equations

  'Aggregate demand & potential growth'
    YF_GAP = a_lead_f*E1_YF_GAP + a_lag_f*YF_GAP{-1} ...
             - a_rrf*RRAF_GAP + RES_YF_GAP;     

    YF = YF_EQ + YF_GAP;
    
    YF_EQ = YF_EQ{-1} + 0.25*DOT_YF_EQ + SHCK_YF_EQ;
    
    SHCK_YF_EQ = rho_shck_yf_eq*SHCK_YF_EQ{-1} + RES_YF_EQ;
        DOT_YF_EQ_EFF = DOT_YF_EQ + 4*SHCK_YF_EQ;    

    DOT_YF_EQ = rho_yf_eq*DOT_YF_EQ{-1} + (1-rho_yf_eq)*DOT_YF_SS + RES_DOT_YF_EQ;

        E1_YF_GAP  = YF_GAP{+1};
        DOT_YF     = 4*(YF - YF{-1});
        DOT4_YF    = YF - YF{-4};
        DOT4_YF_EQ = YF_EQ - YF_EQ{-4};
    
  'Core Phillips curve'

    PIEF_C = (1-c_lead_f-c_lag_f)*PIEF_TAR + c_lead_f*E4_PIEF_C4 + c_lag_f*PIEF_C4{-1} ...
             + c_yf*YF_GAP{-1} - c_suppl_f*k_std_f*SHCK_YF_EQ + RES_PIEF_C;
        
    PIEF_TAR = rho_pief_tar*PIEF_TAR{-1} + (1-rho_pief_tar)*PIEF_SS ...
                + c_pie_dev*(PIEF_C4{-1}-PIEF_TAR4{-1}) + RES_PIEF_TAR;
   
        PIEF       = 4*(LCPIF - LCPIF{-1});
        PIEF4      = LCPIF - LCPIF{-4};            
        PIEF_C     = 4*(LCPIF_C - LCPIF_C{-1});
        PIEF_C4    = LCPIF_C - LCPIF_C{-4};    
        E4_PIEF_C4 = PIEF_C4{+4};     
    
  'Relative prices'    
    LRPF = LCPIF_C - LCPIF;
    LRPF = LRPF_EQ + LRPF_GAP;

    DOT_LRPF_EQ = rho_lrp_eq*DOT_LRPF_EQ{-1} + (1-rho_lrp_eq)*DOT_LRPF_SS + RES_DOT_LRPF_EQ;

    LRPF_GAP = rho_lrp_gap*LRPF_GAP{-1} - c_lrp_tot*LTOT_GAP + RES_LRPF_GAP;

        DOT_LRPF_EQ = 4*(LRPF_EQ - LRPF_EQ{-1});   
    
  'Monetary policy rule'
    RSF = rho_rsf*RSF{-1} + (1-rho_rsf)*( RSF_NEUTRAL ...
          + phi_pief*(E3_PIEF_C4-E3_PIEF_TAR4) ...
          + phi_yf*YF_GAP ) + RES_RSF;

    RSF_NEUTRAL = RRF_EQ + E3_PIEF_C4;

    RRF = RSF - E1_PIEF_C;
  
        E3_PIEF_C4   = PIEF_C4{+3}; 
        PIEF_TAR4    = (PIEF_TAR + PIEF_TAR{-1} + PIEF_TAR{-2} + PIEF_TAR{-3})/4;
        E3_PIEF_TAR4 = PIEF_TAR4{+3};
        E1_PIEF      = PIEF{+1};
        E1_PIEF_C    = PIEF_C{+1};
            
  'Equilibrium real interest rate'
    RRF_EQ = RRF_SS + h_rrf_y*(DOT_YF_EQ-DOT_YF_SS) + ZF;

    ZF = rho_zf*ZF{-1} + RES_ZF;
    RRF = RRF_EQ + RRF_GAP;
           
  'Long-term interest rates: 1Y-rate'
    RSF1    = movavg(RSF, +4);
    RRF1    = RSF1 - E4_PIEF_C4;
    RRF1    = RRF1_EQ + RRF1_GAP;
    RRF1_EQ = movavg(RRF_EQ, +4);
  
  'Long-term interest rates: 10 government bonds'
    RSGF10 = E10Y_RSF + TPREMF10 + RES_RSGF10;
        
    TPREMF10     = TPREMF10_EQ + TPREMF10_GAP;
    TPREMF10_EQ  = TPREMF10_EQ{-1} + RES_TPREMF10_EQ;
    TPREMF10_GAP = rho_tpremf_gap*TPREMF10_GAP{-1} + RES_TPREMF10_GAP;
    
    RRGF10 = RSGF10 - E10Y_PIEF_C10Y;
    RRGF10 = RRGF10_EQ + RRGF10_GAP;   
    RRGF10_EQ = E10Y_RRF_EQ + TPREMF10_EQ;
    
    RRAF_GAP  = wf_1y*RRF1_GAP + wf_10y*RRGF10_GAP;
    
        E10Y_RSF       = movavg(RSF, +40);
        E10Y_PIEF_C10Y = movavg(PIEF_C, +40);
        E10Y_RRF_EQ    = movavg(RRF_EQ, +40);   
    
%

%% External economy model: parameters

!parameters
    a_lead_f        = 0.12;
    a_lag_f         = 0.72;
    a_rrf           = 0.10;
    rho_shck_yf_eq  = 0.35;
    rho_yf_eq       = 0.85;
    DOT_YF_SS       = 100*log(1+1.65/100);
    %
    c_lead_f = 0.50;
    c_lag_f  = 0.30;
    c_yf     = 0.10;
    c_suppl_f = 0.30;
    rho_pief_tar  = 0.85;
    c_pie_dev     = 0.10;
    %
    rho_lrp_eq  = 0.95; 
    DOT_LRPF_SS = 0;
    rho_lrp_gap = 0.50; 
    c_lrp_tot   = 0.01;
    %
    rho_rsf      = 0.85;
    phi_pief     = 0.50;
    phi_yf       = 0.40;
   
    PIEF_SS      = 100*log(1+2.0/100);
    
    RS_US_SS     = 3.25;
    RR_US_SS     = 100 * (1+RS_US_SS/100) / (1+2.0/100) - 100;
    RS_EU_SS     = 2.25;
    RR_EU_SS     = 100 * (1+RS_EU_SS/100) / (1+2.0/100) - 100;
    RRF_SS       = 100*log( (1+RR_EU_SS/100)^0.45 * (1+RR_US_SS/100)^0.55 );
    
    h_rrf_y =  0.75;
    rho_zf = 0.80; 
    %
    rho_tpremf_gap  = 0.75; 
    wf_1y           = 0.40;
    wf_10y          = 0.60;
    %
    std_RES_YF_GAP        = 1.25;
    std_RES_YF_EQ         = 0.10;
    std_RES_DOT_YF_EQ     = 0.15;
    std_RES_PIEF_C        = 0.35;
    k_std_f               = std_RES_PIEF_C / std_RES_YF_EQ;   
    std_RES_DOT_LRPF_EQ   = 0.05;
    std_RES_LRPF_GAP      = 0.20;
    std_RES_RSF           = 0.30;
    std_RES_PIEF_TAR      = 0.05;
    std_RES_ZF            = 0.10;
    std_RES_TPREMF10_EQ   = 0.05;
    std_RES_TPREMF10_GAP  = 0.30;
    std_RES_RSGF10        = 0.30;

%

%% External economy model: observables

!measurement_variables
'Observed YF'        OBS_YF
'Observed LCPIF'     OBS_LCPIF
'Observed LCPIF_C'   OBS_LCPIF_C
'Observed RSF'       OBS_RSF
'Observed RSGF10'    OBS_RSGF10

!measurement_equations
OBS_YF        = YF;
OBS_LCPIF     = LCPIF;
OBS_LCPIF_C   = LCPIF_C;
OBS_RSF       = RSF;
OBS_RSGF10    = RSGF10;

%

%% Tunes

!measurement_variables
'Tuned DOT_YF'         TUNE_DOT_YF
'Tuned YF_GAP'         TUNE_YF_GAP
'Tuned DOT_YF_EQ'      TUNE_DOT_YF_EQ
'Tuned E1_PIEF_C'      TUNE_E1_PIEF_C
'Tuned E3_PIEF_C4'     TUNE_E3_PIEF_C4
'Tuned E4_PIEF_C4'     TUNE_E4_PIEF_C4
'Tuned E10Y_PIEF_C10Y' TUNE_E10Y_PIEF_C10Y
'Tuned PIEF_TAR'       TUNE_PIEF_TAR
'Tuned LRPF_GAP'       TUNE_LRPF_GAP
'Tuned DOT_LRPF_EQ'    TUNE_DOT_LRPF_EQ
'Tuned RRF_EQ'         TUNE_RRF_EQ
'Tuned ZF'             TUNE_ZF
'Tuned E10Y_RSF'       TUNE_E10Y_RSF
'Tuned TPREMF10'       TUNE_TPREMF10
'Tuned TPREMF10_GAP'   TUNE_TPREMF10_GAP
                            
!measurement_equations
TUNE_DOT_YF         = DOT_YF;
TUNE_YF_GAP         = YF_GAP + RES_TUNE_YF_GAP;
TUNE_DOT_YF_EQ      = DOT_YF_EQ;
TUNE_E1_PIEF_C      = E1_PIEF_C;
TUNE_E3_PIEF_C4     = E3_PIEF_C4;
TUNE_E4_PIEF_C4     = E4_PIEF_C4;
TUNE_E10Y_PIEF_C10Y = E10Y_PIEF_C10Y;
TUNE_PIEF_TAR       = PIEF_TAR;
TUNE_DOT_LRPF_EQ    = DOT_LRPF_EQ;
TUNE_LRPF_GAP       = LRPF_GAP;
TUNE_RRF_EQ         = RRF_EQ;
TUNE_ZF             = ZF;
TUNE_E10Y_RSF       = E10Y_RSF;
TUNE_TPREMF10       = TPREMF10;
TUNE_TPREMF10_GAP   = TPREMF10_GAP;

!measurement_shocks
RES_TUNE_YF_GAP

!parameters
std_RES_TUNE_YF_GAP = 0.50;

