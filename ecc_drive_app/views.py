from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required
import math
from .ecc_drive_kinematics import EccentricDriveKinematics
from json import dumps

@login_required
def ecc_drive(request):
    
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():
            a = float(form_in.cleaned_data['a'])
            b = float(form_in.cleaned_data['b'])
            th2 = float(form_in.cleaned_data['th2'])
            n2 = float(form_in.cleaned_data['n2'])

            ed = EccentricDriveKinematics(a, b, th2, n2)
            th3 = ed.get_th3_deg()
            fbos = ed.get_fbos()
            v = ed.get_v()

            th2_lst = []
            fbos_lst = []
            th2_lst.clear()
            fbos_lst.clear()

            th2_lst = ed.get_th2_deg_lst()
            fbos_lst = ed.get_fbos_lst()
            v_lst = ed.get_v_lst()
            acc_lst = ed.get_acc_lst()

            # to arrange the x y data into json format
            fbos_th2_lst_of_dic_lst = []
            v_th2_lst_of_dic_lst = []
            acc_th2_lst_of_dic_lst = []
            for index in range(len(th2_lst)):
                fbos_th2_temp_dic = {"x": th2_lst[index], "y":fbos_lst[index]}
                fbos_th2_lst_of_dic_lst.append(fbos_th2_temp_dic)

                v_th2_temp_dic = {"x": th2_lst[index], "y":v_lst[index]}
                v_th2_lst_of_dic_lst.append(v_th2_temp_dic)

                acc_th2_temp_dic = {"x": th2_lst[index], "y":acc_lst[index]}
                acc_th2_lst_of_dic_lst.append(acc_th2_temp_dic)

            fbos_th2_dic = {
                "xy_data":fbos_th2_lst_of_dic_lst,
            }
            fbos_th2_dataJSON = dumps(fbos_th2_dic)

            v_th2_dic = {
                "xy_data":v_th2_lst_of_dic_lst,
            }
            v_th2_dataJSON = dumps(v_th2_dic)

            acc_th2_dic = {
                "xy_data":acc_th2_lst_of_dic_lst,
            }
            acc_th2_dataJSON = dumps(acc_th2_dic)


            form_out = FormOutput(initial={'th3':round(th3, 1),'fbos':round(fbos,2),'v':round(v,2)})
    else:
        form_in = FormInput()
        form_out = FormOutput()
        fbos_th2_dataJSON = None
        v_th2_dataJSON = None
        acc_th2_dataJSON = None
    return render(request, "ecc_drive_app/ecc_drive.html", {'form_input': form_in, 'form_output': form_out, 
    'fbos_th2_data': fbos_th2_dataJSON, 'v_th2_data': v_th2_dataJSON, 'acc_th2_data': acc_th2_dataJSON})