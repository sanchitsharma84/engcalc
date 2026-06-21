# power screw calculations
#  ref: https://roymech.org/Useful_Tables/Cams_Springs/Power_Screws_1.html
import math
# dm is mean screw dia in m
# w is load in N
# mus is cof of screw
# th is half thread angle in rad
# dmc is mean collar dia in m
# muc is cof for collar
def get_tr(dm, w, mus, l, th, dmc, muc):
    
    ans = 0
    if dm == 0 or l == 0:
        ans = 0
    else:
        alp = math.atan(l / (math.pi * dm))
        thn = math.atan(math.cos(alp) * math.tan(th))
        ans = 0.5 * dm * w * (mus + math.cos(thn) * math.tan(alp)) / (math.cos(thn) - mus * math.tan(alp)) + 0.5 * w * dmc * muc
    return ans  # in Nm

def get_tl(dm, w, mus, l, th, dmc, muc):
    
    ans = 0
    if dm == 0 or l == 0:
        ans = 0
    else:
        alp = math.atan(l / (math.pi * dm))
        thn = math.atan(math.cos(alp) * math.tan(th))
        ans = 0.5 * dm * w * (mus - math.cos(thn) * math.tan(alp)) / (math.cos(thn) + mus * math.tan(alp)) + 0.5 * w * dmc * muc
    return ans  # in Nm

def get_eff(dm, mus, l, th, dmc, muc):
    
    ans = 0
    if dm == 0 or l == 0:
        ans = 0
    else:
        alp = math.atan(l / (math.pi * dm))
        thn = math.atan(math.cos(alp) * math.tan(th))
        denominator = dm * (mus + math.cos(thn) * math.tan(alp)) / (math.cos(thn) - mus * math.tan(alp)) + dmc * muc
        numerator = dm * math.tan(alp)
        ans = numerator / denominator
    return ans
