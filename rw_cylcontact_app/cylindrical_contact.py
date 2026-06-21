import math

class CylindricalContact:
	"""
    A class for calculation of heartzian stress by cylindrical contact
    ...

    Attributes
    ----------


    Methods
    -------
    get_stress():
        Returns maximum stress in units given in input paremeters

    get_contact_width():
        Returns contact width in units given in input paremeters
    """
	def __init__(self, f, l, v1, v2, e1, e2, d1, d2):
		"""
        Parameters
        ----------
		f : float
        	contact force (any std unit system can be followed, eg Newton) 
        l : float
        	length of cylinders (any std length unit can be followed, eg mm) 
	    v1 : float
	        poissons ratio of sphere 1
	    v2 : float
	        poissons ratio of sphere 2
	    e1 : float
	        Youngs modulus of sphere 1 (force and distance unit must be same as used before, eg N/mm2) 
	    e2 : float
	        Youngs modulus of sphere 2 (unit same as used in e1, eg N/mm2) 
	    d1 : float
	        Diameter of sphere 1 (unit same as used in l, eg mm) 
	    d2 : float
	        Diameter of sphere 2 (unit same as used in d1, eg mm) 
		"""
		n1 = 2 * f * (1 - v1**2) / e1
		n2 = (1 - v2**2) / e2
		den = math.pi * l * (1 / d1 + 1 / d2)
		self.b = math.pow((n1 + n2) / den, 1/2)
		self.p = 2 * f / (l * math.pi * self.b)


	def get_stress(self):
		"""
		Returns
		-------
		float
		Returns maximum stress in units given in input paremeters
		"""
		return self.p

	def get_contact_width(self):
		"""
		Returns
		-------
		float
		Returns contact radius in units given in input paremeters
		"""
		return 2 * self.b

# program test
# cc = CylindricalContact(10000, 100, 0.3, 0.3, 210000, 210000, 50, 50)
# print("Contact radius: ", cc.get_contact_width())
# print("Contact stress: ", cc.get_stress())
