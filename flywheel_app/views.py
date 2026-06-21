from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required
from .fwe import Fwe
import math
from json import dumps

@login_required
def flywheel(request):
    
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():

            pcd_fw = float(form_in.cleaned_data['pcd_fw'])  # flywheel pcd in mm
            pcd_pu = float(form_in.cleaned_data['pcd_pu'])  # pulley pcd in mm
            gr_press = float(form_in.cleaned_data['gr_press'])  # press gear ratio
            pow_mot = float(form_in.cleaned_data['pow_mot'])  # motor power in kW
            n_mot_rtd = float(form_in.cleaned_data['n_mot_rtd'])  # rated rpm of motor
            j_mot = float(form_in.cleaned_data['j_mot'])  # motor inertia in kgm2
            j_fw = float(form_in.cleaned_data['j_fw'])  # flywheel inertia in kgm2
            th_form = float(form_in.cleaned_data['th_form'])  # angle of forming in deg
            spm_min = int(form_in.cleaned_data['spm_min'])  # min spm
            spm_max = int(form_in.cleaned_data['spm_max'])  # max spm
            dw_pc = float(form_in.cleaned_data['dw_pc'])  # system efficiency
            eff = float(form_in.cleaned_data['eff'])  # system efficiency
            sspm1 = int(form_in.cleaned_data['sspm1'])  # sspm 1
            sspm2 = int(form_in.cleaned_data['sspm2'])  # sspm2
            trq_ds = float(form_in.cleaned_data['trq_ds'])  # driveshaft's design torque in Nm
            energy_limit = float(form_in.cleaned_data['energy_limit'])  # user defined limit of energy deliever capacity

            fw = Fwe(pcd_fw, pcd_pu, gr_press, pow_mot, n_mot_rtd, j_mot, j_fw, th_form, spm_min, spm_max, dw_pc, eff, sspm1, sspm2, trq_ds, energy_limit)

            # get individual values from object
            n_mot_min = fw.get_n_mot_min()
            n_mot_max = fw.get_n_mot_max()
            npc_mot_min = fw.get_npc_mot_min()
            npc_mot_max = fw.get_npc_mot_max()
            v_belt = fw.get_v_belt()
            n_fw_max = fw.get_n_fw_max()
            spm_press_bas = fw.get_spm_press_bas()
            energy_max_cap = fw.get_energy_max_cap()

            # get arrays from object
            
            spm_lst = fw.get_spm_lst()  # x axis for all other data

            energy_lst = fw.get_energy_lst()  # in continuous mode
            energy_sspm1_lst = fw.get_energy_sspm1_lst()  # in intermittent mode 1
            energy_sspm2_lst = fw.get_energy_sspm2_lst()  # in intermittent mode 2

            dw_pc_lst = fw.get_dw_pc_lst()  # % reduction in speed in continuous mode
            spm_cyc_min_lst = fw.get_spm_cyc_min_lst()  # min spm in cycle
            spm_cyc_max_lst = fw.get_spm_cyc_max_lst()  # max spm in cycle

            # to arrange the x y data into json format
            eng_lst_of_dic_lst = []
            dw_pc_lst_of_dic_lst = []

            min_spm_lst_of_dic_lst = []
            max_spm_lst_of_dic_lst = []

            eng1_lst_of_dic_lst = []
            eng2_lst_of_dic_lst = []

            # edited till here

            for index in range(len(spm_lst)):
                eng_temp_dic = {"x": spm_lst[index], "y":energy_lst[index]}
                eng_lst_of_dic_lst.append(eng_temp_dic)

                eng1_temp_dic = {"x": spm_lst[index], "y":energy_sspm1_lst[index]}
                eng1_lst_of_dic_lst.append(eng1_temp_dic)

                eng2_temp_dic = {"x": spm_lst[index], "y":energy_sspm2_lst[index]}
                eng2_lst_of_dic_lst.append(eng2_temp_dic)

                dw_pc_temp_dic = {"x": spm_lst[index], "y":dw_pc_lst[index]}
                dw_pc_lst_of_dic_lst.append(dw_pc_temp_dic)

                min_spm_temp_dic = {"x": spm_lst[index], "y":spm_cyc_min_lst[index]}
                min_spm_lst_of_dic_lst.append(min_spm_temp_dic)

                max_spm_temp_dic = {"x": spm_lst[index], "y":spm_cyc_max_lst[index]}
                max_spm_lst_of_dic_lst.append(max_spm_temp_dic)


            eng_dic = {"xy_data":eng_lst_of_dic_lst,}
            eng_dataJSON = dumps(eng_dic)

            eng1_dic = {"xy_data":eng1_lst_of_dic_lst,}
            eng1_dataJSON = dumps(eng1_dic)

            eng2_dic = {"xy_data":eng2_lst_of_dic_lst,}
            eng2_dataJSON = dumps(eng2_dic)

            dw_pc_dic = {"xy_data":dw_pc_lst_of_dic_lst,}
            dw_pc_dataJSON = dumps(dw_pc_dic)

            min_spm_dic = {"xy_data":min_spm_lst_of_dic_lst,}
            min_spm_dataJSON = dumps(min_spm_dic)

            max_spm_dic = {"xy_data":max_spm_lst_of_dic_lst,}
            max_spm_dataJSON = dumps(max_spm_dic)
            

            form_out = FormOutput(initial={
                'n_mot_min': round(n_mot_min,2),
                'n_mot_max': round(n_mot_max,2),
                'npc_mot_min': round(npc_mot_min,0),
                'npc_mot_max': round(npc_mot_max,0),
                'v_belt': round(v_belt,1),
                'n_fw_max': round(n_fw_max,1),
                'spm_press_bas': round(spm_press_bas,0),
                'energy_max_cap': round(energy_max_cap,0),
                })

    else:
        form_in = FormInput()
        form_out = FormOutput()
        eng_dataJSON = None
        eng1_dataJSON = None
        eng2_dataJSON = None
        dw_pc_dataJSON = None
        min_spm_dataJSON = None
        max_spm_dataJSON = None
    return render(request, "flywheel_app/flywheel.html", 
        {
        'form_input': form_in,
        'form_output': form_out,
        'eng_data': eng_dataJSON,
        'eng1_data': eng1_dataJSON,
        'eng2_data': eng2_dataJSON,
        'dw_pc_data': dw_pc_dataJSON,
        'min_spm_data': min_spm_dataJSON,
        'max_spm_data': max_spm_dataJSON,
        })
