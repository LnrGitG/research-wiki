
function m = get_ss_growth_rates( m )


for j = 1:length(m)
    
mj = m(j);

mj.DOT_X_SS = ( mj.w_x_no * mj.x_eq_yf * mj.DOT_YF_SS ) + ( mj.w_x_o * mj.DOT_X_O_SS );

DOT_N_SS = mj.DOT_LF_SS;  
DOT_YD_SS = @(DOT_M_SS) mj.DOT_TFP_SS + (1-mj.alpha_m)*mj.alpha_d*DOT_N_SS + mj.alpha_m*DOT_M_SS;
DOT_Y_SS = @(DOT_M_SS) mj.w_x*mj.DOT_X_SS + (1-mj.w_x)*DOT_YD_SS(DOT_M_SS);

DOT_D_SS = @(DOT_M_SS) (DOT_Y_SS(DOT_M_SS) - mj.w_x*mj.DOT_X_SS + mj.w_m*DOT_M_SS) / mj.w_d;

fun = @(DOT_M_SS) DOT_M_SS - ( mj.m_d*DOT_D_SS(DOT_M_SS) );
mj.DOT_M_SS = fzero(fun, 1.50);

DOT_YD_SS = DOT_YD_SS(mj.DOT_M_SS);
mj.DOT_D_SS = DOT_D_SS(mj.DOT_M_SS);
mj.DOT_Y_SS = DOT_Y_SS(mj.DOT_M_SS);
m(j) = mj;

end


end

