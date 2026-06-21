from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from .gear_strength import GearStrength

import math

@login_required
def rw_gearstrength_fcn(request):
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
                    if x_key != 'trq' and x_key != 'pcd_p' and x_key != 'pcd_g' and x_key != 'fw':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    m = float(this_form_in.cleaned_data['m'])  # normal module
                    h = float(this_form_in.cleaned_data['h'])  # helix angle in deg
                    zp = float(this_form_in.cleaned_data['zp'])  # no of teeth in pinion
                    zg = float(this_form_in.cleaned_data['zg'])  # no of teeth in gear

                    gs_obj = GearStrength(m, h, zp, zg)
                    trq = gs_obj.get_torque()  # Nm
                    pcd_p = m * zp / math.cos(h * math.pi/180)
                    pcd_g = m * zg / math.cos(h * math.pi/180)
                    fw = m * 15

                    trq = remove_trailing_0_fcn(round(trq, 0)) # to remove trailing 0s
                    pcd_p = remove_trailing_0_fcn(round(pcd_p, 3)) # to remove trailing 0s
                    pcd_g = remove_trailing_0_fcn(round(pcd_g, 3)) # to remove trailing 0s
                    fw = remove_trailing_0_fcn(round(fw, 0)) # to remove trailing 0s



                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'trq':trq, 'pcd_p':pcd_p, 
                                                                                    'pcd_g':pcd_g, 'fw':fw,}) # to fill mass in form

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
    
    return render(request, "rw_gearstrength_app/rw_gearstrength.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
