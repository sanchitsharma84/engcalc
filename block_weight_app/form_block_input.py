from django import forms

class FormInput(forms.Form):

    density = forms.FloatField(label="Density (kg/m3)", required=False, initial=7850)

    l_b = forms.FloatField(label="Length (x) (mm)", required=False)
    w_b = forms.FloatField(label="Width (y) (mm)", required=False)
    h_b = forms.FloatField(label="Height (z) (mm)", required=False)
    qty_b = forms.FloatField(label="Quantity", required=False, initial=1)

    od_c = forms.FloatField(label="OD (mm)", required=False)
    id_c = forms.FloatField(label="ID (mm)", required=False)
    l_c = forms.FloatField(label="Length (x) (mm)", required=False)
    qty_c = forms.FloatField(label="Quantity", required=False, initial=1)
