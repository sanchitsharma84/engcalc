
class Polynomial_345:

    def __init__(self, s, t, ti):
        self.s = s  # stroke in s
        self.t1_s = t  # motion time in s
        self.ti_s = ti  # idle time in s

        self.t1_ms = (int)(self.t1_s * 1000)  # motion time in  ms
        self.ti_ms = (int)(self.ti_s * 1000)  # idle time type in  ms

        # making list of time for motion segment
        self.t1_lst = []  # motion time list in ms
        timeFill = 0
        for x in range(self.t1_ms + 1):
            self.t1_lst.append(timeFill)
            timeFill += 1

        # making list of time for idle segment
        self.ti_lst = []  # time list for idle segment in ms
        tiFill = 0
        for x in range(self.ti_ms + 1):
            self.ti_lst.append(tiFill)
            tiFill += 1

        # % of time passed during motion
        tPercent_lst = []
        for x in range(self.t1_ms + 1):
            tPercent_lst.append((float)(self.t1_lst[x]/self.t1_ms))

        # stroke list in mm
        self.s_lst = []
        for x in range(self.t1_ms + 1):
            self.s_lst.append((float)
                                (self.s * (10 * (tPercent_lst[x])**3
                                 - 15 * (tPercent_lst[x])**4
                                  + 6 * (tPercent_lst[x])**5)))
        
        # velocity list in mm
        self.v1_lst = []
        for x in range(self.t1_ms + 1):
            self.v1_lst.append((float)
                                ((self.s/self.t1_s)
                                 * (30 * (tPercent_lst[x])**2
                                    - 60 * (tPercent_lst[x])**3
                                     + 30 * (tPercent_lst[x])**4)))

        # acc list in mm
        self.a1_lst = []
        for x in range(self.t1_ms + 1):
            self.a1_lst.append((float)
                                    (self.s/(self.t1_s**2)
                                     * (60 * (tPercent_lst[x])**1
                                        - 180 * (tPercent_lst[x])**2
                                         + 120 * (tPercent_lst[x])**3)) / 1000)

        # generating combined time list (motion time + idle time)
        self.t_lst = []  # time list in ms unit
        timeFill = 0
        for x in range(self.t1_ms + self.ti_ms + 1):
            self.t_lst.append(timeFill)
            timeFill += 1

        # list of dist covered during idle time
        self.si_lst = []
        for x in range(self.ti_ms + 1):
            self.si_lst.append(self.s)

        # list of velocity during idle time
        self.vi_lst = []
        for x in range(self.ti_ms + 1):
            self.vi_lst.append(0)

        # list of acc during idle time
        self.ai_lst = []
        for x in range(self.ti_ms + 1):
            self.ai_lst.append(0)

        # max velocity
        self.v_max = 1.875 * self.s / self.t1_s  # mm/s

        # avg velocity in motion segment
        self.v1_avg = self.s / self.t1_s  # mm/s

        # avg velocity in motion + idle segment
        self.v_avg = self.s / (self.t1_s + self.ti_s)  # mm/s

        # max acceleration
        self.a_max = (5.777 * self.s / self.t1_s**2)/1000  # m/s2

        # rms acceleration in motion segment
        self.a1_rms = (4.14 * self.s / self.t1_s**2)/1000  # m/s2

        # finding rms of acceleration considering idle time in full cycle
        self.a_rms = self.a1_rms * ((self.t1_ms) / (self.t1_ms + self.ti_ms))**0.5  # m/s2
        

        

        # generating combined list of stroke
        s1_last_cut_lst = self.s_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        self.s_lst = s1_last_cut_lst + self.si_lst

        # generating combined list of velocity
        v1_last_cut_lst = self.v1_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        self.v_lst = v1_last_cut_lst + self.vi_lst

        # generating combined list of acceleration a
        a1_last_cut_lst = self.a1_lst[:-1]  # remove last element from list to avoid duplicate with 1st element of next list
        self.a_lst = a1_last_cut_lst + self.ai_lst

        

        # generating combined time list
        self.t_lst = []  # time list in ms unit
        timeFill = 0
        for x in range(self.t1_ms + self.ti_ms + 1):
            self.t_lst.append(timeFill)
            timeFill += 1




    # return segment-wise list
    def t1_lst_fcn(self):
        return self.t1_lst  # returns motion time list in ms

    def s1_lst_fcn(self):
        return self.s_lst  # returns distance list in ms duting motion time

    def v1_lst_fcn(self):
        return self.v1_lst  # returns velocity list in mm/s duting motion time

    def a1_lst_fcn(self):
        return self.a1_lst  # returns acc list in m/s2 duting motion time

    # combined list
    def t_lst_fcn(self):
        return self.t_lst  # returns motion + idle time list in ms
    def s_lst_fcn(self):
        return self.s_lst  # returns distance list in ms duting motion + idle time
    def v_lst_fcn(self):
        return self.v_lst  # returns velocity list in mm/s duting motion + idle time
    def a_lst_fcn(self):
        return self.a_lst  # returns acc list in m/s2 duting motion + idle time

    # max & avg values
    def v_max_fcn(self):
        return self.v_max  # max velocity in mm/s
    def v_avg_fcn(self):
        return self.v_avg  # avg vel in mm/s during motion and idle time
    def a_max_fcn(self):
        return self.a_max  # max acc in m/s2
    def a1_rms_fcn(self):
        return self.a1_rms  # rms acc during motion in m/s2
    def a_rms_fcn(self):
        return self.a_rms  # rms acc during motion + idle time

    # individual values
    def t_fcn(self):
        return self.t1_ms + self.ti_ms  # total time of motion + idle in ms
