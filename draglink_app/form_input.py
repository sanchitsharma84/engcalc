from django import forms

class FormInput(forms.Form):
    a = forms.FloatField(label="a (mm)")  # link length a in mm
    b = forms.FloatField(label="b (mm)")  # link length b in mm
    c = forms.FloatField(label="c (mm)")  # link length c in mm
    d = forms.FloatField(label="d (mm)")  # link length d in mm
    e = forms.FloatField(label="e (mm)")  # link length e in mm

    pf = forms.FloatField(label="pf (ton)")  # press force in ton
    rd = forms.FloatField(label="rd (mm)")  # rated dist in mm
    rpm = forms.FloatField(label="rpm")  # rpm
    f = forms.FloatField(label="f")  # eccentricity in mm
    g = forms.FloatField(label="g")  # conrod length g in mm
    h = forms.FloatField(label="h")  # slide offset in mm
    thd_offset_ccw_dir_add = forms.FloatField(label="offset angle (deg)")  # offset angle in deg CCW dir
    root_op = forms.IntegerField(label="root_op")  # root option
    solid_shaft_flag = forms.BooleanField(label="solid_shaft")  # solid shaft or hollow splined shaft

    
