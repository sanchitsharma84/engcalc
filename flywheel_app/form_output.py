from django import forms

class FormOutput(forms.Form):

    n_mot_min = forms.FloatField(label="Min motor rpm")  # min rpm of motor
    n_mot_max = forms.FloatField(label="Max motor rpm")  # max rpm of motor
    npc_mot_min = forms.FloatField(label="Min motor speed percentage")  # min speed as a % of motor rated speed
    npc_mot_max = forms.FloatField(label="Max motor speed percentage")  # max speed as a % of motor rated speed
    v_belt = forms.FloatField(label="Belt linear velocity (m/s)")  # belt linear speed in m/s
    n_fw_max = forms.FloatField(label="Max rpm of flywheel")  # flywheel max speed
    spm_press_bas = forms.FloatField(label="Base spm of press")  # base spm of press
    energy_max_cap = forms.FloatField(label="Maximum energy limit (kJ)")  # max energy limit