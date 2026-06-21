from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from mechpress import section_mi, crown
import math

@login_required
def rw_crown_fcn(request):
    form_in_lst = []
    nr_rows = 5 # number of rows to be displayed on page
    
    if request.method == 'POST':

        # handling forms one by one using loop
        # forms are differentiated based on prefix number which is loop index
        # one row of calculation is 1 form
        # input from POST request if a list of forms
        for x in range(nr_rows):
            prefix_str = "form_in" + str(x)  # prefix to differentiate froms
            this_form_in = FormIn(request.POST, prefix=prefix_str)  # one form from the list of form
            
            if this_form_in.is_valid():
                form_ok_bool = True  # flag to check if any field in form is None

                # following code checks if there is any None type data in any of the input field in form under observation.  
                # If yes, then it sets a flag to false and further calculations are not performed on that form
               
                for x_key, y_value in this_form_in.cleaned_data.items():
                    if x_key != 'sb' and x_key != 'ss' and x_key != 'def_m' and x_key != 'def_s' and x_key != 'def_pm'\
                        and x_key != 'sec_a' and x_key != 'weight':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    tfx = float(this_form_in.cleaned_data['tfx'])  # top flange x in mm
                    tfy = float(this_form_in.cleaned_data['tfy'])  # top flange y in mm
                    bfx = float(this_form_in.cleaned_data['bfx'])  # bottom flange x in mm
                    bfy = float(this_form_in.cleaned_data['bfy'])  # bottom flange y in mm
                    wx = float(this_form_in.cleaned_data['wx'])  # web x in mm
                    wy = float(this_form_in.cleaned_data['wy'])  # web y in mm
                    rtx = float(this_form_in.cleaned_data['rtx'])  # top reinforced plate x in mm
                    rty = float(this_form_in.cleaned_data['rty'])  # top reinforced plate y in mm
                    rbx = float(this_form_in.cleaned_data['rbx'])  # bottom reinforced plate x in mm
                    rby = float(this_form_in.cleaned_data['rby'])  # bottom reinforced plate y in mm
                    e = float(this_form_in.cleaned_data['e'])  # Youngs modulus in MPa
                    g = float(this_form_in.cleaned_data['g'])  # Shear modulus in MPa
                    pf = float(this_form_in.cleaned_data['pf'])  # force on beam in ton
                    cd = float(this_form_in.cleaned_data['cd'])  # support CD in mm
                    cd_sus = float(this_form_in.cleaned_data['cd_sus'])  # suspension cd in mm

                    sec_obj = section_mi.Section_mi(tfx, tfy, wx, wy, bfx, bfy, rtx, rty, rbx, rby)
                    sec_c = sec_obj.get_centroid()  # from bottom in mm
                    sec_i = sec_obj.get_inertia()  # section inertia in  mm4
                    sec_a = sec_obj.get_section_area()  # section x-sec area in mm2
                    sec_h = tfy + wy + bfy  # section height in mm2
                    sec_y = max(sec_c, sec_h - sec_c)  # distance of farthest fiber from centrid in mm 
                    weight = sec_a * cd * 7.85 * 1e-6
                    
                    crown_obj = crown.Crown(pf * 1e4, cd / 1e3, cd_sus / 1e3, sec_y / 1e3, sec_i / 1e12, wx / 1e3, wy / 1e3, e * 1e6, g * 1e6)
                    
                    sb = crown_obj.get_sb() / 1e6  # bending stress in MPa
                    ss = crown_obj.get_ss() / 1e6  # shear stress in MPa
                    def_m = crown_obj.get_def_b() * 1e3  # deflection due to bending in mm
                    def_s = crown_obj.get_def_s() * 1e3  # deflection due to shear in mm
                    def_pm = (def_m + def_s) / (cd/1e3)  # total deflection in mm/m

                    sec_a = remove_trailing_0_fcn(round(sec_a, 0)) # to remove trailing 0s.
                    weight = remove_trailing_0_fcn(round(weight, 0)) # to remove trailing 0s.

                    sb = remove_trailing_0_fcn(round(sb, 0)) # to remove trailing 0s.
                    ss = remove_trailing_0_fcn(round(ss, 0)) # to remove trailing 0s.
                    def_m = remove_trailing_0_fcn(round(def_m, 4)) # to remove trailing 0s.
                    def_s = remove_trailing_0_fcn(round(def_s, 4)) # to remove trailing 0s.
                    def_pm = remove_trailing_0_fcn(round(def_pm, 4)) # to remove trailing 0s.

                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'sb':sb, 'ss':ss, 
                                                                                    'def_m':def_m, 'def_s':def_s, 
                                                                                    'def_pm':def_pm,'sec_a':sec_a,
                                                                                    'weight':weight,}) # to fill mass in form

                form_in_lst.append(this_form_in)  # to attach ths form in list of forms (this is done only if the form is valid)
            
            # else is used to handle invalid forms
            else:
                form_in_lst.append(this_form_in) # this is to handle invalid forms
                # if else is not used, then the form row with invalid data will be erased from page
    
    else:
        for x in range(nr_rows):
            prefix_str = "form_in" + str(x)
            this_form_in = FormIn(prefix=prefix_str)
            form_in_lst.append(this_form_in)
    
    return render(request, "rw_crown_app/rw_crown.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
