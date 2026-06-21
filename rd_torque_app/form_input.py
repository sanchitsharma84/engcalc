from django import forms

class FormInput(forms.Form):
    f = forms.FloatField(label="Force (ton)")  # force in ton
    r = forms.FloatField(label="Eccentricity (mm)")  # eccentricity in mm
    s = forms.FloatField(label="Rated distance (mm)")  # rated distance in mm
    l = forms.FloatField(label="Conrod length (mm)")  # conrod length in mm