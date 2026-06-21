import math


class Link_Drive_Mechanism:
	def __init__(self, a, b, c, d, f, th2, tht, g, h, m, w2):  # th2, tht in rad, link lengths in mm, w in rad/s

		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.f = f
		self.th2 = th2
		self.tht = tht
		self.g = g
		self.h = h
		self.m = m
		self.w2 = w2

		self.k1 = d/a
		self.k2 = d/c
		self.k3 = (a**2 - b**2 + c**2 + d**2 + f**2)/(2 * a * c)
		self.k4 = f/c
		self.k5 = f/a

		self.A = math.cos(th2) + self.k1 + self.k3 + self.k2 * math.cos(th2) + self.k4 * math.sin(th2)
		self.B = -2 * math.sin(th2) - 2 * self.k5
		self.C = self.k3 + self.k2 * math.cos(th2) + self.k4 * math.sin(th2) - math.cos(th2) - self.k1

		self.th4 = 2 * math.atan((-self.B + math.pow(self.B**2 - 4 * self.A * self.C, 0.5)) / (2 * self.A))
		self.th3 = math.acos(c * math.cos(self.th4)/b - a * math.cos(th2) / b - d / b)
		self.th7 = self.th3 - (math.pi - tht)
		self.th8 = math.acos(a * math.cos(th2) / g - m * math.cos(self.th7) / g - h / g)
		self.k = - a * math.sin(th2) + m * math.sin(self.th7) + g * math.sin(self.th8)

		self.w4 = w2 * (a/c) * (math.sin(self.th3 - th2) / math.sin(self.th3 - self.th4))
		self.w3 = c * self.w4 * math.sin(self.th4) / (b * math.sin(self.th3)) - a * w2 * math.sin(th2) / (b * math.sin(self.th3))

		self.w7 = self.w3
		self.w8 = w2 * (a / g) * (math.sin(th2) / math.sin(self.th8)) - self.w7 * (m / g) * (math.sin(self.th7) / math.sin(self.th8)) 
		self.v_k = - a * w2 * math.cos(th2) + m * self.w7 * math.cos(self.th7) + g * self.w8 * math.cos(self.th8)


	def get_th4(self):
		'''returns th4 in rad'''
		return self.th4

	def get_th3(self):
		'''returns th3 in rad'''
		return self.th3

	def get_th7(self):
		'''returns th7 in rad'''
		return self.th7

	def get_th8(self):
		'''returns th8 in rad'''
		return self.th8

	def get_k(self):
		'''returns k in mm'''
		return self.k

	def get_w3(self):
		'''returns w3 in rad/s'''
		return self.w3

	def get_w4(self):
		'''returns w4 in rad/s'''
		return self.w4

	def get_w7(self):
		'''returns w7 in rad/s'''
		return self.w7

	def get_w8(self):
		'''returns w8 in rad/s'''
		return self.w8

	def get_vk(self):
		'''returns vk in mm/s'''
		return self.v_k

'''
ld = Link_Drive_Mechanism(260, 800, 900, 1175, 375, 4.5, 2.33923, 1175, 0, 1175, 3)
print("th4: ", 180 * ld.get_th4()/math.pi)  # in deg
print("th3: ", 180 * ld.get_th3()/math.pi)  # in deg
print("th7: ", 180 * ld.get_th7()/math.pi)  # in deg
print("th8: ", 180 * ld.get_th8()/math.pi)  # in deg
print("k: ", ld.get_k())  # in mm
print("w3: ", 60 * ld.get_w3() / (2 * math.pi))  # in rpm
print("w4: ", 60 * ld.get_w4() / (2 * math.pi))  # in rpm
print("w7: ", 60 * ld.get_w7() / (2 * math.pi))  # in rpm
print("w8: ", 60 * ld.get_w8() / (2 * math.pi))  # in rpm
print("vel_k: ", ld.get_vk())  # in mm/s
'''
