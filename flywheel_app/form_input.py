from django import forms

class FormInput(forms.Form):

    pcd_fw = forms.FloatField(label="Flywheel pcd (mm)")  # flywheel pcd in mm
    pcd_pu = forms.FloatField(label="Pulley pcd (mm)")  # pulley pcd in mm
    gr_press = forms.FloatField(label="Gear ratio")  # press gear ratio
    pow_mot = forms.FloatField(label="Motor power (kW)")  # motor power in kW
    n_mot_rtd = forms.FloatField(label="Motor rated rpm")  # rated rpm of motor
    j_mot = forms.FloatField(label="Motor inertia (kgm2)")  # motor inertia in kgm2
    j_fw = forms.FloatField(label="Flywheel inertia (kgm2)")  # flywheel inertia in kgm2
    th_form = forms.FloatField(label="Forming angle (deg)")  # angle of forming in deg
    spm_min = forms.IntegerField(label="Min spm of press")  # min spm
    spm_max = forms.IntegerField(label="Max spm of press")  # max spm
    dw_pc = forms.FloatField(label="Percentage (fraction) speed reduction allowed")  # system efficiency
    eff = forms.FloatField(label="System efficiency (fraction)")  # system efficiency
    sspm1 = forms.IntegerField(label="sspm 1")  # sspm 1
    sspm2 = forms.IntegerField(label="sspm 2")  # sspm2
    trq_ds = forms.FloatField(label="Driveshaft torque approx. (Nm)")  # driveshaft's design torque in Nm
    energy_limit = forms.FloatField(label="Max allowable energy (kJ)")  # user defined limit of energy deliever capacity