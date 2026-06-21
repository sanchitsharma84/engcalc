from django import forms

class FormInConst(forms.Form):
    DEN = forms.FloatField(label = 'Density', required=False, initial=0.00000785, widget=forms.TextInput(attrs={\
        'style': 'text-align: center;', 'placeholder': 'density'}))