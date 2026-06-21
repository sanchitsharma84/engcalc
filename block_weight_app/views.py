from django.shortcuts import render
from .form_block_input import FormInput
from .form_block_output import FormOutput
from django.contrib.auth.decorators import login_required
import math

@login_required
def block_weight_fcn(request):
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():
            for x_keys, y_values in form_in.cleaned_data.items():
                if y_values == None:
                    form_in.cleaned_data[x_keys] = 0

                pass 
            density = float(form_in.cleaned_data['density'])  # kg/m3

            l_b = float(form_in.cleaned_data['l_b']) / 1000  # m, x axis
            w_b = float(form_in.cleaned_data['w_b']) / 1000  # m, y axis
            h_b = float(form_in.cleaned_data['h_b']) / 1000  # m, z axis
            qty_b = float(form_in.cleaned_data['qty_b'])

            od_c = float(form_in.cleaned_data['od_c']) / 1000  # m
            or_c = od_c / 2  # outer radius in m
            id_c = float(form_in.cleaned_data['id_c']) / 1000  # m
            ir_c = id_c / 2  # inner radius in m
            l_c = float(form_in.cleaned_data['l_c']) / 1000  # m
            qty_c = float(form_in.cleaned_data['qty_c'])
            
            # block calculations
            m_b = qty_b * l_b * w_b * h_b * density  # mass in kg
            ix_b = m_b * (w_b**2 + h_b**2) / 12  # I-xx in kgm2
            iy_b = m_b * (l_b**2 + h_b**2) / 12  # I-yy in kgm2
            iz_b = m_b * (l_b**2 + w_b**2) / 12  # I-zz in kgm2

            # cylinder calculations 
            m_c = qty_c * 0.25 * math.pi * (od_c**2 - id_c**2) * l_c * density  # mass in kg
            ix_c = 0.5 * m_c * (or_c**2 + ir_c**2)  # I-xx in kgm2
            iy_c = m_c * (3 * (or_c**2 + ir_c**2) + l_c**2) / 12  # I-yy = I-zz in kgm2
            iz_c = iy_c  # I-yy = I-zz in kgm2


            form_out = FormOutput(initial={'m_b':round(m_b, 6),
                                           'ix_b':round(ix_b, 6),
                                           'iy_b':round(iy_b, 6),
                                           'iz_b':round(iz_b, 6),
                                           'm_c':round(m_c, 6),
                                           'ix_c':round(ix_c, 6),
                                           'iy_c':round(iy_c, 6),
                                           'iz_c':round(iz_c, 6),
                                           })
    else:
        form_in = FormInput()
        form_out = FormOutput()
    return render(request, "block_weight_app/block_weight.html", {'form_input': form_in, 'form_output': form_out})
