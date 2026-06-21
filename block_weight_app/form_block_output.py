from django import forms

class FormOutput(forms.Form):
    m_b = forms.FloatField(label="Block mass (kg)", required=False)
    ix_b = forms.FloatField(label="Block inertia xx (kgm2)", required=False)
    iy_b = forms.FloatField(label="Block inertia yy (kgm2)", required=False)
    iz_b = forms.FloatField(label="Block inertia zz (kgm2)", required=False)

    m_c = forms.FloatField(label="Cylinder mass (kg)", required=False)
    ix_c = forms.FloatField(label="Cylinder inertia xx (kgm2)", required=False)
    iy_c = forms.FloatField(label="Cylinder inertia yy (kgm2)", required=False)
    iz_c = forms.FloatField(label="Cylinder inertia zz (kgm2)", required=False)