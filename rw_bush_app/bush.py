import math
from. import e_cal

def hyd_dyn_bush(w, d, l, c, rpm, mu):
    # w is load in N
    # d is dia in m
    # l is bearing width in m
    # c is diameteral clearance in m
    # rpm is rpm
    # mu is dyn viscosity in Pa.s
    r = d / 2  # radius in m
    pl = w / (d * l)  # project load N/m2
    ns = rpm / 60  # rps
    omg = 2 * math.pi * rpm / 60  # ang vel
    s = (mu * ns / pl) * (r / c)**2  # sommerfeld no
    e = e_cal.get_e(s, d, l)  # ecc ratio
    phi = math.atan((math.pi * (1 - e**2)**0.5) / (4 * e))  # atitude ang in rad
    u = r * omg  # linear surface speed
    q = e * u * l * c  # flow in m3/s
    h_min = c * (1 - e)  # min film thk in m
    ans_dic = {
        'e': e,
        's': s,
        'phi': phi,
        'q': q,
        'h_min': h_min,
    }
    return ans_dic

