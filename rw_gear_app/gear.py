import math
from .inv import getAlpha as inv


class GearGeometry():

    def __init__(self, mn, alpn, beta, z1, z2, x1, x2):
        self.mn = mn
        self.alpn = alpn
        self.beta = beta
        self.z1 = z1
        self.z2 = z2
        self.x1 = x1
        self.x2 = x2

        self.mt = self.mn / math.cos(self.beta)
        self.pcd1 = self.z1 * self.mt
        self.pcd2 = self.z2 * self.mt
        self.a0 = (self.pcd1 + self.pcd2) / 2

    def getMt(self):
        return self.mt

    def getPcd1(self):
        return self.pcd1

    def getPcd2(self):
        return self.pcd2

    #  Formulas for S0 gearing

    def getTipCirDia1_S0(self):
        return self.pcd1 + 2 * self.mn * (1 + self.x1)

    def getTipCirDia2_S0(self):
        return self.pcd2 + 2 * self.mn * (1 + self.x2)

    # Formula common to both S and S0 gearing

    def norToothThkOnPcd(self):
        return self.mn * (0.5 * math.pi + 2 * self.x1 * math.tan(self.alpn))

    def transToothThkOnPcd(self):
        return self.mt * (0.5 * math.pi + 2 * self.x1 * math.tan(self.alpn))

    def getRootCirDia1(self):
        return self.pcd1 - 2 * 1.25 * self.mn + 2 * self.x1 * self.mn

    def getRootCirDia2(self):
        return self.pcd2 - 2 * 1.25 * self.mn + 2 * self.x2 * self.mn

    #  Formulas for S gearing

    def getAlpt(self):
        return math.atan(math.tan(self.alpn)/math.cos(self.beta))

    def getAlptW(self):
        inv_alptw = ((2 * (self.x1 + self.x2) * math.tan(self.alpn) / (self.z1 + self.z2)) +
                     (math.tan(GearGeometry.getAlpt(self)) - GearGeometry.getAlpt(self)))
        return inv(inv_alptw)

    def getTipCirWotDia1_S(self):
        return self.pcd1 + 2 * self.mn + 2 * self.x1 * self.mn

    def getTipCirWotDia2_S(self):
        return self.pcd2 + 2 * self.mn + 2 * self.x2 * self.mn

    def getA_S(self):
        return self.a0 * math.cos(GearGeometry.getAlpt(self)) / math.cos(GearGeometry.getAlptW(self))

    def getTipCirWtDia1_S(self):
        return 2 * (GearGeometry.getA_S(self) + self.mn - self.x2 * self.mn) - self.pcd2

    def getTipCirWtDia2_S(self):
        return 2 * (GearGeometry.getA_S(self) + self.mn - self.x1 * self.mn) - self.pcd1

    def getYm(self):
        return self.a0 + (self.x1 + self.x2) * self.mn - GearGeometry.getA_S(self)

    def getTopClearance(self):
        return GearGeometry.getA_S(self) - (GearGeometry.getTipCirWtDia1_S(self) + GearGeometry.getRootCirDia2(self)) / 2

    def workCirDia1(self):
        return self.pcd1 * math.cos(GearGeometry.getAlpt(self)) / math.cos(GearGeometry.getAlptW(self))

    def workCirDia2(self):
        return self.pcd2 * math.cos(GearGeometry.getAlpt(self)) / math.cos(GearGeometry.getAlptW(self))

# def __init__(self, mn, alpn, beta, z1, z2, x1, x2):
"""
a = GearGeometry(10, 0.261799387799147, 0, 100, 20, 0, 0)
print("Transverse module")
print(a.getMt())
print("\n")
print("pcd1")
print(a.getPcd1())
print("\n")
print("pcd2")
print(a.getPcd2())
print("\n")
print("tip circle1")
print(a.getTipCirDia1_S0())
print("\n")
print("tip circle2")
print(a.getTipCirDia2_S0())
print("\n")
print("Normal tooth thickness on pcd")
print(a.norToothThkOnPcd())
print("\n")
print("Transverse tooth thickness on pcd")
print(a.transToothThkOnPcd())
print("\n")
print("Root circle dia1")
print(a.getRootCirDia1())
print("\n")
print("Root circle dia2")
print(a.getRootCirDia2())
print("\n")
print("Transverse pressure angle")
print(a.getAlpt())
print("\n")
print("Working pressure angle")
print(a.getAlptW())
print("\n")
print("Tip circle dia1 without topping")
print(a.getTipCirWotDia1_S())
print("\n")
print("Tip circle dia2 without topping")
print(a.getTipCirWotDia2_S())
print("\n")
print("Actual center distance")
print(a.getA_S())
print("\n")
print("Tip circle dia1 after topping")
print(a.getTipCirWtDia1_S())
print("\n")
print("Tip circle dia2 after topping")
print(a.getTipCirWtDia2_S())
print("\n")
print("Topping")
print(a.getYm())
print("\n")
print("Top clearance")
print(a.getTopClearance())
print("\n")
print("Working circle dia1")
print(a.workCirDia1())
print("\n")
print("Working circle dia2")
print(a.workCirDia2())
"""