***Dissertation Partial Data 30-12-2025

reshape long notional_principal loss pv01 roa nim pat total_assets ldr lta efficiency_ratio gnpa car roe npm debt_asset_ratio debt
> _equity_ratio, i(bank) j(fy ) 
* - already long data 

*checking vacant cells
mdesc

egen id = group(bank )

sum

distinct id


mdesc

drop if loss ==.

drop if pv01 ==.

mdesc

sum

replace efficiency_ratio =0 if efficiency_ratio ==.

***variable construction

*Dep variable

gen nim 

*Indep variable

gen patdummy = cond(pat>0,1,0)

*WINSORISING THE VARIABLE (To take care of outliers)

winsor nim, gen(wnim) p(0.1)
winsor n_p, gen(wnp) p(1)
winsor loss, gen(wloss) p(0.1)
winsor pv01, gen(wpv01) p(0.1)
winsor roa, gen(wroa) p(0.1)
winsor pat, gen(wpat) p(0.1)
winsor t_a, gen(wta) p(0.1)
winsor ldr, gen(wldr) p(0.1)
winsor lta, gen(wlta) p(0.1)
winsor eff_r , gen(weff_r) p(0.1)
winsor gnpa, gen(wgnpa) p(0.1)
winsor car, gen(wcar) p(0.1)
winsor roe, gen(wroe) p(0.1)
winsor npm, gen(wnpm) p(0.1)
winsor d_a_r, gen(wdar) p(0.1)
winsor d_e_r, gen(wder) p(0.1)
winsor d_nim, gen(wdnim) p(0.1)

winsor nim, gen(wnim) p(0.1)
winsor n_p, gen(wnp) p(0.1)
winsor loss, gen(wloss) p(0.1)
winsor pv01, gen(wpv01) p(0.1)
winsor roa, gen(wroa) p(0.1)
winsor pat, gen(wpat) p(0.1)
winsor t_a, gen(wta) p(0.1)
winsor ldr, gen(wldr) p(0.1)
winsor lta, gen(wlta) p(0.1)
winsor eff_r , gen(weff_r) p(0.1)
winsor gnpa, gen(wgnpa) p(0.1)
winsor car, gen(wcar) p(0.1)
winsor roe, gen(wroe) p(0.1)
winsor npm, gen(wnpm) p(0.1)
winsor d_a_r, gen(wdar) p(0.1)
winsor d_e_r, gen(wder) p(0.1)
winsor d_nim, gen(wdnim) p(0.1)

winsor2 n_p, cuts(5 95)
winsor2 loss , cuts(5 95)
winsor2 pv01  , cuts(5 95)
winsor2 nim   , cuts(1 99)
winsor2 d_nim , cuts(1 99)
winsor2 t_a  , cuts(1 99)
winsor2 ldr   , cuts(1 99)
winsor2 eff_r , cuts(1 99)
winsor2 gnpa  , cuts(1 99)
winsor2 car  , cuts(1 99)

gen lnn_p_w = ln(n_p_w )

gen lnpv01_w = ln(pv01_w  )

gen lnt_a_w = ln(t_a_w )


sum

***Panel Data Regression



gen ln_wnim = ln(wnim)
gen ln_wnp = ln(wnp)
gen ln_wloss = ln(wloss)
gen ln_wpv01 = ln(wpv01)
gen ln_wroa = ln(wroa)
gen ln_wpat = ln(wpat)
gen ln_wta = ln(wta)
gen ln_wldr = ln(wldr)
gen ln_wlta = ln(wlta)
gen ln_weff_r = ln(weff_r)
gen ln_wgnpa = ln(wgnpa)
gen ln_wcar = ln(wcar)
gen ln_wroe = ln(wroe)
gen ln_wnpm = ln(wnpm)
gen ln_wdar = ln(wdar)
gen ln_wder = ln(wder)

xtset id year

xtreg wnim wnp wloss wpv01 wroa wpat wta wldr wlta weff_r wgnpa wcar wroe wnpm wdar wder, fe

estimates store fe

xtreg wnim wnp wloss wpv01 wroa wpat wta wldr wlta weff_r wgnpa wcar wroe wnpm wdar wder, fe

estimates store re

hausman fe re 

xtreg ln_wnim ln_wnp ln_wloss ln_wpv01 ln_wroa ln_wpat ln_wta ln_wldr ln_wlta ln_weff_r ln_wgnpa ln_wcar ln_wroe ln_wnpm ln_wdar ln_wder, fe

estimates store fe

xtreg ln_wnim ln_wnp ln_wloss ln_wpv01 ln_wroa ln_wpat ln_wta ln_wldr ln_wlta ln_weff_r ln_wgnpa ln_wcar ln_wroe ln_wnpm ln_wdar ln_wder, re

estimates store re

hausman fe re 



gen ln_np = ln(n_p)

xtreg roa_2 n_p t_a car ldr,fe