from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from. import ps
import math

@login_required
def rw_powerscrew_fcn(request):
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
                    if x_key != 'tr' and x_key != 'tl' and x_key != 'eff':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    w = float(this_form_in.cleaned_data['w'])  # load in ton
                    dm = float(this_form_in.cleaned_data['dm'])  # mean collar dia in mm
                    l = float(this_form_in.cleaned_data['l'])  # lead in mm
                    th = float(this_form_in.cleaned_data['th'])  # half of screw angle in deg
                    mus = float(this_form_in.cleaned_data['mus'])  # cof of screw
                    dmc = float(this_form_in.cleaned_data['dmc'])  # mean collar dia in mm
                    muc = float(this_form_in.cleaned_data['muc'])  # collar cof

                    th_rad = th * math.pi / 180

                    tr = ps.get_tr(dm / 1000, w * 10000, mus, l / 1000, th_rad, dmc / 1000, muc)  # all in SI units
                    tl = ps.get_tl(dm / 1000, w * 10000, mus, l / 1000, th_rad, dmc / 1000, muc)
                    eff = ps.get_eff(dm / 1000, mus, l / 1000, th_rad, dmc / 1000, muc)  # screw efficiency

                    tr = remove_trailing_0_fcn(round(tr, 1)) # to remove trailing 0s. Units In Nm
                    tl = remove_trailing_0_fcn(round(tl, 1)) # to remove trailing 0s
                    eff = remove_trailing_0_fcn(round(eff, 2)) # to remove trailing 0s
                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'tr':tr,'tl':tl, 'eff':eff,}) # to fill mass in form

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
    
    return render(request, "rw_powerscrew_app/rw_powerscrew.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
