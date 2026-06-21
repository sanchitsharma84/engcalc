from django import forms

class FormOutput(forms.Form):
    alp = forms.FloatField(label="Rated angle (deg)")  # rated angle in deg
    beta = forms.FloatField(label="Conrod angle (deg)")  # conrod angle in deg
    t = forms.FloatField(label="Torque (Nm)")  # torque in Nm