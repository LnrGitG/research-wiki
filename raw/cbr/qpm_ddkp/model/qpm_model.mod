
%% qpm_model.mod
%
% QPM for Russia with core inflation, a fiscal block, term structure, 
%  trade block and a labour block
%

%% Import external block model
!import(external_model.mod)
%% Variables' declaration

!transition_variables

%- Output and aggregate demand  
  'Output (100*log)'                                  Y
  'Output growth (%QoQ @ar)'                          DOT_Y
  'Output growth (%YoY)'                              DOT4_Y
  'Seasonal factor of YoY output growth (p.p.)'       DOT4_Y_SF
  'Annual output growth (%YoY)'                       DOT4_Y_MA
  'Equilibrium output (100*log)'                      Y_EQ
  'Eq. output growth (%QoQ @ar)'                      DOT_Y_EQ
  'Eq. output growth with level shocks (%QoQ @ar)'    DOT_Y_EQ_EFF
  'Adj. eq. output grwth with lvl shcks (%QoQ @ar)'   DOT_Y_EQ_EFFX
  'Eq. output growth (%YoY)'                          DOT4_Y_EQ
  'Annual eq. output growth (%YoY)'                   DOT4_Y_EQ_MA
  'Long-run eq. output growth (%QoQ @ar)'             DOT_Y_EQ_LR
  'Output gap (%)'                                    Y_GAP
  'Output gap, 4Q moving average (%)'                 Y_GAP_MA
  'Change in output gap (p.p. QoQ @ar)'               DOT_Y_GAP
  'Expected output gap 1Q ahead (%)'                  E1_Y_GAP
  'Exp. 1Q ahead change in output gap (p.p. QoQ @ar)' E1_DOT_Y_GAP
  'Exp. 1Q ahead output growth (%QoQ @ar)'            E1_DOT_Y
  'Nominal output growth (%YoY)'                      DOT4_Y_NOM
  'Equilibrium nominal output growth (%YoY)'          DOT4_Y_NOM_EQ
  'Nominal output gap, 4Q MA change (p.p.)'           DOT_Y_NOM_MA_GAP
  %
  'Domestic output (100*log)'                         YD
  'Domestic output growth (%QoQ @ar)'                 DOT_YD
  'Domestic output growth (%YoY)'                     DOT4_YD
  'Domestic equilibrium output (100*log)'             YD_EQ
  'Eq. domestic output growth (%QoQ @ar)'             DOT_YD_EQ
  'Effective eq. domestic output growth (%QoQ @ar)'   DOT_YD_EQ_EFF
  'Long-run eq. domestic output growth (%QoQ @ar)'    DOT_YD_EQ_LR
  'Domestic output TFP growth (%QoQ @ar)'             DOT_TFP
  'Domestic output effective TFP growth (%QoQ @ar)'   DOT_TFP_EFF
  'Domestic output effective TFP growth gap (p.p.)'   DOT_TFP_EFF_GAP
  'Exp. domestic output eff. TFP growth gap (p.p.)'   E1_DOT_TFP_EFF_GAP
  'Domestic output long-run TFP growth (%QoQ @ar)'    DOT_TFP_LR
  'Domestic output TFP shock (%)'                     SHCK_TFP
  'Domestic output supply shock (%)'                  SHCK_SUPL
  'Domestic output supply shock, MA (%)'              SHCK_SUPL_MA
  'Domestic output gap (%)'                           YD_GAP
  'Domestic output TFP gap (%)'                       A_D_GAP
  'Domestic output TFP gap, MA (%)'                   A_D_GAP_MA
  'Domestic sector labour demand gap (%)'             L_D_GAP
  'Domestic sector employment gap (%)'                N_D_GAP
  'Domestic sector labour effort gap (%)'             E_D_GAP
  'Domestic sector employm. adjustment costs gap (%)' AC_N_GAP
  'Domestic sector employm. adj. costs gap, MA (%)'   AC_N_GAP_MA
  'Dom. sector employm. effectiveness shock gap (%)'  SHCK_AC_N_GAP
  'Dom. sector employm. effect. shock gap, MA (%)'    SHCK_AC_N_GAP_MA
  'Domestic sector capital utilisation gap (%)'       CU_D_GAP
  'Domestic sector capital rental rate gap (%)'       RK_D_GAP
  'Domestic sector capital rental rate gap (%)'       RK_D_GAP_MA
  'Domestic sector capital adjustment costs gap (%)'  AC_K_GAP
  'Domestic sector capital adj. costs gap, MA (%)'    AC_K_GAP_MA
  'Dom. sector capital effectiveness shock gap (%)'   SHCK_AC_K_GAP
  'Dom. sector capital effect. shock gap, MA (%)'     SHCK_AC_K_GAP_MA
  'Domestic sector imports adjustment costs gap (%)'  AC_M_GAP
  'Domestic sector imports adj. costs gap, MA (%)'    AC_M_GAP_MA
  'Dom. sector imports effectiveness shock gap (%)'   SHCK_AC_M_GAP
  'Dom. sector imports effect. shock gap, MA (%)'     SHCK_AC_M_GAP_MA
  %
  'Domestic demand (100*log)'                         D
  'Domestic demand growth (%QoQ @ar)'                 DOT_D
  'Domestic demand growth (%YoY)'                     DOT4_D
  'Domestic demand annual growth (%YoY)'              DOT4_D_MA
  'Equilibrium domestic demand (100*log)'             D_EQ
  'Eq. domestic demand growth (%QoQ @ar)'             DOT_D_EQ  
  'Eq. domestic demand level shock (p.p.)'            SHCK_D_EQ
  'Eq. dom. demand growth with lvl shocks (%QoQ @ar)' DOT_D_EQ_EFF
  'Eq. domestic demand growth (%YoY)'                 DOT4_D_EQ
  'Annual eq. domestic demand growth (%YoY)'          DOT4_D_EQ_MA
  'Domestic demand gap (%)'                           D_GAP
  'Domestic final demand gap (%)'                     DF_GAP
  'Expected domestic demand gap 1Q ahead (%)'         E1_DF_GAP
  'Domestic final demand shock (%)'                   SHCK_DF_GAP
  'Auxiliary variable for tuning RES_DF_GAP'          AUX_RES_DF_GAP
  %
  'Exports (100*log)'                                 X
  'Exports growth (%QoQ @ar)'                         DOT_X
  'Exports growth (%YoY)'                             DOT4_X
  'Seasonal factor of YoY exports growth (p.p.)'      DOT4_X_SF
  'Annual exports growth (%YoY)'                      DOT4_X_MA
  'Equilibrium exports (100*log)'                     X_EQ
  'Eq. exports growth (%QoQ @ar)'                     DOT_X_EQ
  'Eq. exports growth with level shocks (%QoQ @ar)'   DOT_X_EQ_EFF
  'Eq. exports growth (%YoY)'                         DOT4_X_EQ
  'Annual eq. exports growth (%YoY)'                  DOT4_X_EQ_MA
  'Exports gap (%)'                                   X_GAP
  %
  'Non-oil&gas exports (100*log)'                     X_NO
  'Non-oil&gas exports growth (%QoQ @ar)'             DOT_X_NO
  'Non-oil&gas equilibrium exports (100*log)'         X_NO_EQ
  'Eq. non-oil&gas exports growth (%QoQ @ar)'         DOT_X_NO_EQ
  'Eff. eq. non-oil&gas exports growth (%QoQ @ar)'    DOT_X_NO_EQ_EFF
  'Non-oil&gas exports gap (%)'                       X_NO_GAP
  'Exports output TFP gap (%)'                        A_X_GAP
  'Exports sector labour demand gap (%)'              L_X_GAP
  'Exports sector employment gap (%)'                 N_X_GAP
  'Exports sector labour effort gap (%)'              E_X_GAP
  'Exports sector capital utilisation gap (%)'        CU_X_GAP
  'Exports sector capital rental rate gap (%)'        RK_X_GAP
  %
  'Oil&gas exports (100*log)'                         X_O
  'Oil&gas exports growth (%QoQ @ar)'                 DOT_X_O
  'Oil&gas equilibrium exports (100*log)'             X_O_EQ
  'Eq. oil&gas exports growth (%QoQ @ar)'             DOT_X_O_EQ
  'Eff. eq. oil&gas exports growth (%QoQ @ar)'        DOT_X_O_EQ_EFF
  'Oil&gas exports gap (%)'                           X_O_GAP
  %
  'Imports (100*log)'                                 M
  'Imports growth (%QoQ @ar)'                         DOT_M
  'Imports growth (%YoY)'                             DOT4_M
  'Seasonal factor of YoY imports growth (p.p.)'      DOT4_M_SF
  'Annual imports growth (%YoY)'                      DOT4_M_MA
  'Equilibrium imports (100*log)'                     M_EQ
  'Eq. imports growth (%QoQ @ar)'                     DOT_M_EQ
  'Eq. imports growth with level shocks (%QoQ @ar)'   DOT_M_EQ_EFF  
  'Eq. imports growth (%YoY)'                         DOT4_M_EQ
  'Annual eq. imports growth (%YoY)'                  DOT4_M_EQ_MA
  'Imports gap (%)'                                   M_GAP
  'Intermediate imports gap (%)'                      M_Y_GAP
  'Final goods imports gap (%)'                       M_D_GAP
  
%- Labour block
  'Level of labour force (100*log)'                   LF
  'Labour force growth (%QoQ @ar)'                    DOT_LF
  'Eq. level of labour force (100*log)'               LF_EQ
  'Growth of eq. labour force (% QoQ ann.)'           DOT_LF_EQ
  'Growth of eq. labour force, MA (% QoQ ann.)'       DOT_LF_EQ_MA
  'Labour force gap (%)'                              LF_GAP
  'Aux. variable for eq. labor force level shock'     AUX_RES_LF_EQ
  %
  'Unemployment rate (%)'                             UR
  'Eq. unemployment rate (%)'                         UR_EQ
  'Change of eq. unemployment rate (p.p.)'            DOT_UR_EQ
  'Unemployment rate gap (p.p.)'                      UR_GAP
  'Unemployment gap (p.p.)'                           U_GAP
  'Beginning of period unemployment gap (p.p.)'       UB_GAP
  %
  'Employment growth (%QoQ @ar)'                      DOT_N
  'Level of employment (100*log)'                     N
  'Eq. employment (100*log)'                          N_EQ
  'Eq. employment growth (%QoQ @ar)'                  DOT_N_EQ
  'Eq. employment growth, MA (%QoQ @ar)'              DOT_N_EQ_MA
  'Employment gap (%)'                                N_GAP
  'Aux. variable for eq. employment level shock'      AUX_RES_N_EQ
  %
  'Number of matches gap (%)'                         MATCH_GAP
  'Number of vacancies gap (%)'                       V_GAP
  'Hiring rate gap (%)'                               HR_GAP
  'Expected hiring rate gap (%)'                      E1_HR_GAP
  'Survival rate gap (%)'                             SURV_GAP
  'Expected survival rate gap (%)'                    E1_SURV_GAP
  'Vacancy-filling probability gap (%)'               Q_GAP
  'Job-finding probability gap (%)'                   F_GAP
  'Expected job-finding probability gap (%)'          E1_F_GAP
  'Labour market tightness gap (%)'                   LMT_GAP
  %
  'Shadow real wage gap (%)'                          PW_GAP
  'Shadow real wage gap, MA (%)'                      PW_GAP_MA
  'Nominal wage (100*log)'                            W
  'Nominal wage growth (%QoQ @ar)'                    DOT_W
  'Nominal wage growth (%YoY @ar)'                    DOT4_W
  'Seasonal factor of YoY wage growth (p.p.)'         DOT4_W_SF
  'Real wage (100*log)'                               WR
  'Real wage growth (%QoQ @ar)'                       DOT_WR
  'Real wage growth (%YoY)'                           DOT4_WR
  'Equilibrium real wage (100*log)'                   WR_EQ
  'Equilibrium real wage growth (%QoQ @ar)'           DOT_WR_EQ
  'Equilibrium real wage growth (%YoY)'               DOT4_WR_EQ
  'Real wage gap (%)'                                 WR_GAP
  'Expected real wage gap (%)'                        E1_WR_GAP
  'Optimal real wage gap (%)'                         WRO_GAP
  'Stochastic discount factor gap (%)'                SDF_GAP
  'Adjusted worker bargaining power gap (%)'          CHI_GAP
  'Expected adjusted worker bargaining power gap (%)' E1_CHI_GAP
  'Worker discount factor gap (%)'                    EPS_GAP
  'Expected worker discount factor gap (%)'           E1_EPS_GAP
  'Employment agency discount factor gap (%)'         MU_GAP
  'Exp. employment agency discount factor gap (%)'    E1_MU_GAP
 
%- Aggregate supply: prices
  'Level of headline CPI (100*log)'                   LCPI
  'Headline CPI aggregation wedge (p.p.)'             LCPI_WEDGE
  'Headline CPI inflation (%QoQ @ar)'                 PIE
  'Headline CPI inflation (%YoY)'                     PIE4
  'Seasonal factor of headline CPI inflation (p.p.)'  PIE4_SF
  'Average yearly inflation (%YoY)'                   PIE4_MA
  'QoQ headline inflation gap (p.p.)'                 PIE_GAP
  'Expected QoQ headline inflation gap (p.p.)'        E1_PIE_GAP
  'YoY headline inflation gap (p.p.)'                 PIE4_GAP
  'Domestic CPI inflation (%QoQ @ar)'                 PIE_D
  'Domestic CPI to core CPI rel. price gap (%)'       LRP_D_GAP
  'Domestic CPI to core CPI rel. price gap, MA (%)'   LRP_D_GAP_MA
  'Imported CPI inflation (%QoQ @ar)'                 PIE_M
  'Imported CPI to core CPI rel. price gap (%)'       LRP_M_GAP
  'Domestic real marginal costs gap (%)'              RMC_D_GAP
  'Domestic smoothed real marginal costs gap (%)'     RMC_D_GAP_MA
  'Smoothed employment part of domestic RMC gap (%)'  RMC_N_GAP_MA
  'Smoothed capital part of domestic RMC gap (%)'     RMC_K_GAP_MA
  'Smoothed imports part of domestic RMC gap (%)'     RMC_M_GAP_MA
  'Imported real marginal costs gap (%)'              RMC_IMP_GAP
  'Aggregated real marginal costs gap (%)'            RMC_GAP
  'Aggregated smoothed real marginal costs gap (%)'   RMC_GAP_MA
  %
 !for
  ?X = C, VEG, FUEL, SREG, VOL, NC
 !do
  'Level of ? CPI (100*log)'                          LCPI_?X
  '? CPI inflation (%QoQ @ar)'                        PIE_?X
  '? CPI inflation (%YoY)'                            PIE_?X4
  'Seasonal factor of ? CPI inflation (p.p.)'         PIE_?X4_SF
  'Average yearly ? inflation (%YoY)'                 PIE4_?X_MA
  'QoQ ? inflation gap (p.p.)'                        PIE_?X_GAP
  'YoY ? inflation gap (p.p.)'                        PIE_?X4_GAP
 !end
 !for
  ?X = VEG, FUEL, SREG, VOL
 !do
  '? CPI to core CPI relative price (p.p.)'           LRP_?X
  'Eq. ? CPI to core CPI relative price (p.p.)'       LRP_?X_EQ
  'Change of eq. ? CPI to core CPI rel. price (p.p.)' DOT_LRP_?X_EQ
  '? CPI to core CPI relative price gap (p.p.)'       LRP_?X_GAP
 !end
  'Non-core CPI to core CPI rel. price (p.p.)'        LRP_NC
  'Non-core CPI to core CPI rel. price gap (p.p.)'    LRP_NC_GAP
  'Non-core to core CPI rel. price gap, MA (p.p.)'    LRP_NC_GAP_MA
  'MA-shock in vegetables inflation (p.p.)'           SHCK_PIE_VEG
  'Auxiliary shock variable in veggy infl. (p.p.)'    AUX_RES_PIE_VEG
  %
  'Cost-push shock (p.p.)'                            SHCK_PIE_D
  'Exp. of core inflation 1Q ahead (%QoQ)'            E1_PIE_C
  'Weighted exp. of core infl. 1Q ahead (%QoQ)'       EW1_PIE_C
  'Exp. of dom. core inflation 1Q ahead (%QoQ)'       E1_PIE_D
  'Weighted exp. of dom. core infl. 1Q ahead (%QoQ)'  EW1_PIE_D
  'Exp. of imp. core inflation 1Q ahead (%QoQ)'       E1_PIE_M
  'Weighted exp. of imp. core infl. 1Q ahead (%QoQ)'  EW1_PIE_M
  'GDP deflator (%YoY)'                               DOT4_Y_DEFL
  'GDP deflator approximation error (p.p.)'           ERR_DOT4_Y_DEFL
  'Equilibrium GDP deflator (%YoY)'                   DOT4_Y_DEFL_EQ
  
%- Monetary policy rule
  'Nominal interest rate (%p.a.)'                     RS
  'Neutral nominal interest rate (%p.a.)'             RS_NEUTRAL
  'Interest rate gap w.r.t neutral rate (p.p.)'       RS_GAP
  'Real interest rate (%p.a.)'                        RR
  'Equilibrium real interest rate (%p.a.)'            RR_EQ  
  'Real interest rate gap (p.p.)'                     RR_GAP
  'Expected headline inflation 1Q ahead (%QoQ @ar)'   E1_PIE
  'Inflation target (%QoQ @ar)'                       PIE_TAR
  'Inflation target (%YoY)'                           PIE_TAR4
  'Expected 3Q ahead inflation target (%YoY)'         E3_PIE_TAR4
  'Expected core CPI inflation 3Q ahead (%YoY)'       E3_PIE_C4
  'Expected non-core CPI inflation 3Q ahead (%YoY)'   E3_PIE_NC4
  'Expected headline CPI inflation 3Q ahead (%YoY)'   E3_PIE4  
  'Regul. weighted exp. of infl. 3Q ahead (%YoY)'     E3_PIE4_MP
  'Exp. 3Q ahead yearly inflation deviation (p.p.)'   E3_PIE4_DEV

%- Exchange rates 
  'Nominal exchange rate, basket (100*log)'           LS
  'Nominal exchange rate depreciation (%QoQ @ar)'     DOT_LS
  'Nominal exchange rate depreciation (%YoY)'         DOT4_LS
  'Expected nominal exchange rate 1Q ahead (100*log)' E1_LS
  'Nominal exchange rate, USD/RUB (100*log)'          LS_USD
  'USD/RUB exchange rate depreciation (%QoQ @ar)'     DOT_LS_USD
  'USD/RUB exchange rate depreciation (%YoY)'         DOT4_LS_USD
  'USD/RUB approximation error (p.p.)'                ERR_LS_USD
  'Country risk premium (p.p.)'                       PREM
  'Equilibrium country risk premium (p.p.)'           PREM_EQ
  'Country risk premium gap (p.p.)'                   PREM_GAP
  'Balance-of-payments premium (p.p.)'                PREM_BOP
  'BoP premium during capital controls (p.p.)'        PREM_BOP_CC  
  'Terms-of-trade premium (p.p.)'                     PREM_TOT
  'Transitory risk premium (p.p.)'                    PREM_TRANS    
  'Real exchange rate (100*log)'                      LZ
  'Real exchange rate depreciation (%QoQ @ar)'        DOT_LZ
  'Expected RER change 1Q ahead (%QoQ @ar)'           E1_DOT_LZ  
  'Equilibrium real exchange rate (100*log)'          LZ_EQ
  'Eq. real exchange rate depreciation (%QoQ @ar)'    DOT_LZ_EQ
  'Eq. RER depr. with BoP level premium (%QoQ @ar)'   DOT_LZ_EQ_EFF  
  'Expected eq. RER depreciation 1Q ahead (%QoQ @ar)' E1_DOT_LZ_EQ  
  'Real exchange rate gap (%)'                        LZ_GAP
  'Smoothed real exchange rate gap (%)'               LZ_GAP_MA
  'Expected RER gap 1Q ahead (%)'                     E1_LZ_GAP  
  'Weighted expectations of RER gap (%)'              EW_LZ_GAP
  'BoP premium in eq. RER change (p.p.)'              PREM_BOP_EQ
  'BoP premium in eq. RER level (p.p.)'               PREM_BOP_EQ_LVL
  'Eq. nominal exchange rate, basket (100*log)'       LS_EQ
  'Eq. nominal exchange rate depreciation (%QoQ @ar)' DOT_LS_EQ
  'Eq. nominal exchange rate depreciation (%YoY)'     DOT4_LS_EQ
  'Auxiliary variable for tuning RES_LZ_GAP'          AUX_RES_LZ_GAP
   
%

%% Output and aggregate demand block

!transition_equations

  'Output'
    Y = Y_EQ + Y_GAP;
    
    Y     = (1-w_x)*YD + w_x*X;
    Y_GAP = (1-w_x)*YD_GAP + w_x*X_GAP;
    
    DOT_Y_EQ      = (1-w_x)*DOT_YD_EQ + w_x*DOT_X_EQ;
    DOT_Y_EQ_EFFX = (1-w_x)*DOT_YD_EQ_EFF + w_x*(w_x_no*DOT_X_NO_EQ_EFF + w_x_o*DOT_X_O_EQ);
    DOT_Y_EQ_LR   = (1-w_x)*DOT_YD_EQ_LR + w_x*DOT_X_EQ;
    
  'Domestic (non-exports) output'
    YD = YD_EQ + YD_GAP;

    YD_GAP = A_D_GAP + (1-alpha_m)*( alpha_d*L_D_GAP + (1-alpha_d)*CU_D_GAP ) + alpha_m*M_Y_GAP;
        A_D_GAP = rho_a_y*A_D_GAP{-1} + RES_A_D_GAP;
        L_D_GAP = N_D_GAP + E_D_GAP;
        
    '- cost-minimisation by firms'
    M_Y_GAP = YD_GAP - (sigh/(sigh*chi_m+1))*(LZ_GAP - RMC_D_GAP) + ((sigh-1)/(sigh*chi_m+1))*A_D_GAP ...
        + (sigh/(sigh*chi_m+1))*( chi_m*(M_Y_GAP{-1} - YD_GAP{-1}) + SHCK_AC_M_GAP );  
    
    CU_D_GAP = L_D_GAP + sigk_d*( (PW_GAP - RK_D_GAP) ...  
        + SHCK_AC_K_GAP - AC_K_GAP );
    
    E_D_GAP = AC_N_GAP - SHCK_AC_N_GAP;
        
    AC_N_GAP = chi_n*( N_D_GAP - N_D_GAP{-1} );
    AC_K_GAP = chi_k*( CU_D_GAP - YD_GAP - (CU_D_GAP{-1} - YD_GAP{-1}) );
    AC_M_GAP = chi_m*( M_Y_GAP - YD_GAP - (M_Y_GAP{-1} - YD_GAP{-1}) );
    
        SHCK_AC_N_GAP = RES_AC_N_GAP;
        SHCK_AC_K_GAP = RES_AC_K_GAP;
        SHCK_AC_M_GAP = RES_AC_M_GAP;
        
    '- rental rate of capital specific to domestic output production'
    CU_D_GAP = eta_nu*RK_D_GAP;

    '- domestic potential output'
    DOT_YD_EQ     = DOT_TFP + (1-alpha_m)*alpha_d*DOT_N_EQ_MA + alpha_m*DOT_M_EQ;
    DOT_YD_EQ_EFF = DOT_TFP_EFF + (1-alpha_m)*alpha_d*DOT_N_EQ_MA + alpha_m*DOT_M_EQ;
    DOT_YD_EQ_LR  = DOT_TFP_LR + (1-alpha_m)*alpha_d*DOT_LF_EQ_MA + alpha_m*DOT_M_EQ;
    
    DOT_N_EQ_MA  = movavg(DOT_N_EQ{+4}, -9);
    DOT_LF_EQ_MA = movavg(DOT_LF_EQ{+4}, -9);
    
    SHCK_SUPL = SHCK_TFP + (1-alpha_m)*alpha_d*( RES_LF_EQ - 1.042*RES_UR_EQ + RES_N_EQ ) + alpha_m*RES_M_EQ;

    DOT_TFP_EFF = DOT_TFP + 4*SHCK_TFP;
        SHCK_TFP = 0.5*SHCK_TFP{-1} + RES_TFP;
    DOT_TFP     = rho_tfp*DOT_TFP{-1} + (1-rho_tfp)*DOT_TFP_LR + RES_DOT_TFP;
    DOT_TFP_LR  = rho_tfp_lr*DOT_TFP_LR{-1} + (1-rho_tfp_lr)*DOT_TFP_SS + RES_DOT_TFP_LR;
    
        DOT_YD_EQ_EFF      = 4*(YD_EQ - YD_EQ{-1});
        DOT_TFP_EFF_GAP    = DOT_TFP_EFF - DOT_TFP_LR;
        E1_DOT_TFP_EFF_GAP = DOT_TFP_EFF_GAP{+1};
                       
  'Exports output and demand'
    X     = X_EQ + X_GAP;
    X     = w_x_no*X_NO + w_x_o*X_O;
    X_GAP = w_x_no*X_NO_GAP + w_x_o*X_O_GAP;

    '- non-oil exports'
    X_NO      = X_NO_EQ + X_NO_GAP;

    X_NO_GAP  = rho_x_gap*X_NO_GAP{-1} + x_yf*YF_GAP + x_z*LZ_GAP + x_tot*LTOT_GAP + RES_X_NO_GAP;
    %
    X_NO_GAP = A_X_GAP + alpha_x*L_X_GAP + (1-alpha_x)*CU_X_GAP;
        A_X_GAP = rho_a_x*A_X_GAP{-1} + RES_A_X_GAP;
        L_X_GAP = N_X_GAP + E_X_GAP;
                
    CU_X_GAP = L_X_GAP + sigk_x*( (PW_GAP - RK_X_GAP) ... 
        - chi_k_x*(CU_X_GAP - X_NO_GAP - (CU_X_GAP{-1} - X_NO_GAP{-1}) ) + RES_AC_K_X_GAP );   
    
    E_X_GAP = chi_n_x*(N_X_GAP - N_X_GAP{-1});
    
    '- rental rate of capital specific to non-oil exports production'
    CU_X_GAP = eta_nu_x*RK_X_GAP;

    X_NO_EQ     = X_NO_EQ{-1} + 0.25*DOT_X_NO_EQ + RES_X_NO_EQ;
    DOT_X_NO_EQ = rho_x_eq*DOT_X_NO_EQ{-1} + (1-rho_x_eq)*( ...
                  x_eq_yf*DOT_YF_EQ + x_n*alpha_x*DOT_N_EQ_MA ...
                  ) + RES_DOT_X_NO_EQ;
              
    DOT_X_EQ        = w_x_no*DOT_X_NO_EQ + w_x_o*DOT_X_O_EQ;
    DOT_X_NO_EQ_EFF = DOT_X_NO_EQ + 4*RES_X_NO_EQ;
              
    '- oil exports'
    X_O = X_O_EQ + X_O_GAP;
    
    X_O_GAP = rho_xo_gap*X_O_GAP{-1} + RES_X_O_GAP;
    
    X_O_EQ     = X_O_EQ{-1} + 0.25*DOT_X_O_EQ + RES_X_O_EQ;
    DOT_X_O_EQ = rho_xo_eq*DOT_X_O_EQ{-1} + (1-rho_xo_eq)*DOT_X_O_SS + RES_DOT_X_O_EQ;
    
    DOT_X_O_EQ_EFF = DOT_X_O_EQ + 4*RES_X_O_EQ;
              
  'Domestic demand'
    Y      = w_d*D + w_x*X - w_m*M;
    Y_GAP  = w_d*D_GAP + w_x*X_GAP - w_m*M_GAP;
    
    D        = D_EQ + D_GAP;
    D_EQ     = D_EQ{-1} + 0.25*DOT_D_EQ + SHCK_D_EQ;
    DOT_D_EQ = (DOT_Y_EQ - w_x*DOT_X_EQ + w_m*DOT_M_EQ) / w_d;
    
    D_GAP = w_df*DF_GAP + (1-w_df)*M_Y_GAP;
    
  'Domestic demand curve (Euler equation)'
    DF_GAP = d_lead*E1_DF_GAP + d_lag*DF_GAP{-1} - d_rr*RRA_GAP ...
            + d_wr*( WR_GAP + N_GAP + d_ub*U_GAP ) + d_tot*LTOT_GAP + FISC_STIM + SHCK_DF_GAP;
        SHCK_DF_GAP = rho_shck_d_gap*SHCK_DF_GAP{-1} + RES_DF_GAP;
    
  'Imports'
    M = M_EQ + M_GAP;
    
    M_GAP = w_m_y*M_Y_GAP + w_m_d*M_D_GAP;
  
    M_D_GAP = rho_m_gap*M_D_GAP{-1} + m_d*DF_GAP - m_z*LRP_M_GAP + RES_M_D_GAP;
    
    M_EQ     = M_EQ{-1} + 0.25*DOT_M_EQ + m_d*SHCK_D_EQ + RES_M_EQ;
    DOT_M_EQ = rho_m_eq*DOT_M_EQ{-1} + (1-rho_m_eq)*m_d*DOT_D_EQ - m_eq_z*DOT_LZ_EQ + RES_DOT_M_EQ;
            
  'Nominal output growth'   
    DOT4_Y_NOM       = DOT4_Y + DOT4_Y_DEFL + RES_DOT4_Y_NOM;
    DOT4_Y_NOM_EQ    = DOT4_Y_EQ + DOT4_Y_DEFL_EQ;
    DOT_Y_NOM_MA_GAP = movavg(DOT4_Y_NOM - DOT4_Y_NOM_EQ, -4);
                           
  'Identities'
        E1_DOT_Y          = DOT_Y{+1};
        E1_Y_GAP          = Y_GAP{+1};
        Y_GAP_MA          = movavg(Y_GAP, -4);
        DOT_Y_GAP         = 4*(Y_GAP - Y_GAP{-1});
        E1_DOT_Y_GAP      = DOT_Y_GAP{+1};
        %
        E1_DF_GAP         = DF_GAP{+1};        
        AUX_RES_DF_GAP     = RES_DF_GAP;        
        %
      !for
        ?Z = Y, D, X, M
      !do
        DOT_?Z        = 4*(?Z - ?Z{-1});
        DOT4_?Z_MA    = movavg(DOT4_?Z, -4);
        DOT_?Z_EQ_EFF = 4*(?Z_EQ - ?Z_EQ{-1});
        DOT4_?Z_EQ    = ?Z_EQ - ?Z_EQ{-4};
        DOT4_?Z_EQ_MA = movavg(DOT4_?Z_EQ, -4);
      !end
      !for
        ?Z = Y, X, M
      !do   
        DOT4_?Z       = ?Z - ?Z{-4} + DOT4_?Z_SF;
        DOT4_?Z_SF    = ?.Z_sf*DOT4_?Z_SF{-1} + (1-?.Z_sf)*0.0 + RES_DOT4_?Z_SF;
      !end
        DOT4_D     = D - D{-4};
        DOT_YD     = 4*(YD - YD{-1});
        DOT4_YD    = YD - YD{-4};
        %
        DOT_X_NO   = 4*(X_NO - X_NO{-1});
        DOT_X_O    = 4*(X_O - X_O{-1});
            
          
!transition_shocks
  'Domestic final demand shock residual'             RES_DF_GAP
  'Non-exports transitory TFP level shock  residual' RES_A_D_GAP
  'Permanent TFP level shock residual'               RES_TFP
  'Permanent TFP growth shock'                       RES_DOT_TFP 
  'Long-run permanent TFP growth shock'              RES_DOT_TFP_LR
  'Shock to SF of YoY output growth'                 RES_DOT4_Y_SF
  'Shock to domestic employment adjustment costs'    RES_AC_N_GAP
  'Shock to domestic capital adjustment costs'       RES_AC_K_GAP
  'Shock to intermediate imports adjustment costs'   RES_AC_M_GAP
  'Observational shock to YoY nominal output growth' RES_DOT4_Y_NOM
  %
  'Exports transitory TFP level shock'               RES_A_X_GAP
  'Non-oil exports demand shock'                     RES_X_NO_GAP
  'Non-oil exports eq. level shock'                  RES_X_NO_EQ
  'Non-oil exports eq. growth shock'                 RES_DOT_X_NO_EQ
  'Oil exports demand shock'                         RES_X_O_GAP
  'Oil exports eq. level shock'                      RES_X_O_EQ
  'Oil exports eq. growth shock'                     RES_DOT_X_O_EQ
  'Shock to SF of YoY exports growth'                RES_DOT4_X_SF
  'Shock to exports capital adjustment costs'        RES_AC_K_X_GAP
  %
  'Imports demand shock'                             RES_M_D_GAP
  'Eq. imports level shock'                          RES_M_EQ
  'Eq. imports growth shock'                         RES_DOT_M_EQ
  'Shock to SF of YoY imports growth'                RES_DOT4_M_SF
    


%% Labour block

!transition_equations

  'Labour force'
    LF        = LF_EQ + LF_GAP;
    LF_EQ     = LF_EQ{-1} + 0.25*DOT_LF_EQ + RES_LF_EQ;
    DOT_LF_EQ = rho_lf_eq*DOT_LF_EQ{-1} + (1-rho_lf_eq)*DOT_LF_SS + RES_DOT_LF_EQ;
    LF_GAP    = rho_lf_gap*LF_GAP{-1} + RES_LF_GAP;
    
        AUX_RES_LF_EQ = RES_LF_EQ;

  'Unemployment'
    UR        = UR_EQ + UR_GAP;
    UR_EQ     = UR_EQ{-1} + DOT_UR_EQ + RES_UR_EQ;
    DOT_UR_EQ = rho_dot_ur_eq*DOT_UR_EQ{-1} + RES_DOT_UR_EQ;
    
    UR_GAP    = 0.04*(U_GAP - LF_GAP);
    U_GAP     = 25*LF_GAP - 24*N_GAP;

  'Employment and working hours'
    N = N_EQ + N_GAP;
    
    N_GAP = w_n_d*N_D_GAP + w_n_x*N_X_GAP;

    N_EQ     = N_EQ{-1} + 0.25*DOT_N_EQ + RES_LF_EQ - 1.042*RES_UR_EQ + RES_N_EQ;
    DOT_N_EQ = DOT_LF_EQ - 4.2*DOT_UR_EQ + RES_DOT_N_EQ;

        AUX_RES_N_EQ = RES_N_EQ;        
        DOT_LF = 4*(LF - LF{-1});
        DOT_N  = 4*(N - N{-1});
                    
  'Search and matching'
    UB_GAP = 25*LF_GAP - rho_surv*24*(N_GAP{-1} + SURV_GAP);

    MATCH_GAP = sigm*UB_GAP + (1-sigm)*V_GAP;

    N_GAP = N_GAP{-1} + (1-rho_surv)*HR_GAP + rho_surv*SURV_GAP;
    
    SURV_GAP = rho_surv_gap*SURV_GAP{-1} + RES_SURV_GAP;

    HR_GAP = Q_GAP + V_GAP - N_GAP{-1};

    Q_GAP = MATCH_GAP - V_GAP;

    F_GAP = MATCH_GAP - UB_GAP;
    
    LMT_GAP = V_GAP - UB_GAP;
    
  'Hiring and wages'
    PW_GAP = b_w*WR_GAP + b_hr*HR_GAP - b_hr_fwd*E1_HR_GAP - b_sdf*SDF_GAP - b_rho*SURV_GAP;

    WR_GAP = b_lag*( WR_GAP{-1} - (PIE_GAP + DOT_TFP_EFF_GAP) + b_index*PIE_GAP{-1} ) ... 
            + b_opt*WRO_GAP ...
            + b_fwd*( E1_WR_GAP + (E1_PIE_GAP + E1_DOT_TFP_EFF_GAP) - b_index*PIE_GAP ) + RES_WR_GAP;

    WRO_GAP = bo_w*PW_GAP + bo_hr*E1_HR_GAP + bo_f*E1_F_GAP + bo_sdf*SDF_GAP ... 
              + bo_chi*( CHI_GAP - bo_chi1*E1_CHI_GAP );         

    CHI_GAP = -(1-CHI_SS)*(MU_GAP - EPS_GAP);

    EPS_GAP = beps_fwd*( E1_EPS_GAP + E1_SURV_GAP + SDF_GAP - (E1_PIE_GAP + E1_DOT_TFP_EFF_GAP) + b_index*PIE_GAP );

    MU_GAP = bmu_hr*E1_HR_GAP + bmu_rho*E1_SURV_GAP ... 
             - bmu_w*( WR_GAP - (E1_PIE_GAP + E1_DOT_TFP_EFF_GAP) + b_index*PIE_GAP - E1_WR_GAP ) ...
             + bmu_fwd*( E1_MU_GAP + SDF_GAP - (E1_PIE_GAP + E1_DOT_TFP_EFF_GAP) + b_index*PIE_GAP );

    SDF_GAP = -RR_GAP + E1_DOT_TFP_EFF_GAP;
    
        E1_HR_GAP   = HR_GAP{+1};
        E1_WR_GAP   = WR_GAP{+1};
        E1_F_GAP    = F_GAP{+1};
        E1_SURV_GAP = SURV_GAP{+1};
        E1_CHI_GAP  = CHI_GAP{+1};
        E1_EPS_GAP  = EPS_GAP{+1};
        E1_MU_GAP   = MU_GAP{+1};
        
  'Equilibrium wage'
    WR = W - LCPI;
    WR = WR_EQ + WR_GAP;

    DOT_WR_EQ = rho_wr_eq*DOT_WR_EQ{-1} + (1-rho_wr_eq)*DOT_TFP_EFF + RES_DOT_WR_EQ;

        DOT_W      = 4*(W - W{-1});
        DOT4_W     = W - W{-4} + DOT4_W_SF;
        DOT4_W_SF  = w_sf*DOT4_W_SF{-1} + (1-w_sf)*0.0 + RES_DOT4_W_SF;
        DOT_WR     = 4*(WR - WR{-1});
        DOT4_WR    = WR - WR{-4};
        DOT_WR_EQ  = 4*(WR_EQ - WR_EQ{-1});
        DOT4_WR_EQ = WR_EQ - WR_EQ{-4};
        
        
!transition_shocks
  'Equilibrium labour force level shock'   RES_LF_EQ
  'Equilibrium labour force growth shock'  RES_DOT_LF_EQ
  'Labour force gap shock'                 RES_LF_GAP
  'Equilibrium unemployment level shock'   RES_UR_EQ
  'Change of eq, unemployment level shock' RES_DOT_UR_EQ
  'Equilibrium employment growth shock'    RES_N_EQ
  'Equilibrium employment growth shock'    RES_DOT_N_EQ
  'Survival probability shock residual'    RES_SURV_GAP  
  'Real wage gap shock'                    RES_WR_GAP
  'Equlibrium real wage growth shock'      RES_DOT_WR_EQ
  'Shock to SF of YoY nom. wage growth'    RES_DOT4_W_SF
  

%


%% Aggregate supply: prices block

!substitutions
    PN := PW; PK := RK_D; PM := LZ;

!transition_equations

  'Domestic & imported core inflation Phillips curves'  % [mpie]  
    PIE_C = w_h*PIE_D + (1-w_h)*PIE_M;

    '- domestic core inflation Phillips curve'    
    PIE_D = c_lag_d*PIE_D{-1} + (1-c_lag_d)*EW1_PIE_D + c_rmc_d*RMC_D_GAP_MA + SHCK_PIE_D;          
        SHCK_PIE_D = rho_shck_pie_d*SHCK_PIE_D{-1} + RES_PIE_D;
        
    '- imported core inflation Phillips curve'
    PIE_M = c_lag_m*PIE_M{-1} + (1-c_lag_m)*EW1_PIE_M + c_rmc_m*RMC_IMP_GAP;
        
    '- weighted core inflation expectations'
    EW1_PIE_C = w_h*EW1_PIE_D + (1-w_h)*EW1_PIE_M;
    
    EW1_PIE_D = w_exp_lag*PIE_D{-1} + (1-w_exp_lag)*E1_PIE_D
                + c_exp_nc*(PIE_NC - PIE_C) + RES_EW1_PIE_D;
                
    EW1_PIE_M = w_exp_lag*PIE_M{-1} + (1-w_exp_lag)*E1_PIE_M;
     
    '- real marginal costs for domestic core goods'
    RMC_D_GAP = (1-alpha_m)*( alpha_d*PW_GAP + (1-alpha_d)*(RK_D_GAP + AC_K_GAP - RES_AC_K_GAP) ) ...
                       + alpha_m*(LZ_GAP + AC_M_GAP - RES_AC_M_GAP) - A_D_GAP - c_supl*SHCK_SUPL - LRP_D_GAP + w_nc*LRP_NC_GAP;
    
    '- smoothed real marginal costs for domestic core goods'
    RMC_D_GAP_MA = (1-alpha_m)*( alpha_d*RMC_N_GAP_MA + (1-alpha_d)*RMC_K_GAP_MA ) ...
                       + alpha_m*RMC_M_GAP_MA - A_D_GAP_MA - c_supl*SHCK_SUPL_MA - LRP_D_GAP_MA + w_nc*LRP_NC_GAP_MA;
                   
    '- real marginal costs for imported core goods'
    RMC_IMP_GAP = LZ_GAP - LRP_M_GAP + w_nc*LRP_NC_GAP;
    
    '- aggregated real marginal costs for core goods'
    RMC_GAP    = w_h*RMC_D_GAP + (1-w_h)*(c_rmc_m/c_rmc_d)*RMC_IMP_GAP;
    RMC_GAP_MA = w_h*RMC_D_GAP_MA + (1-w_h)*(c_rmc_m/c_rmc_d)*RMC_IMP_GAP;
                 
  !for
    ?F = K, M
  !do
    RMC_?F_GAP_MA = $P?F$_GAP_MA + AC_?F_GAP_MA - SHCK_AC_?F_GAP_MA;
  !end
    RMC_N_GAP_MA = PW_GAP_MA;

  !for
    ?X = PW, AC_N, SHCK_AC_N,  RK_D, AC_K, SHCK_AC_K, LZ, AC_M, SHCK_AC_M, A_D, LRP_D, LRP_NC
  !do
    ?X_GAP_MA = 0.25*?X_GAP{-2} + 0.50*?X_GAP{-1} + 0.25*?X_GAP;
  !end
    SHCK_SUPL_MA = 0.25*SHCK_SUPL{-2} + 0.50*SHCK_SUPL{-1} + 0.25*SHCK_SUPL; 
     
    
  'Fruits and vegetables inflation'
    PIE_VEG = c_lag_veg*PIE_VEG{-1} + (1-c_lag_veg)*(PIE_TAR + DOT_LRP_VEG_EQ)
              + c_z_veg*(LZ_GAP-LZ_GAP{-1}) - c_rp_veg*LRP_VEG_GAP + SHCK_PIE_VEG;
                      
    SHCK_PIE_VEG    = AUX_RES_PIE_VEG - c_veg_revert*AUX_RES_PIE_VEG{-1};
    AUX_RES_PIE_VEG = RES_PIE_VEG;
    
  'Fuels (oil products) inflation'
    PIE_FUEL = c_lag_fuel*PIE_FUEL{-1} + (1-c_lag_fuel)*(PIE_TAR + DOT_LRP_FUEL_EQ)
               + c_oil_fuel*(LTOT_GAP + LZ_GAP) - c_rp_fuel*LRP_FUEL_GAP + RES_PIE_FUEL;
               
  'Regulated services (including utilities) inflation'
    PIE_SREG = c_lag_sreg*PIE_SREG{-1} + (1-c_lag_sreg)*(PIE_TAR + DOT_LRP_SREG_EQ)
               - c_rp_sreg*LRP_SREG_GAP + RES_PIE_SREG;
               
  'Volatile components inflation'
    PIE_VOL = c_lag_vol*PIE_VOL{-1} + (1-c_lag_vol)*(PIE_TAR + DOT_LRP_VOL_EQ) 
              - c_rp_vol*LRP_VOL_GAP + RES_PIE_VOL;
              
  'Relative prices'
  !for
    ?X = VEG, FUEL, SREG, VOL
  !do
    LRP_?X        = LCPI_?X - LCPI_C;
    LRP_?X        = LRP_?X_EQ + LRP_?X_GAP;
    LRP_?X_EQ     = LRP_?X_EQ{-1} + 0.25*DOT_LRP_?X_EQ + RES_LRP_?X_EQ  + c_rp_?.X_eq*LRP_?X_GAP ;
    DOT_LRP_?X_EQ = rho_rp_?.X_eq*DOT_LRP_?X_EQ{-1} + RES_DOT_LRP_?X_EQ;

  !end
    LRP_NC     = LCPI_NC - LCPI_C;
    LRP_NC_GAP = (w_veg/w_nc)*LRP_VEG_GAP + (w_fuel/w_nc)*LRP_FUEL_GAP
                 + (w_sreg/w_nc)*LRP_SREG_GAP + (w_vol/w_nc)*LRP_VOL_GAP;
                 
    '- core inflation relative prices'
    0 = w_h*LRP_D_GAP + (1-w_h)*LRP_M_GAP;
    LRP_M_GAP = LRP_M_GAP{-1} + PIE_M - PIE_C;
                
  'Price indices aggregation'
    LCPI = w_core*LCPI_C + w_veg*LCPI_VEG + w_fuel*LCPI_FUEL
           + w_sreg*LCPI_SREG + w_vol*LCPI_VOL + LCPI_WEDGE;
    LCPI_WEDGE = LCPI_WEDGE{-1} + RES_LCPI;
    
    LCPI_NC = (w_veg/w_nc)*LCPI_VEG + (w_fuel/w_nc)*LCPI_FUEL
              + (w_sreg/w_nc)*LCPI_SREG + (w_vol/w_nc)*LCPI_VOL;   
            
  'GDP deflator'
    DOT4_Y_DEFL = c_defl_cpi*PIE4 + c_defl_oil*( DOT4_LPOIL + DOT4_LS )
                - (c_defl_cpi + c_defl_oil - 1)*( PIEF4 + DOT4_LS ) + ERR_DOT4_Y_DEFL;             
               
    ERR_DOT4_Y_DEFL = rho_defl*ERR_DOT4_Y_DEFL{-1} + RES_DOT4_Y_DEFL;
    
    DOT4_Y_DEFL_EQ = c_defl_cpi*PIE_TAR4 + c_defl_oil*( DOT4_LPOIL_EQ + DOT4_LS_EQ )
                     - (c_defl_cpi + c_defl_oil - 1)*( PIEF_SS + DOT4_LS_EQ );
                
  'Identities'
        PIE        = 4*(LCPI - LCPI{-1});
        PIE4       = LCPI - LCPI{-4} + PIE4_SF;
        PIE4_SF    = c_sf_pie*PIE4_SF{-1} + RES_PIE4_SF;
        PIE4_MA    = movavg(PIE4, -4);
        PIE_GAP    = PIE - PIE_TAR;
        PIE4_GAP   = PIE4 - PIE_TAR4;
        E1_PIE_GAP = PIE_GAP{+1};
        E1_PIE_D    = PIE_D{+1};
        E1_PIE_M    = PIE_M{+1};
        %
      !for
        ?X = C, VEG, FUEL, SREG, VOL, NC
      !do
        PIE_?X      = 4*(LCPI_?X - LCPI_?X{-1});
        PIE_?X4     = LCPI_?X - LCPI_?X{-4} + PIE_?X4_SF;
        PIE_?X4_SF  = c_sf_pie*PIE_?X4_SF{-1} + RES_PIE_?X4_SF;
        PIE4_?X_MA  = movavg(PIE_?X4, -4);
        PIE_?X_GAP  = PIE_?X - PIE_TAR;
        PIE_?X4_GAP = PIE_?X4 - PIE_TAR4;        
      !end


!transition_shocks
  'Domestic core inflation shock residual'          RES_PIE_D
  'Expected domestic core inflation shock'          RES_EW1_PIE_D
  'Fruits and vegetables inflation shock'           RES_PIE_VEG
  'Fuels (oil products) inflation shock'            RES_PIE_FUEL
  'Regulated services inflation shock'              RES_PIE_SREG
  'Volatile components inflation shock'             RES_PIE_VOL
  % 
 !for
  ?X = VEG, FUEL, SREG, VOL
 !do
  'Shock to level of eq. ? CPI rel. price'          RES_LRP_?X_EQ 
  'Shock to change of eq. ? CPI rel. price'         RES_DOT_LRP_?X_EQ
 !end  
  'Headline CPI wedge shock'                        RES_LCPI
  'GDP deflator approximation error residual'       RES_DOT4_Y_DEFL
  'Shock to SF of YoY headline CPI inflation'       RES_PIE4_SF
 !for
  ?X = C, VEG, FUEL, SREG, VOL, NC
 !do
  'Shock to SF of YoY ?X CPI inflation'             RES_PIE_?X4_SF
 !end
    


%% Monetary policy rule block

!transition_equations

  'Monetary policy rule'  % [mrs]
    RS  = gamma1*RS{-1} + (1-gamma1)*(RS_NEUTRAL + gamma2*E3_PIE4_DEV + gamma3*Y_GAP) + RES_RS;

    RS_NEUTRAL   = RR_EQ + E3_PIE4_MP;
    RS_GAP       = RS - RS_NEUTRAL;
    E3_PIE4_DEV  = E3_PIE4_MP - E3_PIE_TAR4;
    E3_PIE4_MP   = w_mp_pie_c*E3_PIE_C4 + (1-w_mp_pie_c)*E3_PIE4;    
    
    PIE_TAR      = psi*PIE_TAR{-1}+ (1-psi)*PIE_TAR_SS + RES_PIE_TAR;
  
  'Real interbank interest rate and its equilibrium'    
    RR = RS - EW1_PIE_C;
    RR = RR_EQ + RR_GAP;
    RR_EQ = lappa*RR_EQ{-1} + (1-lappa)*( gamma_ext*(RRF_EQ + PREM_EQ + E1_DOT_LZ_EQ) ...
                                     + (1-gamma_ext)*h_rr_y*DOT_Y_EQ );
    
  'Identities'
        E1_PIE      = PIE{+1};
        E1_PIE_C    = PIE_C{+1};
        E3_PIE_C4   = PIE_C4{+3};
        E3_PIE_NC4   = PIE_NC4{+3};
        E3_PIE4     = PIE4{+3};
        PIE_TAR4    = movavg(PIE_TAR, -4);
        E3_PIE_TAR4 = PIE_TAR4{+3};

!transition_shocks
  'Policy shock' RES_RS
  'Inflation target shock' RES_PIE_TAR
    
    
%

%% Term structure block
!import(qpm_term_structure.mod)
%% Fiscal block
!import(qpm_fiscal_block.mod)
%% Exchange rates block

!transition_equations

  'UIP'  % [mz]
    LZ_GAP = (1-w_cc)*( EW_LZ_GAP - (RR_GAP - RRF_GAP - PREM_GAP - PREM_TRANS - PREM_BOP - PREM_TOT)/4 ) ...
          + w_cc*( (1-delta_cc)*LZ_GAP{-1} + PREM_BOP_CC/4 ) + RES_LZ_GAP/4;
        
  'ER weighted expectations'
    EW_LZ_GAP   = delta*E1_LZ_GAP + (1-delta)*LZ_GAP{-1}; 
        
  'Country risk premium'
    PREM     = PREM_EQ + PREM_GAP;
    PREM_GAP = chi*PREM_GAP{-1} - chi_oil*(REV_O_EXTRA_ARAT + REV_O_EXTRA_ARAT{+4})/2 + RES_PREM;
    PREM_EQ  = rho_prem_eq*PREM_EQ{-1} + (1-rho_prem_eq)*PREM_SS + RES_PREM_EQ;
    
  'Balance-of-payments premium'
    PREM_BOP    = -c_prem_bop * ( X_GAP - M_GAP + c_tot_elast*LTOT_GAP );
    PREM_BOP_CC = -c_prem_bop_cc *( X_GAP - M_GAP + c_tot_elast_cc*LTOT_GAP );
    
  'Terms-of-trade premium'
    PREM_TOT = -c_prem_tot * 4*(LTOT - E1_LTOT{-1}); 
    
  'Transitory risk premium'
    PREM_TRANS = rho_prem_trans*PREM_TRANS{-1} + RES_PREM_TRANS;
    
  'Equilibrium real exchange rate'
    DOT_LZ_EQ = rho_z_eq*DOT_LZ_EQ{-1} + (1-rho_z_eq)*( ...
                    c_z_eq_bop*PREM_BOP_EQ ) + RES_DOT_LZ_EQ;
            
    LZ_EQ = LZ_EQ{-1} + 0.25*DOT_LZ_EQ + c_z_eq_bop*PREM_BOP_EQ_LVL;
        
    PREM_BOP_EQ = -( (DOT_X_EQ - DOT_X_SS) - (DOT_M_EQ - DOT_M_SS) ...
                     + (DOT_LTOT_EQ - DOT_LTOT_SS) );
                 
    PREM_BOP_EQ_LVL = -( (w_x_no*RES_X_NO_EQ + w_x_o*RES_X_O_EQ) - RES_M_EQ );
    
    LZ = LS + LCPIF - LCPI;  
    LZ = LZ_EQ + LZ_GAP;
    
    DOT_LS_EQ = DOT_LZ_EQ + PIE_TAR - PIEF_SS;
    
        DOT_LZ_EQ_EFF = DOT_LZ_EQ + 4*c_z_eq_bop*PREM_BOP_EQ_LVL; 
        E1_DOT_LZ_EQ  = DOT_LZ_EQ{+1} + RES_E_LZ_EQ;
        
  'USD/RUB exchange rate'
    LS_USD = LS - (1-w_usd)*L_EUR_USD + ERR_LS_USD;
    ERR_LS_USD = ERR_LS_USD{-1} + RES_LS_USD;
    
  'Identities'
        LS = LS{-1} + 0.25*DOT_LS;  
        DOT4_LS = LS - LS{-4};
        AUX_RES_LZ_GAP = RES_LZ_GAP;
        LZ = LZ{-1} + 0.25*DOT_LZ;
        LS_EQ = LS_EQ{-1} + 0.25*DOT_LS_EQ;
        DOT4_LS_EQ = LS_EQ - LS_EQ{-4};      
        E1_LS = LS{+1};
        E1_DOT_LZ = DOT_LZ{+1};
        E1_LZ_GAP = LZ_GAP{+1};
        LS_USD = LS_USD{-1} + 0.25*DOT_LS_USD;
        DOT4_LS_USD = LS_USD - LS_USD{-4};
            
!transition_shocks
  'UIP shock'                      RES_LZ_GAP
  'Country risk premium gap shock' RES_PREM
  'Eq. country risk premium shock' RES_PREM_EQ
  'Transitory risk premium shock'  RES_PREM_TRANS
  'RER trend depreciation shock'   RES_DOT_LZ_EQ
  'RER trend expectations shock'   RES_E_LZ_EQ
  'Approximation error in LS_USD'  RES_LS_USD

        
%

%%
% Ќиже объ€влены наблюдаемые переменные и уравнени€ св€зи наблюдаемых и ненаблюдаемых переменных. 
% ƒанные блоки необходимы при работе с фактическими данными.
%% Measurement variables

!measurement_variables

'Observed Y'                     OBS_Y
'Observed DOT4_Y_SF'             OBS_DOT4_Y_SF
'Observed DOT4_Y_NOM'            OBS_DOT4_Y_NOM
'Observed DOT4_Y_DEFL'           OBS_DOT4_Y_DEFL
%
'Observed X'                     OBS_X
'Observed DOT4_X_SF'             OBS_DOT4_X_SF
'Observed X_O'                   OBS_X_O
'Observed M'                     OBS_M
'Observed DOT4_M_SF'             OBS_DOT4_M_SF
%
'Observed LF'                    OBS_LF
'Observed N'                     OBS_N
'Observed UR'                    OBS_UR
'Observed W'                     OBS_W
'Observed DOT4_W_SF'             OBS_DOT4_W_SF
%
'Observed LCPI'                  OBS_LCPI
'Observed PIE4_SF'               OBS_PIE4_SF
'Observed LCPI_C'                OBS_LCPI_C
'Observed PIE_C4_SF'             OBS_PIE_C4_SF
'Observed LCPI_VEG'              OBS_LCPI_VEG
'Observed PIE_VEG4_SF'           OBS_PIE_VEG4_SF
'Observed LCPI_FUEL'             OBS_LCPI_FUEL
'Observed PIE_FUEL4_SF'          OBS_PIE_FUEL4_SF
'Observed LCPI_SREG'             OBS_LCPI_SREG
'Observed PIE_SREG4_SF'          OBS_PIE_SREG4_SF
'Observed LCPI_VOL'              OBS_LCPI_VOL
'Observed PIE_VOL4_SF'           OBS_PIE_VOL4_SF
%
'Observed RS'                    OBS_RS
'Observed LS'                    OBS_LS
'Observed LS_USD'                OBS_LS_USD
'Observed PREM'                  OBS_PREM
   
%

%% Measurement equations

!measurement_equations

OBS_Y                     = Y;
OBS_DOT4_Y_SF             = DOT4_Y_SF;
OBS_DOT4_Y_NOM            = DOT4_Y_NOM;
OBS_DOT4_Y_DEFL           = DOT4_Y_DEFL;
%
OBS_X                     = X + RES_OBS_X;
OBS_DOT4_X_SF             = DOT4_X_SF;
OBS_X_O                   = X_O;
OBS_M                     = M;
OBS_DOT4_M_SF             = DOT4_M_SF;
%
OBS_LF                    = LF;
OBS_N                     = N;
OBS_UR                    = UR;
OBS_W                     = W;
OBS_DOT4_W_SF             = DOT4_W_SF;
%
OBS_LCPI                  = LCPI;
OBS_PIE4_SF               = PIE4_SF;
OBS_LCPI_C                = LCPI_C;
OBS_PIE_C4_SF             = PIE_C4_SF;
OBS_LCPI_VEG              = LCPI_VEG;
OBS_PIE_VEG4_SF           = PIE_VEG4_SF;
OBS_LCPI_FUEL             = LCPI_FUEL;
OBS_PIE_FUEL4_SF          = PIE_FUEL4_SF;
OBS_LCPI_SREG             = LCPI_SREG;
OBS_PIE_SREG4_SF          = PIE_SREG4_SF;
OBS_LCPI_VOL              = LCPI_VOL;
OBS_PIE_VOL4_SF           = PIE_VOL4_SF;
%
OBS_RS                    = RS;
OBS_LS                    = LS;
OBS_LS_USD                = LS_USD; 
OBS_PREM                  = PREM;

!measurement_shocks
RES_OBS_X

!import(parameters_main.mod)

