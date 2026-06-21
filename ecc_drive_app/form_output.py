from django import forms

class FormOutput(forms.Form):
    th3 = forms.FloatField(label="Conrod angle (deg)")  # conrod angle in deg
    fbos = forms.FloatField(label="FBOS (mm)")  # fbos in mm
    v = forms.FloatField(label="Slide velocity (mm/s)")  # slide vel in mm/s