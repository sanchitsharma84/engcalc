from django import forms
from servo345_app.models import SmallServoMotor
from django.forms import ModelChoiceField

class FormInput(forms.Form):
    s = forms.FloatField(label="Stroke (mm)")  # stroke in mm
    t = forms.FloatField(label="Time (s)")  # time for stroke in s
    pc_cv = forms.FloatField(label="fraction time for CV motion")  # % (fraction) time fort constant velocity motion
    d_pu = forms.FloatField(label="Pulley pcd (mm)")  # pulley pcd in mm
    m = forms.FloatField(label="Moving mass (kg)")  # moving mass in kg
    cof = forms.FloatField(label="Coefficent of friction")  # coefficient of friction
    f_res = forms.FloatField(label="Resisting force (N)")  # any other resisting force opposing motion in N
    j_pu = forms.FloatField(label="Pulley inertia (kgm2)")  # pulley inertia in kgm2 (individual)
    j_mot = forms.FloatField(label="Motor inertia (kgm2)")  # motor inertia in kgm2 (individual)
    j_gb = forms.FloatField(label="Gearbox inertia (kgm2)")  # gearbox inertia in kgm2 at its input (individual)
    gr = forms.FloatField(label="Gear ratio")  # gear ratio of gearbox
    t_idle = forms.FloatField(label="Idle time (s)")  # idle time after motion in s
    motor = forms.ModelChoiceField(queryset=SmallServoMotor.objects.all(), initial=0)

    
    class Meta:
        model = SmallServoMotor
        fields = [
                #'rated_torque','motor_model','shaft_height'
        ]