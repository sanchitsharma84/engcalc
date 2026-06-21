from django import forms

class FormInConst(forms.Form):
    DEN = forms.FloatField(label = 'Density (kg/m3)', required=False, initial=7850, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'density'}))