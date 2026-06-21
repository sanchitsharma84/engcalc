from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required
import math
from .ecc_drive_torque import EccentricDriveTorque
from json import dumps

@login_required
def rd_torque(request):
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():
            f = float(form_in.cleaned_data['f'])
            r = float(form_in.cleaned_data['r'])
            s = float(form_in.cleaned_data['s'])
            l = float(form_in.cleaned_data['l'])
            '''c1 = r + l - s
            alp_rad = math.acos((r**2 + c1**2 -l**2)/(2*r*c1))
            alp_deg = alp_rad * 180 / math.pi
            beta_rad = math.acos((l**2 + c1**2 -r**2)/(2*l*c1))
            beta_deg = beta_rad * 180 / math.pi
            t = 10 * f * r * (math.sin(alp_rad) + math.cos(alp_rad)*math.tan(beta_rad))  # ans in Nm
            '''
            ed = EccentricDriveTorque(r, l, s, f)
            t = ed.get_torque()
            alp_deg = ed.get_alp_deg()
            beta_deg = ed.get_beta_deg()

            f_lst = []
            th2_lst = []
            fbos_lst = []

            f_lst.clear()
            th2_lst.clear()
            fbos_lst.clear()

            th2_lst = ed.get_th2_deg_lst()
            f_lst = ed.get_f_lst()
            fbos_lst = ed.get_fbos_lst()

            # to arrange the x y data into json format
            f_th2_lst_of_dic_lst = []
            f_th2_lst_of_dic_lst.clear()

            f_fbos_lst_of_dic_lst = []
            f_fbos_lst_of_dic_lst.clear()

            for index in range(len(th2_lst)):
                f_th2_temp_dic = {"x": th2_lst[index], "y":f_lst[index]}
                f_th2_lst_of_dic_lst.append(f_th2_temp_dic)

                f_fbos_temp_dic = {"x": fbos_lst[index], "y":f_lst[index]}
                f_fbos_lst_of_dic_lst.append(f_fbos_temp_dic)

            f_th2_dic = {
                "xy_data":f_th2_lst_of_dic_lst,
            }
            f_th2_dataJSON = dumps(f_th2_dic)

            f_fbos_dic = {
                "xy_data":f_fbos_lst_of_dic_lst,
            }
            f_fbos_dataJSON = dumps(f_fbos_dic)

            form_out = FormOutput(initial={'t':round(t, 1),'alp':round(alp_deg,2),'beta':round(beta_deg,2)})
    else:
        form_in = FormInput()
        form_out = FormOutput()
        f_th2_dataJSON = None
        f_fbos_dataJSON = None
    return render(request, "rd_torque_app/rd_torque.html", {'form_input': form_in, 'form_output': form_out,
    'f_th2_data': f_th2_dataJSON, 'f_fbos_data': f_fbos_dataJSON})
