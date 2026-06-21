import math

class SphericalContact:
	"""
    A class for calculation of heartzian stress by spherical contact
    ...

    Attributes
    ----------


    Methods
    -------
    get_stress():
        Returns maximum stress in units given in input paremeters

    get_contact_radius():
        Returns contact radius in units given in input paremeters
    """
	def __init__(self, f, v1, v2, e1, e2, d1, d2):
		"""
        Parameters
        ----------
		f : float
        	contact force (any std unit system can be followed, eg Newton) 
	    v1 : float
	        poissons ratio of sphere 1
	    v2 : float
	        poissons ratio of sphere 2
	    e1 : float
	        Youngs modulus of sphere 1 (force unit must be same as used before, 
	        distance unit can be any standard eg N/mm2) 
	    e2 : float
	        Youngs modulus of sphere 2 (unit same as used in e1, eg N/mm2) 
	    d1 : float
	        Diameter of sphere 1 (unit same as used in e1 and e2, eg mm) 
	    d2 : float
	        Diameter of sphere 2 (unit same as used in d1, eg mm) 
		"""
		n1 = 3 * f * (1 - v1**2) / e1
		n2 = (1 - v2**2) / e2
		den = 8 * (1 / d1 + 1 / d2)
		self.a = math.pow((n1 + n2) / den, 1/3)
		self.p = 3 * f / (2 * math.pi * self.a**2)


	def get_stress(self):
		"""
		Returns
		-------
		float
		Returns maximum stress in units given in input paremeters
		"""
		return self.p

	def get_contact_radius(self):
		"""
		Returns
		-------
		float
		Returns contact radius in units given in input paremeters
		"""
		return self.a

# program test
# sc = SphericalContact(10000, 0.3, 0.3, 210000, 210000, 50, 50)
# print("Contact radius: ", sc.get_contact_radius())
# print("Contact stress: ", sc.get_stress())
