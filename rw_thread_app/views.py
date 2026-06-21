from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
import math

@login_required
def rw_thread_fcn(request):
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

                for x_key, y_value in this_form_in.cleaned_data.items():
                    if x_key == 'f' and y_value == None:  # output fields are not checked for None value as they will be None generally
                        this_form_in.cleaned_data[x_key] = 0
                    if x_key == 'nut_l' and y_value == None:  # output fields are not checked for None value as they will be None generally
                        this_form_in.cleaned_data[x_key] = 0

                # following code checks if there is any None type data in any of the input field in form under observation.  
                # If yes, then it sets a flag to false and further calculations are not performed on that form
               
                for x_key, y_value in this_form_in.cleaned_data.items():
                    if x_key != 'dm_ext' and x_key != 'dm_int' and x_key != 'ss' and x_key != 'sc':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                
                
                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    d = float(this_form_in.cleaned_data['d'])
                    p = float(this_form_in.cleaned_data['p'])
                    nut_l = float(this_form_in.cleaned_data['nut_l'])
                    f = float(this_form_in.cleaned_data['f'])

                    dm_ext = d - 1.227 * p
                    dm_int = d - 1.083 * p

                    if nut_l == 0 or p == 0:
                        ss = 0
                        sc = 0

                    else:
                        nr_thread = nut_l / p
                        ss = f * 10000 / (math.pi * d * nut_l * 0.8)
                        sc = f * 10000 / (0.25 * math.pi * (d**2 - dm_int**2) * nr_thread)
                    


                    dm_ext = remove_trailing_0_fcn(round(dm_ext, 3)) # to remove trailing 0s
                    dm_int = remove_trailing_0_fcn(round(dm_int, 3)) # to remove trailing 0s
                    ss = remove_trailing_0_fcn(round(ss, 3)) # to remove trailing 0s
                    sc = remove_trailing_0_fcn(round(sc, 3)) # to remove trailing 0s
                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'dm_ext':dm_ext,'dm_int':dm_int,
                                                                                    'ss':ss,'sc':sc,}) # to fill mass in form

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
    
    return render(request, "rw_thread_app/rw_thread.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
