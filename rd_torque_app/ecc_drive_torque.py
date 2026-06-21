import math

class EccentricDriveTorque:
    def __init__(self, r, l, s, f):
        self.r = r  # eccentricity in mm
        self.l = l  # con rod length in mm
        self.s = s  # rated distance in mm
        self.f = f  # press force in ton
        self.c1 = self.r + self.l - self.s
        self.alp_rad = math.acos((self.r**2 + self.c1**2 -self.l**2)/(2*self.r*self.c1))
        self.alp_deg = self.alp_rad * 180 / math.pi
        self.beta_rad = math.acos((self.l**2 + self.c1**2 -self.r**2)/(2*self.l*self.c1))
        self.beta_deg = self.beta_rad * 180 / math.pi
        self.t = 10 * self.f * self.r * (math.sin(self.alp_rad) + math.cos(self.alp_rad)*math.tan(self.beta_rad))  # torque in Nm

        TH2_S_DEG = 110  # start crank angle in deg
        self.th2_deg_lst = []  # crank angle from tdc in deg
        self.f_lst = []  # press force in ton
        self.fbos_lst = []  # fbos in mm
        self.th2_deg_lst.clear()
        self.f_lst.clear()
        self.fbos_lst.clear()
        for x in range(TH2_S_DEG, 181):
            self.th2_deg_lst.append(x)
            this_th2_rad = x * math.pi / 180  # crank angle from tdc in rad
            this_alp_rad = math.pi - this_th2_rad  # crank angle from BDC
            this_beta_rad = math.asin(self.r * math.sin(this_th2_rad) / self.l)
            this_fbos = self.r + self.l - (self.l * math.cos(this_beta_rad) - self.r * math.cos(this_th2_rad))
            self.fbos_lst.append(this_fbos)
            try:
                this_f = self.t / (10 * self.r * (math.sin(this_alp_rad) + math.cos(this_alp_rad)*math.tan(this_beta_rad)))  # force in ton
            except ZeroDivisionError:
                this_f = self.f
            
            if this_f > self.f:
                this_f = self.f

            self.f_lst.append(this_f)
    
    def get_alp_rad(self):
        return self.alp_rad
    
    def get_alp_deg(self):
        return self.alp_deg

    def get_beta_rad(self):
        return self.beta_rad

    def get_beta_deg(self):
        return self.beta_deg

    def get_beta_rad(self):
        return self.beta_rad

    def get_torque(self):
        return self.t

    def get_th2_deg_lst(self):
        return self.th2_deg_lst

    def get_f_lst(self):
        return self.f_lst

    def get_fbos_lst(self):
        return self.fbos_lst

