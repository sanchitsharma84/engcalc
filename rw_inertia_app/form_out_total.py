from django import forms

class FormOutTotal(forms.Form):
    mass_total = forms.FloatField(label = "Total mass (kg)", required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;'}))
    inertia_total = forms.FloatField(label = "Total inertia (kgm2)", required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;'}))

        