import math


class EccentricDriveKinematics:
    def __init__(self, a, b, th2, n2):
        self.a = a  # eccentricity in mm
        self.b = b  # con rod length in mm
        self.th2 = th2  # ecc gear angle from TDC in deg
        self.th2_rad = th2 * math.pi/180  # ecc gear angle from TDC in rad
        self.n2 = n2  # ecc gear rpm
        self.w2 = 2 * math.pi * self.n2 / 60  # ecc gear angular velocity
        self.th3_rad = math.asin(self.a * math.sin(self.th2_rad) / self.b)  # con rod angle in rad
        self.th3_deg = self.th3_rad * 180 / math.pi  # con rod angle in deg
        self.d = self.b * math.cos(self.th3_rad) - self.a * math.cos(self.th2_rad)  # distance of slider from ecc gear center in mm
        self.fbos = self.a + self.b - self.d  # fbos in mm
        self.w3 = self.a * math.cos(self.th2_rad) * self.w2 / (self.b * math.cos(self.th3_rad))  # angular vel of conrod
        self.v = self.a * self.w2 * math.sin(self.th2_rad) - self.b * self.w3 * math.sin(self.th3_rad)  # slide vel in mm/s
        self.alp2 = 0

        self.th2_deg_lst = []
        self.fbos_lst = []
        self.v_lst = []
        self.acc_lst = []
        for x in range(360 + 1):
            this_th2_rad = x * math.pi/180
            self.th2_deg_lst.append(x)
            this_th3_rad = math.asin(self.a * math.sin(this_th2_rad) / self.b)
            this_fbos = self.a + self.b - (self.b * math.cos(this_th3_rad) - self.a * math.cos(this_th2_rad))
            self.fbos_lst.append(this_fbos)
            this_w3 = self.a * math.cos(this_th2_rad) * self.w2 / (self.b * math.cos(this_th3_rad))
            this_v = self.a * self.w2 * math.sin(this_th2_rad) - self.b * this_w3 * math.sin(this_th3_rad)
            self.v_lst.append(this_v)
            this_alp3 = (self.a * self.alp2 * math.cos(this_th2_rad) - self.a * self.w2**2 * math.sin(this_th2_rad) + self.b * this_w3**2 * math.sin(this_th3_rad)) / (self.b * math.cos(this_th3_rad))
            this_acc = (self.a * self.alp2 * math.sin(this_th2_rad) + self.a * self.w2**2 * math.cos(this_th2_rad) - self.b * this_alp3 * math.sin(this_th3_rad) - self.b * self.w3**2 * math.cos(this_th3_rad)) / 1000
            self.acc_lst.append(this_acc)
    
    def get_th3_deg(self):
        return self.th3_deg

    def get_fbos(self):
        return self.fbos

    def get_v(self):
        return self.v

    def get_th2_deg_lst(self):
        return self.th2_deg_lst

    def get_fbos_lst(self):
        return self.fbos_lst

    def get_v_lst(self):
        return self.v_lst

    def get_acc_lst(self):
        return self.acc_lst

