from django.shortcuts import render
from .form_in import FormIn
from .form_in_const import FormInConst
from .form_out_total import FormOutTotal
from django.contrib.auth.decorators import login_required

import math

@login_required
def rw_weight_fcn(request):
    form_in_lst = []
    nr_rows = 20 # number of rows to be displayed on page
    
    if request.method == 'POST':
        form_in_const = FormInConst(request.POST)  # for constant value which is alid throughout the page
        if form_in_const.is_valid():
            DEN = float(form_in_const.cleaned_data['DEN']) 

        total = 0  # to display total of all output fields on top of page
        
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
                    if x_key != 'ans':  # output fields are not checked for None value as they will be None generally
                        if y_value == None:  # if any input field is None then bool is set to false and further calculations are not performed
                            form_ok_bool = False
                
                # if all fields have valid data, calculations are performed on that form
                if form_ok_bool:
                    thk = float(this_form_in.cleaned_data['thk'])
                    l = float(this_form_in.cleaned_data['l'])
                    w = float(this_form_in.cleaned_data['w'])
                    qty = float(this_form_in.cleaned_data['qty'])
                    shape = str(this_form_in.cleaned_data['shape'])
                    
                    if shape == 'P':
                        answer = thk * l * w * qty * DEN
                    elif shape == 'R':
                        answer = thk * qty * DEN * 0.25 * math.pi * (l**2 - w**2)
                    else: answer = 0

                    total = round(total + answer, 3)
                    answer = remove_trailing_0_fcn(round(answer, 3)) # to remove trailing 0s
                    
                    this_form_in = FormIn(request.POST, prefix=prefix_str, initial={'ans':answer,}) # to fill answer in form

                form_in_lst.append(this_form_in)  # to attach ths form in list of forms (this is done only if the form is valid)
            
            # else is used to handle invalid forms
            else:
                form_in_lst.append(this_form_in) # this is to handle invalid forms
                # if else is not used, then the form row with invalid data will be erased from page

            total = remove_trailing_0_fcn(total) # to remove trailing 0s
            form_out_total = FormOutTotal(initial={'total':total})
    
    else:
        for x in range(nr_rows):
            prefix_str = "form_in" + str(x)
            this_form_in = FormIn(prefix=prefix_str)
            form_in_lst.append(this_form_in)
        
        form_out_total = FormOutTotal()
        form_in_const = FormInConst()
    
    return render(request, "rw_weight_app/rw_weight.html", {'form_in_lst':form_in_lst,
                                                            'form_out_total':form_out_total, 
                                                            'form_in_const':form_in_const})
    

# method to remove trailing zeros
def remove_trailing_0_fcn(number):
    diff_number = number -int(number)
    if diff_number == 0:
        number = int(number)
    
    return number

