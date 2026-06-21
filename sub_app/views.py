from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required

@login_required
def sub(request):
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():
            n1 = float(form_in.cleaned_data['num1'])
            n2 = float(form_in.cleaned_data['num2'])
            answer = n1 - n2
            form_out = FormOutput(initial={'ans':answer,})
    else:
        form_in = FormInput()
        form_out = FormOutput()
    return render(request, "sub_app/sub.html", {'form_input': form_in, 'form_output': form_out})
