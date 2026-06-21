from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from .spherical_contact import SphericalContact

import math

@login_required
def rw_sphcontact_fcn(request):
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
                    if x_key != 'a' and x_key != 'p':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False

                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    f = float(this_form_in.cleaned_data['f'])  # contact force in N
                    v1 = float(this_form_in.cleaned_data['v1'])  # poissions ratio material 1
                    v2 = float(this_form_in.cleaned_data['v2'])  # poissions ratio material 2
                    e1 = float(this_form_in.cleaned_data['e1'])  # Youngs modulus material 1 in MPa
                    e2 = float(this_form_in.cleaned_data['e2'])  # Youngs modulus material 2 in MPa
                    d1 = float(this_form_in.cleaned_data['d1'])  # Dia of sphere 1 in mm
                    d2 = float(this_form_in.cleaned_data['d2'])  # Dia of sphere 2 in mm

                    sc_obj = SphericalContact(f, v1, v2, e1, e2, d1, d2)
                    a = sc_obj.get_contact_radius()  # mm
                    p = sc_obj.get_stress()  # MPa


                    a = remove_trailing_0_fcn(round(a, 3)) # to remove trailing 0s
                    p = remove_trailing_0_fcn(round(p, 0)) # to remove trailing 0s

                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'a':a,'p':p,}) # to fill mass in form

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
    
    return render(request, "rw_sphcontact_app/rw_sphcontact.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
