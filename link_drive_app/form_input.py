from django import forms

class FormInput(forms.Form):
    a = forms.FloatField(label="a (mm)")  # link length a in mm
    b = forms.FloatField(label="b (mm)")  # link length b in mm
    c = forms.FloatField(label="c (mm)")  # link length c in mm
    d = forms.FloatField(label="d (mm)")  # link length d in mm
    f = forms.FloatField(label="f (mm)")  # link length f in mm
    th2 = forms.FloatField(label="crank angle th2(rad)")  # ecc gear angle at any moment in rad
    tht = forms.FloatField(label="Link angle tht (rad)")  # link angle in rad
    g = forms.FloatField(label="g (mm)")  # link length g in mm
    h = forms.FloatField(label="h (mm)")  # link length h in mm
    m = forms.FloatField(label="m (mm)")  # link length m in mm
    w2 = forms.FloatField(label="SPM")  # ecc gear speed in rad/s
    pf = forms.FloatField(label="Press force (ton)")  # press force in ton
    rd = forms.FloatField(label="Rated distance (mm)")  # rated dist in mm