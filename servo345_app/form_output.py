from django import forms

class FormOutput(forms.Form):
    t_mot_rms = forms.FloatField(label="Required RMS torque at motor (Nm)")  # motor rms torque in Nm
    t_mot_pk = forms.FloatField(label="Required peak torque at motor (Nm)")  # motor peak torque in Nm
    n_mot_avg = forms.FloatField(label="Required average rpm at motor")  # motor avg rpm
    n_mot_pk = forms.FloatField(label="Required max rpm at motor")  # motor peak rpm
    a_pk = forms.FloatField(label="Max linear acceleration (m/s2)")  # peak linear acceleration in m/s2
    v_pk = forms.FloatField(label="Max linear velocity (mm/s)")  # peak linear velocity in mm/s