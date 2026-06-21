import math

def get_e(s, d, l):
    e = 0.999
    err = 0.0001
    s_this = get_s(e, d, l)
    
    while abs(s - s_this) >= err or e < 0:
        e = e - err
        s_this = get_s(e, d, l)
    
    return round(e, 3)


def get_s(e, d, l):
    n1 = (1 - e**2)
    n2 = (d / l)
    d1 = math.pi * e
    d2 = math.pi**2 * (1 - e**2)
    d3 = 16 * e**2
    s_this = n1**2 * n2**2 / (d1 * (d2 + d3)**0.5)
    return s_this


# for program testing
# d = 100
# l = 75
# s = 0.0159375

# ans = get_e(s, d, l)
# print(ans)