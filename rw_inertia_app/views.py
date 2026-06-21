from django.shortcuts import render
from .form_in import FormIn
from .form_in_const import FormInConst
from .form_out_total import FormOutTotal
from django.contrib.auth.decorators import login_required

import math

@login_required
def rw_inertia_fcn(request):
    form_in_lst = []
    nr_rows = 20 # number of rows to be displayed on page
    
    if request.method == 'POST':
        form_in_const = FormInConst(request.POST)  # for constant value which is alid throughout the page
        if form_in_const.is_valid():
            DEN = float(form_in_const.cleaned_data['DEN']) 

        total_mass = 0  # to display total of all weight fields on top of page
        total_inertia = 0  # to display total of all inertia fields on top of page
        
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
                    if x_key != 'ans_mass' and x_key != 'ans_inertia':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False
                
                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    thk = float(this_form_in.cleaned_data['thk'])  # to extract value of fields named num1
                    l = float(this_form_in.cleaned_data['l'])  # to extract value of fields named num2
                    w = float(this_form_in.cleaned_data['w'])  # to extract value of fields named num2
                    # density = float(this_form_in.cleaned_data['density'])  # to extract value of fields named num2
                    qty = float(this_form_in.cleaned_data['qty'])  # to extract value of fields named num2
                    shape = str(this_form_in.cleaned_data['shape'])  # to extract value of fields named num2
                    
                    if shape == 'P':
                        mass =  qty * DEN * (thk * l * w) / 1000000000  # mass is in kg
                        inertia = mass * ((l/1000)**2 + (w/1000)**2) / 12  # inertia in kgm2
                    elif shape == 'R':
                        mass = (thk/1000) * qty * DEN * 0.25 * math.pi * ((l/1000)**2 - (w/1000)**2)  # mass is in kg
                        inertia = 0.5 * mass * ((l/2000)**2 + (w/2000)**2)  # inertia in kgm2
                    else: 
                        mass = 0
                        inertia = 0

                    total_mass = round(total_mass + mass, 3)
                    total_inertia = round(total_inertia + inertia, 6)

                    mass = remove_trailing_0_fcn(round(mass, 3)) # to remove trailing 0s
                    inertia = remove_trailing_0_fcn(round(inertia, 6)) # to remove trailing 0s

                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'ans_mass':mass,'ans_inertia':inertia,}) # to fill mass in form

                form_in_lst.append(this_form_in)  # to attach ths form in list of forms (this is done only if the form is valid)
            
            # else is used to handle invalid forms
            else:
                form_in_lst.append(this_form_in) # this is to handle invalid forms
                # if else is not used, then the form row with invalid data will be erased from page

            total_mass = remove_trailing_0_fcn(total_mass) # to remove trailing 0s
            total_inertia = remove_trailing_0_fcn(total_inertia) # to remove trailing 0s

            # form_out_total = FormOutTotal(initial={'total':total, 'total_inertia':total_inertia})
            form_out_total = FormOutTotal(initial={'mass_total':total_mass, 'inertia_total':total_inertia})

    
    else:
        for x in range(nr_rows):
            prefix_str = "form_in" + str(x)
            this_form_in = FormIn(prefix=prefix_str)
            form_in_lst.append(this_form_in)
        
        form_out_total = FormOutTotal()
        form_in_const = FormInConst()

    
    return render(request, "rw_inertia_app/rw_inertia.html", {'form_in_lst':form_in_lst,
                                                              'form_out_total':form_out_total,
                                                              'form_in_const':form_in_const})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number
