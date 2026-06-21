from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from . import bush
import math

@login_required
def rw_bush_fcn(request):
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
                    if x_key != 'e' and x_key != 's' and x_key != 'phi' and x_key != 'q' and x_key != 'h_min':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    w = float(this_form_in.cleaned_data['w'])  # load in ton
                    d = float(this_form_in.cleaned_data['d'])  # dia in mm
                    l = float(this_form_in.cleaned_data['l'])  # bush length in mm
                    cd = float(this_form_in.cleaned_data['cd'])  # diameteral clearance in mm
                    n = float(this_form_in.cleaned_data['n'])  # shaft rpm
                    mu = float(this_form_in.cleaned_data['mu'])  # dyn visc in Pa.s

                    c = cd/2  # radial clr in mm
                    
                    ans_dic = bush.hyd_dyn_bush(w * 10000, d / 1000, l / 1000, c / 1000, n, mu)
                    e = ans_dic['e']  # ecc ratio
                    s = ans_dic['s']  # sommerfeld no
                    phi = ans_dic['phi'] * 180 / math.pi  # attitude angle in deg
                    q = ans_dic['q'] * 1000000 * 60  # flow in cc/min
                    h_min = ans_dic['h_min'] * 1000000  # min film thk micron

                    e = remove_trailing_0_fcn(round(e, 3)) # to remove trailing 0s.
                    s = remove_trailing_0_fcn(round(s, 3)) # to remove trailing 0s.
                    phi = remove_trailing_0_fcn(round(phi, 2)) # to remove trailing 0s.
                    q = remove_trailing_0_fcn(round(q, 3)) # to remove trailing 0s.
                    h_min = remove_trailing_0_fcn(round(h_min, 4)) # to remove trailing 0s.


                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'e':e, 's':s, 'phi':phi, 'q':q, 'h_min':h_min,}) # to fill mass in form

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
    
    return render(request, "rw_bush_app/rw_bush.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
