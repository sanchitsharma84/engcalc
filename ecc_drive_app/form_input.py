from django import forms

class FormInput(forms.Form):
    a = forms.FloatField(label="Eccentricity (mm)")  # eccentricity in mm
    b = forms.FloatField(label="Conrod length (mm)")  # conrod length in mm
    th2 = forms.FloatField(label="Crank angle (deg)")  # ecc gear angle in deg
    n2 = forms.FloatField(label="SPM")  # ecc gear rpm