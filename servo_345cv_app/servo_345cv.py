
from .polynomial_345_cv import Polynomial_345_cv
import math

class Servo345cv:

	def __init__(self, s, t, pc_cv, d_pu, m, cof, f_res, j_pu, j_mot, j_gb, gr, t_idle):

		self.s = s  # stroke in mm
		self.t = t  # time for stroke in s
		self.pc_cv = pc_cv  # % (fraction) time fort constant velocity motion
		self.d_pu = d_pu  # pulley pcd in mm
		self.m = m  # moving mass in kg
		self.cof = cof  # coefficient of friction
		self.f_res = f_res  # any other resisting force opposing motion in N
		self.j_pu = j_pu  # pulley inertia in kgm2 (individual)
		self.j_mot = j_mot  # motor inertia in kgm2 (individual)
		self.j_gb = j_gb  # gearbox inertia in kgm2 at its input (individual)
		self.gr = gr  # gear ratio of gearbox
		self.t_idle = t_idle  # idle time after motion in s
		
		# declaring all list
		self.n_pu_lst = []  # pulley rpm list
		self.n_mot_lst = []  # motor rpm list
		self.w_pu_lst = []  # pulley ang vel list
		self.alp_pu_lst = []  # pulley ang acc list
		self.alp_mot_lst = []  # motor ang acc list
		self.trq_mot_lst = []  # motor torque list. Units in Nm

		# clear all lists
		self.n_pu_lst.clear()
		self.n_mot_lst.clear()
		self.w_pu_lst.clear()
		self.alp_pu_lst.clear()
		self.alp_mot_lst.clear()
		self.trq_mot_lst.clear()

		# calculations
		self.j_t_mot = self.j_mot + self.j_gb + (self.j_pu / self.gr**2) + (self.m * (self.d_pu/2000)**2) / self.gr**2
		self.f_cof = self.m * 9.8 * self.cof
		self.f_res_tot = self.f_res + self.f_cof
		self.trq_res_tot_pu = self.f_res_tot * (self.d_pu/2000)
		self.trq_res_tot_mot = self.trq_res_tot_pu / self.gr

		# making object of 345 polynomial with constant velocity
		self.curveGen = Polynomial_345_cv(self.s, self.t, self.t_idle, self.pc_cv)

		# getting calculation answers from object methods
		self.T_ms = self.curveGen.timePeriod_fcn()
		self.t_lst = self.curveGen.t_lst_fcn()
		self.s_lst = self.curveGen.s_lst_fcn()
		self.v_lst = self.curveGen.v_lst_fcn()
		self.a_lst = self.curveGen.a_lst_fcn()
		self.v_avg = self.curveGen.v_avg_fcn()
		self.v_pk = self.curveGen.v_max_fcn()
		self.a_pk = self.curveGen.a_max_fcn()
		self.t_acc = self.curveGen.t1_fcn()
		self.t_cv = self.curveGen.t2_fcn()
		self.s_acc = self.curveGen.s1_fcn()
		self.s_cv = self.curveGen.s2_fcn()
		self.a_rms = self.curveGen.a_rms_fcn()


		# making list of pulley rpm and w from list of "linear velocity of belt"
		for x in range(self.T_ms + 1):
			self.n_pu_lst.append(60 * self.v_lst[x]/(math.pi * self.d_pu))
			self.w_pu_lst.append(2 * self.v_lst[x]/self.d_pu)

		# making list of motor rpm
		for x in range(self.T_ms + 1):
			self.n_mot_lst.append(self.gr * 60 * self.v_lst[x] / (math.pi * self.d_pu))

		# calculating average rpm of pulley
		self.n_pu_avg = 60 * self.v_avg/(math.pi * self.d_pu)

		# calculating peak rpm of pulley
		self.n_pu_pk = 60 * self.v_pk/(math.pi * self.d_pu)

		# making list of pulley alpha from list of "linear acceleration of belt"
		for x in range(self.T_ms + 1):
			self.alp_pu_lst.append(2 * self.a_lst[x]/(self.d_pu*0.001))  # a is m/s2 and dia in m
		
		# making list of motor alpha from list of "pulley alpha"
		for x in range(self.T_ms + 1):
			self.alp_mot_lst.append(self.alp_pu_lst[x] * self.gr)

		# making list of motor torque from list of "motor alpha", value of total inertia and resisting torque
		for x in range(self.T_ms + 1):
			self.trq_mot_lst.append(self.alp_mot_lst[x] * self.j_t_mot + self.trq_res_tot_mot)

		# getting peak torque of motor form list
		self.t_mot_pk = max(self.trq_mot_lst)  # max torque on motor in Nm

		# calculating average motor rpm from average pulley rpm
		self.n_mot_avg = self.n_pu_avg * self.gr

		# calculating peak motor rpm from peak pulley rpm
		self.n_mot_pk = self.n_pu_pk * self.gr

		# calculating rms torque on motor
		self.t_mot_rms = self.j_t_mot * self.gr * self.a_rms / ((self.d_pu*0.5)*0.001)  + self.trq_res_tot_mot

	def get_t_lst(self):
		return self.t_lst
	
	def get_s_lst(self):
		return self.s_lst
	
	def get_v_lst(self):
		return self.v_lst

	def get_a_lst(self):
		return self.a_lst

	def get_n_mot_lst(self):
		return self.n_mot_lst

	def get_trq_mot_lst(self):
		return self.trq_mot_lst



	def get_t_mot_rms(self):
		return self.t_mot_rms
	
	def get_t_mot_pk(self):
		return self.t_mot_pk

	def get_n_mot_avg(self):
		return self.n_mot_avg

	def get_n_mot_pk(self):
		return self.n_mot_pk

	def get_a_pk(self):
		return self.a_pk

	def get_v_pk(self):
		return self.v_pk

	def get_t_acc(self):
		return self.t_acc

	def get_t_cv(self):
		return self.t_cv

	def get_s_acc(self):
		return self.s_acc

	def get_s_cv(self):
		return self.s_cv