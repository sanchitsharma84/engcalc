# import matplotlib.pyplot as plt


class Polynomial_345_cv:

    def __init__(self, s, t, ti, pc_cv):
        self.s = s  # distance or stroke in mm
        self.t_s = t  # motion time in s
        self.ti_s = ti  # idle time in s
        self.pc_cv = pc_cv # percentage of time for constant velocity travel

        self.t_ms = (int)(self.t_s * 1000)  # int data type in  ms
        self.ti_ms = (int)(self.ti_s * 1000)  # int data type in  ms
        
        '''
        self.t_lst = []  # time list in ms unit
        timeFill = 0
        for x in range(self.t_ms + 1):
            self.t_lst.append(timeFill)
            timeFill += 1
        '''

        # calculation of all 3 motion segments
        self.t2_ms = (int)(self.pc_cv * self.t_ms)  # time of constant velocity motion in ms
        self.t1_ms = (int)((self.t_ms - self.t2_ms) / 2)  # time of acc motion in  ms
        self.t3_ms = self.t1_ms  # time of dec motion in ms. but we will use t1 most of the time in calculations
        # print("t1",self.t1_ms)
        # print("t2",self.t2_ms)

        self.v_max = self.s/(self.t1_ms*0.001 + self.t2_ms*0.001)  # mex vel in cycle in mm/s

        self.s1 = 0.5 * self.v_max * self.t1_ms*0.001  # distance (in mm) covered in acc or dec zone
        self.s2 = self.v_max * self.t2_ms*0.001  # distance covered (in mm) in constant vel zone
        
        # making list of time for acc segment
        self.t1_lst = []  # time list for acc segment in ms
        t1Fill = 0
        for x in range(self.t1_ms + 1):
            self.t1_lst.append(t1Fill)
            t1Fill += 1

        # making list of time for const vel segment
        self.t2_lst = []  # time list for acc segment in ms
        t2Fill = 0
        for x in range(self.t2_ms + 1):
            self.t2_lst.append(t2Fill)
            t2Fill += 1

        # making list of time for idle segment
        self.ti_lst = []  # time list for acc segment in ms
        tiFill = 0
        for x in range(self.ti_ms + 1):
            self.ti_lst.append(tiFill)
            tiFill += 1





        # filling array of percentage time of acc motion
        # it is used in S curve equation
        t1Percent_lst = []
        for x in range(self.t1_ms + 1):
            t1Percent_lst.append((float)(x/self.t1_ms))

        # motion calculations for segment 1 and 3 - acc-dec segment
        # distance equation of standard 3-4-5 polynomial curve is used for Velocity profile of actual machine

        # calculation velocity profile of both acc and then decceleration segment
        # v1 is for acceleration segment, v3 is deceleration segment, vi is idle segment
        self.v1_lst = []
        for x in range(self.t1_ms + 1):
            self.v1_lst.append((self.v_max * (10 * (t1Percent_lst[x])**3
                                 - 15 * (t1Percent_lst[x])**4
                                  + 6 * (t1Percent_lst[x])**5)))

        self.v3_lst = []
        for x in range(self.t1_ms + 1):
            self.v3_lst.append(self.v_max - 
                                (self.v_max * (10 * (t1Percent_lst[x])**3
                                 - 15 * (t1Percent_lst[x])**4
                                  + 6 * (t1Percent_lst[x])**5)))

        self.vi_lst = []
        for x in range(self.ti_ms + 1):
            self.vi_lst.append(0)
        

        # calculation distance profile of both acc and then decceleration segment
        # s1 is for acceleration segment, s3 is deceleration segment, si is idle segment
        self.s1_lst = []
        for x in range(self.t1_ms + 1):
            self.s1_lst.append((self.v_max * (self.t1_ms*0.001) * (2.5 * (t1Percent_lst[x])**4
                                 - 3 * (t1Percent_lst[x])**5
                                  + 1 * (t1Percent_lst[x])**6)))

        self.s3_lst = []
        for x in range(self.t1_ms + 1):
            self.s3_lst.append(self.s1 + self.s2 + self.v_max * (x*0.001) -
                                (self.v_max * (self.t1_ms*0.001) * (2.5 * (t1Percent_lst[x])**4
                                 - 3 * (t1Percent_lst[x])**5
                                  + 1 * (t1Percent_lst[x])**6)))

        self.si_lst = []
        for x in range(self.ti_ms + 1):
            self.si_lst.append(self.s)


        # calculation acceleration profile of both acc and then decceleration segment
        # a1 is for acceleration segment, a3 is deceleration segment, ai is idle segment
        self.a1_lst = []  # acc is in m/s2
        for x in range(self.t1_ms + 1):
            self.a1_lst.append(((self.v_max / (self.t1_ms*0.001)) * (30 * (t1Percent_lst[x])**2
                                 - 60 * (t1Percent_lst[x])**3
                                  + 30 * (t1Percent_lst[x])**4)) / 1000)

        self.a3_lst = []  # acc is in m/s2
        for x in range(self.t1_ms + 1):
            self.a3_lst.append((-(self.v_max / (self.t1_ms*0.001)) * (30 * (t1Percent_lst[x])**2
                                 - 60 * (t1Percent_lst[x])**3
                                  + 30 * (t1Percent_lst[x])**4)) / 1000)

        self.ai_lst = []
        for x in range(self.ti_ms + 1):
            self.ai_lst.append(0)

        

        # motion calculations for segment 2 - const vel segment

        # calculation velocity profile - const vel segment
        self.v2_lst = []
        for x in range(self.t2_ms + 1):
            self.v2_lst.append(self.v_max)

        # calculation distance profile - const vel segment
        self.s2_lst = []
        for x in range(self.t2_ms + 1):
            self.s2_lst.append(self.s1 + self.v_max * (x * 0.001))

        # calculation acceleration profile - const vel segment
        self.a2_lst = []
        for x in range(self.t2_ms + 1):
            self.a2_lst.append(0)



        # max accceleration in segment 1 or 3
        self.a_max = 1.875 * (self.v_max / (self.t1_ms*0.001)) / 1000  # m/s2

        # finding rms of acceleration in segment 1 or 3
        self.a1_rms = (1.195 * (self.v_max / (self.t1_ms*0.001))) / 1000  # m/s2

        # finding rms of acceleration in combined 1 - 3 segment
        self.a_rms = self.a1_rms * ((self.t1_ms + self.t3_ms) /(self.t1_ms + self.t2_ms + self.t3_ms + self.ti_ms))**0.5  # m/s2

        # finding average velocity
        self.v_avg = self.s / (self.t_s + self.ti_s)  # mm/s


        # generating combined time list
        self.t_lst = []  # time list in ms unit
        timeFill = 0
        for x in range(self.t1_ms + self.t2_ms + self.t1_ms + self.ti_ms + 1):
            self.t_lst.append(timeFill)
            timeFill += 1

        # generating combined list of distance/stroke s
        s1_last_cut_lst = self.s1_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        s2_last_cut_lst = self.s2_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        s3_last_cut_lst = self.s3_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list

        self.s_lst = s1_last_cut_lst + s2_last_cut_lst + s3_last_cut_lst + self.si_lst

        # generating combined list of velocity v
        v1_last_cut_lst = self.v1_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        v2_last_cut_lst = self.v2_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        v3_last_cut_lst = self.v3_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        self.v_lst = v1_last_cut_lst + v2_last_cut_lst + v3_last_cut_lst + self.vi_lst

        # generating combined list of acceleration a
        a1_last_cut_lst = self.a1_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        a2_last_cut_lst = self.a2_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        a3_last_cut_lst = self.a3_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        self.a_lst = a1_last_cut_lst + a2_last_cut_lst + a3_last_cut_lst + self.ai_lst


    # segment - wise list
    def t1_lst_fcn(self):
        return self.t1_lst
    def t2_lst_fcn(self):
        return self.t2_lst

    def s1_lst_fcn(self):
        return self.s1_lst
    def s2_lst_fcn(self):
        return self.s2_lst
    def s3_lst_fcn(self):
        return self.s3_lst

    def v1_lst_fcn(self):
        return self.v1_lst
    def v3_lst_fcn(self):
        return self.v3_lst

    def a1_lst_fcn(self):
        return self.a1_lst
    def a3_lst_fcn(self):
        return self.a3_lst

    # combined list
    def t_lst_fcn(self):
        return self.t_lst
    def s_lst_fcn(self):
        return self.s_lst
    def v_lst_fcn(self):
        return self.v_lst
    def a_lst_fcn(self):
        return self.a_lst

    # max values
    def v_max_fcn(self):
        return self.v_max
    def v_avg_fcn(self):
        return self.v_avg
    def a_max_fcn(self):
        return self.a_max
    def a1_rms_fcn(self):
        return self.a1_rms
    def a_rms_fcn(self):
        return self.a_rms

    # individual values
    def timePeriod_fcn(self):
        return self.t1_ms + self.t2_ms + self.t3_ms + self.ti_ms

    def t1_fcn(self):
        return self.t1_ms

    def t2_fcn(self):
        return self.t2_ms

    def s1_fcn(self):
        return self.s1

    def s2_fcn(self):
        return self.s2
    



# ob1 = Polynomial_345_cv(200, 2.4, 0.2)
'''
xAxis_lst = ob1.t_fcn()
yAxis_lst = ob1.s_fcn()
plt.plot(xAxis_lst, yAxis_lst)
plt.show()
'''
# print(len(xAxis_lst))
# print(len(yAxis_lst))
'''
print("local rms", ob1.a1_rms_fcn())
print("total rms", ob1.a_rms_fcn())
print("peak vel", ob1.v_max_fcn())
'''
