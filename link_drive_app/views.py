from django.shortcuts import render
from .form_input import FormInput
from .form_output import FormOutput
from django.contrib.auth.decorators import login_required
import math
from .link_drive_mechanism import Link_Drive_Mechanism
from json import dumps


@login_required
def link_drive(request):

    
    
    if request.method == 'POST':
        form_in = FormInput(request.POST)
        
        if form_in.is_valid():
            a = float(form_in.cleaned_data['a'])
            b = float(form_in.cleaned_data['b'])
            c = float(form_in.cleaned_data['c'])
            d = float(form_in.cleaned_data['d'])
            f = float(form_in.cleaned_data['f'])
            th2 = float(form_in.cleaned_data['th2'])  # in rad
            tht = float(form_in.cleaned_data['tht'])  # in rad
            g = float(form_in.cleaned_data['g'])
            h = float(form_in.cleaned_data['h'])
            m = float(form_in.cleaned_data['m'])
            w2 = float(form_in.cleaned_data['w2'])
            pf = float(form_in.cleaned_data['pf'])  # press force in ton
            rd = float(form_in.cleaned_data['rd'])

            t_cyc_ms = int(1000 * (2 * math.pi/w2))  # cycle time in ms, converted to int

            t_cyc_ms_lst = []  # cycle time list in ms
            th2_deg_lst = []  # ecc gear angle list in deg
            k_lst = []  # slide distance from ecc center list in mm
            fbos_lst = []  # fbos list in mm
            v_lst = []  # slide velocity list in mm/s

            # making list of values for graph
            for t in range(t_cyc_ms + 1):
                t_cyc_ms_lst.append(t)
                this_th2_rad = w2 * (t * 0.001)
                this_th2_deg = 180 * this_th2_rad / math.pi
                th2_deg_lst.append(this_th2_deg)

                # making object of ld calculation class
                ld = Link_Drive_Mechanism(a, b, c, d, f, this_th2_rad, tht, g, h, m, w2)
                this_k = ld.get_k()  # get value of slide position in mm
                k_lst.append(ld.get_k())
                this_v = ld.get_vk()  # slide vel in mm/s
                v_lst.append(this_v)
            
            # getting min and max values in k_lst
            # k_lst is the list of distance between ecc center to slide
            max_k = max(k_lst)  # max distance of slide from ecc gear center in mm
            min_k = min(k_lst)  # min distance of slide from ecc gear center in mm
            stroke = max_k - min_k  # slide stroke in mm

            # getting tdc and bdc time
            t_tdc = k_lst.index(min_k)  # time in ms when slide is at TDC. time starts from 0 when ecc gear is at eng X axis
            t_bdc = k_lst.index(max_k)  # time in ms when slide is at BDC. time starts from 0 when ecc gear is at eng X axis

            # getting tdc and bdc angle
            th2_tdc_deg = th2_deg_lst[t_tdc]  # tdc angle in deg. angle is measured from eng X axis 
            th2_bdc_deg = th2_deg_lst[t_bdc]  # bdc angle in deg. angle is measured from eng X axis 

            # making list of fbos (in mm)
            for t in range(t_cyc_ms + 1):
                this_k = k_lst[t]
                fbos_lst.append(max_k - this_k)

            # making time list from TDC to BDC in ms
            t_tdc_to_bdc = []
            for x in range(t_tdc, t_bdc):
                t_tdc_to_bdc.append(x)
            
            # making CA angle, fbos & velocity list from TDC to BDC
            th2_tdc_to_bdc_lst = []
            v_tdc_to_bdc_lst = []
            fbos_tdc_to_bdc_lst = []
            for x in range(t_tdc, t_bdc):
                this_th2 = th2_deg_lst[x]
                th2_tdc_to_bdc_lst.append(this_th2)
                this_v = v_lst[x]
                v_tdc_to_bdc_lst.append(this_v)
                this_fbos = fbos_lst[x]
                fbos_tdc_to_bdc_lst.append(this_fbos)

            # finding the time at rated distance. time is 0 when ecc gear starts from enx X axis
            t_rd = 0  # let time at rated distance is 0
            fbos_prev_temp_1 = fbos_lst[t_tdc]
            for x in range(t_tdc, t_bdc):
                this_fbos = fbos_lst[x]
                if fbos_prev_temp_1 > rd and this_fbos < rd:
                    t_rd = x
                fbos_prev_temp_1 = fbos_lst[x]
            
            # finding crank angle at rated distance (in deg)
            th2_rd_deg = th2_deg_lst[t_rd]

            # finding slide vel at rated distance (in mm/s)
            v_rd = v_lst[t_rd]

            # finding the rated torque (based on slide velocity)
            trq_eg_rtd = (pf * 10000) * (v_rd / 1000) / w2  # in Nm

            # finding time at 40% of stroke (to show in graph)
            # 40% in such a way that it covers 40% of stroke from FBOS
            stroke_40_pct = 0.4 * stroke
            t_s_40_pct = 0  # let time at 40% stroke is 0
            fbos_prev_temp_2 = fbos_lst[t_tdc]
            for x in range(t_tdc, t_bdc):
                this_fbos = fbos_lst[x]
                if fbos_prev_temp_2 > stroke_40_pct and this_fbos < stroke_40_pct:
                    t_s_40_pct = x
                fbos_prev_temp_2 = fbos_lst[x]

            # finding crank angle at 40% stroke (40% fbos)
            th2_s_40_pct_deg = th2_deg_lst[t_s_40_pct]

            # making CA angle, fbos & velocity list in 40% stroke (40% fbos)
            fbos_s_40_pct_lst = []
            v_s_40_pct_lst = []
            th2_s_40_pct_lst = []
            for x in range(t_s_40_pct, t_bdc):
                this_v = v_lst[x]
                v_s_40_pct_lst.append(this_v)
                this_fbos = fbos_lst[x]
                fbos_s_40_pct_lst.append(this_fbos)
                this_th2 = th2_deg_lst[x]
                th2_s_40_pct_lst.append(this_th2)

            # making force curve in 40% of downstroke wrt crank angle
            pf_s_40_pct_lst = []
            for x in range(t_s_40_pct, t_bdc):
                this_v = v_lst[x]
                this_pf = (trq_eg_rtd * w2 / (this_v * 0.001))/10000 # ans in ton
                if this_pf > pf:
                    this_pf = pf
                pf_s_40_pct_lst.append(this_pf)
            

            # -------------------- making customer graphs. 0 deg is TDC --------------------
            # as cycle time is known, we will make a time array that contains value of time starting from TDC time
            # customer list and variables will contain 'cust' prefix

            t_cyc_ms_cust_lst = []
            th2_deg_cust_lst = []
            fbos_cust_lst = []
            v_cust_lst = []

            # making list of values for graph
            for t in range(t_tdc, t_cyc_ms + t_tdc):
                t_cyc_ms_cust_lst.append(t)
                this_th2_rad_cust = w2 * (t * 0.001)
                
                # making object of ld calculation class
                ld_cust = Link_Drive_Mechanism(a, b, c, d, f, this_th2_rad_cust, tht, g, h, m, w2)
                this_k_cust = ld_cust.get_k()  # get value of slide position from ecc gear center in mm
                fbos_cust_lst.append(max_k - this_k_cust)
                this_v_cust = ld_cust.get_vk()  # slide vel in mm/s
                v_cust_lst.append(this_v_cust)

                this_th2_deg_cust = 180 * this_th2_rad_cust / math.pi
                if this_th2_deg_cust < 90:
                    th2_deg_cust_lst.append(round(360 - (90 - this_th2_deg_cust)))
                else:
                    th2_deg_cust_lst.append(round(this_th2_deg_cust - 90))
            
            # making list of acceleration from delta method
            acc_cust_lst = []
            v_prev_temp = v_cust_lst[0]
            for x in v_cust_lst:
                if v_cust_lst.index(x) == 0: # ignoring 1st delta calculation to avoid discontinuity
                    continue
                this_acc = v_prev_temp - x # units in m/s2
                acc_cust_lst.append(this_acc)
                v_prev_temp = x
            
            acc_cust_lst.insert(0, acc_cust_lst[0])  # adding 0th element = 1st element to make list size same as th2 list to avoid plotting problem in graph

            # print(len(acc_cust_lst))
            # print(len(th2_deg_cust_lst))
            
            # getting point values at given angle th2 in input

            ld_pt = Link_Drive_Mechanism(a, b, c, d, f, th2, tht, g, h, m, w2)
            th3 = ld_pt.get_th3()
            th4 = ld_pt.get_th4()
            th7 = ld_pt.get_th7()
            th8 = ld_pt.get_th8()
            fbos = ld_pt.get_k()
            w3 = ld_pt.get_w3()
            w4 = ld_pt.get_w4()
            w7 = ld_pt.get_w7()
            w8 = ld_pt.get_w8()
            v = ld_pt.get_vk()

            # to arrange the x y data into json format
            fbos_th2_lst_of_dic_lst = []
            v_th2_lst_of_dic_lst = []
            v_th2_half_lst_of_dic_lst = []
            v_fbos_half_lst_of_dic_lst = []
            fbos_th2_half_lst_of_dic_lst = []
            pf_th2_lst_of_dic_lst = []
            pf_fbos_lst_of_dic_lst = []
            v_fbos_lst_of_dic_lst = []

            

            for index in range(t_cyc_ms + 1):
                fbos_th2_temp_dic = {"x": th2_deg_lst[index], "y":fbos_lst[index]}
                fbos_th2_lst_of_dic_lst.append(fbos_th2_temp_dic)

                v_th2_temp_dic = {"x": th2_deg_lst[index], "y":v_lst[index]}
                v_th2_lst_of_dic_lst.append(v_th2_temp_dic)

            for index in range(t_tdc, t_bdc):
                v_th2_half_temp_dic = {"x": th2_deg_lst[index], "y":v_lst[index]}
                v_th2_half_lst_of_dic_lst.append(v_th2_half_temp_dic)

                v_fbos_half_temp_dic = {"x": fbos_lst[index], "y":v_lst[index]}
                v_fbos_half_lst_of_dic_lst.append(v_fbos_half_temp_dic)

                fbos_th2_half_temp_dic = {"x": th2_deg_lst[index], "y":fbos_lst[index]}
                fbos_th2_half_lst_of_dic_lst.append(fbos_th2_half_temp_dic)
                

            for index in range(t_bdc - t_s_40_pct):
                pf_th2_temp_dic = {"x": th2_s_40_pct_lst[index], "y":pf_s_40_pct_lst[index]}
                pf_th2_lst_of_dic_lst.append(pf_th2_temp_dic)

                pf_fbos_temp_dic = {"x": fbos_s_40_pct_lst[index], "y":pf_s_40_pct_lst[index]}
                pf_fbos_lst_of_dic_lst.append(pf_fbos_temp_dic)

                v_fbos_temp_dic = {"x": fbos_s_40_pct_lst[index], "y":v_s_40_pct_lst[index]}
                v_fbos_lst_of_dic_lst.append(v_fbos_temp_dic)
                

            fbos_th2_dic = {
                "xy_data":fbos_th2_lst_of_dic_lst,
            }
            fbos_th2_dataJSON = dumps(fbos_th2_dic)

            v_th2_dic = {
                "xy_data":v_th2_lst_of_dic_lst,
            }
            v_th2_dataJSON = dumps(v_th2_dic)

            v_th2_half_dic = {
                "xy_data":v_th2_half_lst_of_dic_lst,
            }
            v_th2_half_dataJSON = dumps(v_th2_half_dic)

            v_fbos_half_dic = {
                "xy_data":v_fbos_half_lst_of_dic_lst,
            }
            v_fbos_half_dataJSON = dumps(v_fbos_half_dic)

            fbos_th2_half_dic = {
                "xy_data":fbos_th2_half_lst_of_dic_lst,
            }
            fbos_th2_half_dataJSON = dumps(fbos_th2_half_dic)

            pf_th2_dic = {
                "xy_data":pf_th2_lst_of_dic_lst,
            }
            pf_th2_dataJSON = dumps(pf_th2_dic)

            pf_fbos_dic = {
                "xy_data":pf_fbos_lst_of_dic_lst,
            }
            pf_fbos_dataJSON = dumps(pf_fbos_dic)

            v_fbos_dic = {
                "xy_data":v_fbos_lst_of_dic_lst,
            }
            v_fbos_dataJSON = dumps(v_fbos_dic)


            form_out = FormOutput(initial={
                'stroke':round(stroke, 2),
                'th2_tdc_deg':round(th2_tdc_deg, 1),
                'th2_bdc_deg':round(th2_bdc_deg, 1),
                'th3':round(th3, 1),
                'th4':round(th4, 1),
                'th7':round(th7, 1),
                'th8':round(th8, 1),
                'fbos':round(fbos,2),
                'w3':round(w3,2),
                'w4':round(w4,2),
                'w7':round(w7,2),
                'w8':round(w8,2),
                'v':round(v,1),
                'th2_rd_deg':round(th2_rd_deg,2),
                'trq_eg_rtd':round(trq_eg_rtd,0),
                })
    else:
        # form_in = FormInput()
        form_in = FormInput(initial={
                'a':234,
                'b':720,
                'c':810,
                'd':1057.5,
                'f':337.5,
                'th2':4.2,
                'tht':2.33874,
                'g':1057.5,
                'h':0,
                'm':1057.5,
                'w2':2.5,
                'pf':1250,
                'rd':13,
                })

        form_out = FormOutput()
        fbos_th2_dataJSON = None
        v_th2_dataJSON = None
        v_th2_half_dataJSON = None
        v_fbos_half_dataJSON = None
        fbos_th2_half_dataJSON = None
        pf_th2_dataJSON = None
        pf_fbos_dataJSON = None
        v_fbos_dataJSON = None
        th2_deg_cust_lst = None
        fbos_cust_lst = None
        v_cust_lst = None
        acc_cust_lst = None

    return render(request, "link_drive_app/link_drive.html", {
        'form_input': form_in,
        'form_output': form_out,
        'fbos_th2_data': fbos_th2_dataJSON,
        'v_th2_data': v_th2_dataJSON,
        'v_th2_half_data': v_th2_half_dataJSON,
        'v_fbos_half_data': v_fbos_half_dataJSON,
        'fbos_th2_half_data': fbos_th2_half_dataJSON,
        'pf_th2_data': pf_th2_dataJSON,
        'pf_fbos_data': pf_fbos_dataJSON,
        'v_fbos_data': v_fbos_dataJSON,
        'th2_deg_cust_lst':th2_deg_cust_lst,
        'fbos_cust_lst':fbos_cust_lst,
        'v_cust_lst':v_cust_lst,
        'acc_cust_lst':acc_cust_lst,
        })
