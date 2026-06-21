from django import forms

class FormOutput(forms.Form):
    stroke = forms.FloatField(label="stroke (mm)")
    th2_tdc_deg = forms.FloatField(label="Crank agle at TDC (deg)")
    th2_bdc_deg = forms.FloatField(label="Crank agle at BDC (deg)")
    th3 = forms.FloatField(label="Angle th3 (deg)")
    th4 = forms.FloatField(label="Angle th4 (deg)")
    th7 = forms.FloatField(label="Angle th7 (deg)")
    th8 = forms.FloatField(label="Angle th (deg)")
    fbos = forms.FloatField(label="FBOS (mm)")
    w3 = forms.FloatField(label="w3 (rad/s)")
    w4 = forms.FloatField(label="w4 (rad/s)")
    w7 = forms.FloatField(label="w7 (rad/s)")
    w8 = forms.FloatField(label="w8 (rad/s)")
    v = forms.FloatField(label="Slide velocity (mm/s)")
    th2_rd_deg = forms.FloatField(label="Crank angle at rated dist (deg)")
    trq_eg_rtd = forms.FloatField(label="Ecc gear torque (Nm)")