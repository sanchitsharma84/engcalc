from django.shortcuts import render
from .form_in import FormIn
from django.contrib.auth.decorators import login_required
from .ecc_drive_torque import EccentricDriveTorque


import math

@login_required
def rw_presstorque_fcn(request):
    form_in_lst = []
    nr_rows = 20 # number of rows to be displayed on page
    
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
                    if x_key != 'torque' and x_key != 'alp_deg' and x_key != 'beta_deg':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False
                
                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    stroke = float(this_form_in.cleaned_data['stroke'])  
                    rd = float(this_form_in.cleaned_data['rd'])  
                    force = float(this_form_in.cleaned_data['force'])   

                    ed = EccentricDriveTorque(stroke / 2, stroke * 3, rd, force)
                    torque = ed.get_torque()
                    alp_deg = ed.get_alp_deg()
                    beta_deg = ed.get_beta_deg()

                    torque = remove_trailing_0_fcn(round(torque, 0)) # to remove trailing 0s
                    alp_deg = remove_trailing_0_fcn(round(alp_deg, 2)) # to remove trailing 0s
                    beta_deg = remove_trailing_0_fcn(round(beta_deg, 2)) # to remove trailing 0s

                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'torque':torque,'alp_deg':alp_deg,'beta_deg':beta_deg,}) # to fill mass in form

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
    
    return render(request, "rw_presstorque_app/rw_presstorque.html", {'form_in_lst':form_in_lst,})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
