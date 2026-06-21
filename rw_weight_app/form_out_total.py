from django import forms

class FormOutTotal(forms.Form):
    total = forms.FloatField(label = "Total", required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'text-align: center;'}))

        