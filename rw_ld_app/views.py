from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from mechpress import ld
from .ld_link_len_gen import get_link_len
import math

@login_required
def rw_ld_fcn(request):
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
                    if x_key != 'teg' and x_key != 'fbos' and x_key != 'vel':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    pf = float(this_form_in.cleaned_data['pf'])  # force in ton
                    stk = float(this_form_in.cleaned_data['stk'])  # stroke in mm
                    rd = float(this_form_in.cleaned_data['rd'])  # rated distance in mm
                    spm = float(this_form_in.cleaned_data['spm'])  # press spm
                    ca = float(this_form_in.cleaned_data['ca'])  # crank angle in deg
                    
                    link_len_lst = get_link_len(stk)
                    
                    a = link_len_lst[0] / 1000  # ecc in m
                    b = link_len_lst[1] / 1000  # ternary link len - rocker side in m
                    c = link_len_lst[2] / 1000  # rocker len in m
                    d = link_len_lst[3] / 1000  # rocker y in m
                    e = link_len_lst[4] / 1000  # rocker x in m
                    f = link_len_lst[5] / 1000  # ternary link len - conrod side in m
                    g = link_len_lst[6] / 1000  # conrod len in m
                    h = link_len_lst[7] / 1000  # slide offset in m
                    tht = link_len_lst[8] * math.pi / 180  # ternary link angle in rad

                    w2 = 2 * math.pi * spm / 60  # press speed in rad/s

                    ld_obj = ld.LD(a, b, c, e, d, tht, g, h, f, pf * 10000, rd / 1000)
                    teg = ld_obj.get_eg_torque() # eg torque in Nm
                    fbos_lst = ld_obj.get_fbos_lst() # fbos list, 3600 elements
                    vel_lst = ld_obj.get_vel_lst(w2) # slide vel list, 3600 elements
                    fbos = fbos_lst[int(ca * 10)] * 1000  # fbos in mm
                    vel = vel_lst[int(ca * 10)] * 1000  # slide vel in mm/s

                    teg = remove_trailing_0_fcn(round(teg, 0)) # to remove trailing 0s.
                    fbos = remove_trailing_0_fcn(round(fbos, 1)) # to remove trailing 0s.
                    vel = remove_trailing_0_fcn(round(vel, 0)) # to remove trailing 0s.

                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'teg':teg,'fbos':fbos,'vel':vel,}) # to fill mass in form

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
    
    return render(request, "rw_ld_app/rw_ld.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
