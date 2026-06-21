from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from .gear import GearGeometry
import math

@login_required
def rw_gear_fcn(request):
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
                    if x_key != 'pcd_p' and x_key != 'pcd_g' and x_key != 'w_pcd_p' and x_key != 'w_pcd_g' and \
                        x_key != 'od_p' and x_key != 'od_g' and x_key != 'root_d_p' and x_key != 'root_d_g' and \
                            x_key != 'cd':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False
                
                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    m = float(this_form_in.cleaned_data['m'])  
                    helix = float(this_form_in.cleaned_data['helix'])  
                    zp = int(this_form_in.cleaned_data['zp'])  
                    xp = float(this_form_in.cleaned_data['xp'])  
                    zg = int(this_form_in.cleaned_data['zg'])  
                    xg = float(this_form_in.cleaned_data['xg'])  

                    pa_deg = 20  # pressure angle in deg
                    pa_rad = pa_deg * math.pi / 180  # pressure angle in rad

                    helix_rad = helix * math.pi / 180  # pressure angle in rad

                    # making gear geometry object
                    gg = GearGeometry(m, pa_rad, helix_rad, zp, zg, xp, xg)

                    # function common to S0 and S
                    pcd_p = gg.getPcd1()
                    pcd_g = gg.getPcd2()
                    w_pcd_p = gg.workCirDia1()
                    w_pcd_g = gg.workCirDia2()
                    root_d_p = gg.getRootCirDia1()
                    root_d_g = gg.getRootCirDia2()
                    cd = gg.getA_S()
                    
                    # function different for S0 and S
                    if abs(xp) == abs(xg):
                        # S0 gearing
                        od_p = gg.getTipCirDia1_S0()
                        od_g = gg.getTipCirDia2_S0()
                    else: 
                        # S gearing
                        od_p = gg.getTipCirWtDia1_S()
                        od_g = gg.getTipCirWtDia2_S()

                    pcd_p = remove_trailing_0_fcn(round(pcd_p, 3)) # to remove trailing 0s
                    pcd_g = remove_trailing_0_fcn(round(pcd_g, 3)) # to remove trailing 0s
                    w_pcd_p = remove_trailing_0_fcn(round(w_pcd_p, 3)) # to remove trailing 0s
                    w_pcd_g = remove_trailing_0_fcn(round(w_pcd_g, 3)) # to remove trailing 0s
                    od_p = remove_trailing_0_fcn(round(od_p, 3)) # to remove trailing 0s
                    od_g = remove_trailing_0_fcn(round(od_g, 3)) # to remove trailing 0s
                    root_d_p = remove_trailing_0_fcn(round(root_d_p, 3)) # to remove trailing 0s
                    root_d_g = remove_trailing_0_fcn(round(root_d_g, 3)) # to remove trailing 0s
                    cd = remove_trailing_0_fcn(round(cd, 3)) # to remove trailing 0s

                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'pcd_p':pcd_p,'pcd_g':pcd_g,
                                                                                    'w_pcd_p':w_pcd_p,'w_pcd_g':w_pcd_g,
                                                                                    'od_p':od_p,'od_g':od_g,
                                                                                    'root_d_p':root_d_p,'root_d_g':root_d_g,
                                                                                    'cd':cd,}) # to fill mass in form

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
    
    return render(request, "rw_gear_app/rw_gear.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
