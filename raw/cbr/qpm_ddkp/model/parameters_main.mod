!parameters
  'Output'
    alpha_m = 0.13;
    sigh    = 0.75;
    alpha_d = 0.56;
    sigk_d  = 0.75;
    chi_n   = 12.5;
    chi_m   = 5;
    chi_k   = 2;
    eta_nu  = 1.0;
    %
    w_x_no;
    %
    rho_a_y    = 0.50;
    rho_tfp    = 0.80;
    rho_tfp_lr = 0.9999;
    DOT_TFP_SS = 100*log(1+2.0/100);
    y_sf       = 0; 
    %
    std_RES_A_D_GAP    = 1.0;
    std_RES_TFP        = 0.10;
    std_RES_DOT_TFP    = 0.40;
    std_RES_DOT_TFP_LR = 0.10;
    std_RES_AC_N_GAP   = 0.25;
    std_RES_AC_K_GAP   = 0.5;
    std_RES_AC_M_GAP   = 1.00;
    std_RES_DOT4_Y_NOM = 0.75;
  'Output and demand'
    w_x = 0.313;
    w_m = 0.203;
    w_d;
    w_df;
    DOT_D_SS;
    DOT_Y_SS;
  'Domestic demand'
    d_lead = 0.20;
    d_lag  = 0.50;
    d_rr   = 0.35;
    d_wr   = 0.05;
    d_ub  = 0.0042; 
    d_tot  = 0.015;
    %
    rho_shck_d_gap = 0.50;
    std_RES_DF_GAP  = 1.0;
  'Exports'
    alpha_x  = 0.25;
    sigk_x   = 0.25;
    chi_n_x  = 12.5;
    chi_k_x  = 1.00;
    eta_nu_x = 4;
    w_x_o    = 0.44;
    %
    rho_a_x   = 0.25;
    rho_x_gap = 0.50;
    x_yf      = 1.00;
    x_z       = 0.05;
    x_tot     = 0.01;
    x_eq_yf   = 1.00;
    x_n       = 1.00;
    rho_x_eq  = 0.75;
    x_sf      = 0;
    DOT_X_SS;
    %
    rho_xo_gap = 0.25;
    rho_xo_eq  = 0.50;
    DOT_X_O_SS = 0;
    %
    std_RES_A_X_GAP     = 5;
    std_RES_X_NO_EQ     = 0.50;
    std_RES_DOT_X_NO_EQ = 1.50;
    std_RES_X_NO_GAP    = 5.00;
    std_RES_X_O_EQ      = 0.60;
    std_RES_DOT_X_O_EQ  = 1.00;
    std_RES_AC_K_X_GAP  = 0.00;
  'Imports'
    w_m_y    = 0.37; 
    w_m_d;
    rho_m_gap = 0;
    m_d       = 1.0;
    m_z       = 0.50;
    m_eq_z    = 0.50;
    rho_m_eq  = 0.00;
    m_sf      = 0.15;
    DOT_M_SS;
    %
    std_RES_M_D_GAP    = 5.00;
    std_RES_M_EQ     = 0.15;
    std_RES_DOT_M_EQ = 0.50;
    
!links
    w_x_no = 1 - w_x_o;
    w_m_d  = 1 - w_m_y;
    w_d    = 1 - w_x + w_m;
    w_df   = 1 - w_m*w_m_y / w_d;
       
%
!parameters
  'Labour force'
    rho_lf_eq  = 0.75;
    DOT_LF_SS  = 0;
    rho_lf_gap = 0.5;
    %
    std_RES_LF_EQ     = 0.05;
    std_RES_DOT_LF_EQ = 0.25;
    std_RES_LF_GAP    = 0.75;
  'Unemployment'
    rho_dot_ur_eq = 0.50;
   
    %
    std_RES_UR_EQ     = 0.05;
    std_RES_DOT_UR_EQ = 0.10;
  'Employment and working hours'
    w_n_x   = 0.177;
    w_n_d;
    b_elast = 1.0;
    sigc = 0.5;
    hc   = 0.5;
    %
    std_RES_DOT_N_EQ = 0.25;
    std_RES_N_EQ     = 0.05;
  'Search and matching'
    rho_surv     = 0.962;
    rho_surv_gap = 0.50;
    sigm         = 0.50;
    %
    std_RES_SURV_GAP = 0.25;
  'Optimal hiring' 
    b_w      = 0.95;
    b_hr     = 0.25;
    b_hr_fwd = 0.24;
    b_sdf    = 0.10;
    b_rho    = 0.25;
  'Average wage'
    b_lag   = 0.35;
    b_opt   = 0.40;
    b_fwd;
    b_index = 0.40;
    %
    std_RES_WR_GAP = 2;
  'Optimal wage'
    bo_w    = 0.70;
    bo_hr   = 0.07;
    bo_f    = 0.07;
    bo_sdf  = 0.07;
    bo_chi  = 0.60;
    bo_chi1 = 0.40;
  'Bargaining power and marginal surpluses'
    CHI_SS   = 0;
    beps_fwd = 0.35;
    bmu_hr   = 0.015; 
    bmu_rho  = 0.35;
    bmu_w    = 0.12;
    bmu_fwd  = 0.35;
   'Equilibrium wage'
    rho_wr_eq = 0.5;
    w_sf      = 0.0;
    %
    std_RES_DOT_WR_EQ = 1.5;
    
!links
    w_n_d = 1 - w_n_x;
    b_fwd = 1 - b_lag - b_opt;
    
    
    
    
   !parameters
  'Core inflation'
    c_lag_d          = 0.20;
    c_rmc_d          = 0.35;
    c_lag_m          = 0.20;
    c_rmc_m          = 0.225; 
    w_h;
    c_supl           = 2;
    
    !if expect_adapt == true
    w_exp_lag        = 0.375;
    !else
    w_exp_lag        = 0.25;
    !end
    
    c_exp_nc         = 0.25;
    rho_shck_pie_d   = 0.50;
    std_RES_PIE_D    = 1.50;
    %
    std_RES_EW1_PIE_D = 0.50;
    std_RES_LCPI      = 0.25;
  'Veggies inflation'
    c_lag_veg        = 0.18;
    c_z_veg          = 0.50;   
    c_rp_veg         = 0.15;
    c_rp_veg_eq      = 0.35;
    c_veg_revert     = 0.25;
    %
    std_RES_PIE_VEG        = 10;
    std_RES_LRP_VEG_EQ     = 0.5;
    std_RES_DOT_LRP_VEG_EQ = 0.5;
  'Fuels inflation'    
    c_lag_fuel       = 0.12;
    c_oil_fuel       = 0.025;
    c_rp_fuel        = 0.05; 
    c_rp_fuel_eq     = 0.5;
    %
    std_RES_PIE_FUEL        = 4.0;
    std_RES_LRP_FUEL_EQ     = 0.5;
    std_RES_DOT_LRP_FUEL_EQ = 0.5;
  'Regulated services inflation'
    c_lag_sreg       = 0.20;
    c_rp_sreg        = 0.05;
    c_rp_sreg_eq     = 0.35;
    %
    std_RES_PIE_SREG        = 1.4;
    std_RES_LRP_SREG_EQ     = 0.5;
    std_RES_DOT_LRP_SREG_EQ = 0.5;
  'Volatile inflation'
    c_lag_vol        = 0.20;
    c_rp_vol         = 0.15;
    c_rp_vol_eq      = 0.25;
    %
    std_RES_PIE_VOL        = 3.3;
    std_RES_LRP_VOL_EQ     = 0.5;
    std_RES_DOT_LRP_VOL_EQ = 0.5; 
  'Relative prices'
    rho_rp_veg_eq    = 0.50;
    rho_rp_fuel_eq   = 0.50;
    rho_rp_sreg_eq   = 0.50;
    rho_rp_vol_eq    = 0.50;
  'Aggregation'    
    w_core           = 0.7107; 
    w_veg            = 0.0460;  
    w_fuel           = 0.0464; 
    w_sreg           = 0.1188; 
    w_vol;
    w_nc;
    c_sf_pie         = 0.70;
    std_RES_PIE_NC4_SF = 0.0;
  'GDP deflator'
    c_defl_cpi = 0.90;
    c_defl_oil = 0.14;
    rho_defl   = 0.63;
    std_RES_DOT4_Y_DEFL = 1.83;
    
!links    
    w_vol = 1 - w_core - w_veg - w_fuel - w_sreg;
    w_nc  = 1 - w_core;
    w_h   = 1 - w_m*w_m_d / (w_d*w_df);

    
    !parameters
    delta          = 0.8; 
    delta_cc       = 0.5; 
    chi            = 0.5;
    chi_oil        = 0.05;
    %
    !if capital_controls == true
    w_cc           = 0.75;
    !else
    w_cc           = 0.0;
    !end
    c_prem_bop     = 0.05;
    c_tot_elast    = 0.35;
    c_prem_bop_cc  = 1.00; 
    c_tot_elast_cc = 1.00; 
  'Steady state of country risk premium' PREM_SS = 100*log(1+3.28/100);
    rho_prem_eq    = 0.9;
    c_prem_tot     = 0.05; 
    rho_prem_trans = 0.5;
    %
    rho_z_eq   = 0.80;
    c_z_eq_bop = 0.20;
    %
    std_RES_LZ_GAP     = 10;
    std_RES_PREM       = 1.0;
    std_RES_PREM_EQ    = 0.15;
    std_RES_PREM_TRANS = 1.25;
    std_RES_DOT_LZ_EQ  = 0.50; 
    std_RES_E_LZ_EQ    = 0.25; 
    std_RES_LS_USD     = 0.75; 
    std_RES_OBS_X  = 1.0;

    !parameters
    PIE_TAR_SS = 100*log(1+4.0/100);
    gamma1 = 0.75; 
    
    !if monetary_hard == true
    gamma2=1.9
    !else 
    gamma2 = 1.5;
    !end
    
    gamma3=0.5;
    psi    = 0.9999;    
    w_mp_pie_c = 0.75;
    lappa = 0.50;
    gamma_ext = 1.00;
    h_rr_y    = 0.00;
    %
    std_RES_RS = 1;
    std_RES_PIE_TAR = 0.25;

