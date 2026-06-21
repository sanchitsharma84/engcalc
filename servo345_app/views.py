from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required
import math
from .servo_345 import Servo345
from json import dumps

@login_required
def servo345(request):
    
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():

            s = float(form_in.cleaned_data['s'])
            t = float(form_in.cleaned_data['t'])
            d_pu = float(form_in.cleaned_data['d_pu'])
            m = float(form_in.cleaned_data['m'])
            cof = float(form_in.cleaned_data['cof'])
            f_res = float(form_in.cleaned_data['f_res'])
            j_pu = float(form_in.cleaned_data['j_pu'])
            j_mot = float(form_in.cleaned_data['j_mot'])
            j_gb = float(form_in.cleaned_data['j_gb'])
            gr = float(form_in.cleaned_data['gr'])
            t_idle = float(form_in.cleaned_data['t_idle'])
            motor = form_in.cleaned_data['motor']
            # print(motor.motor_series)

            s345 = Servo345(s, t, d_pu, m, cof, f_res, j_pu, j_mot, j_gb, gr, t_idle)

            t_lst = s345.get_t_lst()

            s_lst = s345.get_s_lst()
            v_lst = s345.get_v_lst()
            a_lst = s345.get_a_lst()
            trq_mot_lst = s345.get_trq_mot_lst()  # list of motor torque
            n_mot_lst = s345.get_n_mot_lst()  # list of motor rpm

            t_mot_rms = s345.get_t_mot_rms()
            t_mot_pk = s345.get_t_mot_pk()
            n_mot_avg = s345.get_n_mot_avg()
            n_mot_pk = s345.get_n_mot_pk()
            a_pk = s345.get_a_pk()
            v_pk = s345.get_v_pk()

            # to arrange the x y data into json format
            s_time_lst_of_dic_lst = []
            v_time_lst_of_dic_lst = []
            a_time_lst_of_dic_lst = []
            trq_mot_time_lst_of_dic_lst = []
            mot_trq_n_lst_of_dic_lst = []

            for index in range(len(t_lst)):
                s_time_temp_dic = {"x": t_lst[index], "y":s_lst[index]}
                s_time_lst_of_dic_lst.append(s_time_temp_dic)

                v_time_temp_dic = {"x": t_lst[index], "y":v_lst[index]}
                v_time_lst_of_dic_lst.append(v_time_temp_dic)

                a_time_temp_dic = {"x": t_lst[index], "y":a_lst[index]}
                a_time_lst_of_dic_lst.append(a_time_temp_dic)

                trq_mot_time_temp_dic = {"x": t_lst[index], "y":trq_mot_lst[index]}
                trq_mot_time_lst_of_dic_lst.append(trq_mot_time_temp_dic)

                mot_trq_n_temp_dic = {"x": n_mot_lst[index], "y":trq_mot_lst[index]}
                mot_trq_n_lst_of_dic_lst.append(mot_trq_n_temp_dic)

            s_time_dic = {
                "xy_data":s_time_lst_of_dic_lst,
            }
            s_time_dataJSON = dumps(s_time_dic)
            

            v_time_dic = {
                "xy_data":v_time_lst_of_dic_lst,
            }
            v_time_dataJSON = dumps(v_time_dic)

            a_time_dic = {
                "xy_data":a_time_lst_of_dic_lst,
            }
            a_time_dataJSON = dumps(a_time_dic)

            trq_mot_time_dic = {
                "xy_data":trq_mot_time_lst_of_dic_lst,
            }
            trq_mot_time_dataJSON = dumps(trq_mot_time_dic)

            mot_trq_n_dic = {
                "xy_data":mot_trq_n_lst_of_dic_lst,
            }
            mot_trq_n_dataJSON = dumps(mot_trq_n_dic)

            # to make motor rated graph in positive direction
            mot_rtd_pos_dic = {
                "xy_data":[{"x": 0, "y":motor.torque_at_0_rpm}, {"x": motor.rated_rpm, "y":motor.rated_torque}, {"x": motor.max_rpm, "y":motor.torque_at_max_rpm},]
            }
            mot_rtd_pos_dataJSON = dumps(mot_rtd_pos_dic)

            # to make motor rated graph in negative direction
            mot_rtd_neg_dic = {
                "xy_data":[{"x": 0, "y": - motor.torque_at_0_rpm}, {"x": motor.rated_rpm, "y": - motor.rated_torque}, {"x": motor.max_rpm, "y": - motor.torque_at_max_rpm},]
            }
            mot_rtd_neg_dataJSON = dumps(mot_rtd_neg_dic)


            # to make motor peak graph in positive direction
            mot_max_pos_dic = {
                "xy_data":[{"x": 0, "y":motor.max_torque}, {"x": motor.rpm_at_max_torque, "y":motor.max_torque}, {"x": motor.max_rpm, "y":motor.torque_at_max_rpm},]
            }
            mot_max_pos_dataJSON = dumps(mot_max_pos_dic)

            # to make motor peak graph in negative direction
            mot_max_neg_dic = {
                "xy_data":[{"x": 0, "y": - motor.max_torque}, {"x": motor.rpm_at_max_torque, "y": - motor.max_torque}, {"x": motor.max_rpm, "y": - motor.torque_at_max_rpm},]
            }
            mot_max_neg_dataJSON = dumps(mot_max_neg_dic)

            # to make rms - avg rpm point of motor
            rms_avg_n_dic = {
                "xy_data":[{"x": n_mot_avg, "y": t_mot_rms},]
            }
            rms_avg_n_dataJSON = dumps(rms_avg_n_dic)


            form_out = FormOutput(initial={
                't_mot_rms': round(t_mot_rms,2),
                't_mot_pk': round(t_mot_pk,2),
                'n_mot_avg': round(n_mot_avg,0),
                'n_mot_pk': round(n_mot_pk,0),
                'a_pk': round(a_pk,1),
                'v_pk': round(v_pk,1),
                })
    else:
        form_in = FormInput()
        form_out = FormOutput()
        s_time_dataJSON = None
        v_time_dataJSON = None
        a_time_dataJSON = None
        trq_mot_time_dataJSON = None
        mot_trq_n_dataJSON = None
        mot_rtd_pos_dataJSON = None
        mot_max_pos_dataJSON = None
        mot_rtd_neg_dataJSON = None
        mot_max_neg_dataJSON = None
        rms_avg_n_dataJSON = None
    return render(request, "servo345_app/servo_345.html", 
        {
        'form_input': form_in,
        'form_output': form_out,
        's_time_data': s_time_dataJSON,
        'v_time_data': v_time_dataJSON,
        'a_time_data': a_time_dataJSON,
        'trq_mot_time_data': trq_mot_time_dataJSON,
        'mot_trq_n_data': mot_trq_n_dataJSON,
        'mot_rtd_pos_data': mot_rtd_pos_dataJSON,
        'mot_max_pos_data': mot_max_pos_dataJSON,
        'mot_rtd_neg_data': mot_rtd_neg_dataJSON,
        'mot_max_neg_data': mot_max_neg_dataJSON,
        'rms_avg_n_data': rms_avg_n_dataJSON,
        })
