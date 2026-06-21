from django import forms

class FormIn(forms.Form):
    force = forms.IntegerField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'force'}))
    stroke = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'stroke'}))
    rd = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'rd'}))
    
    torque = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'torque'}))
    alp_deg = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'CA'}))
    beta_deg = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 16.66%; text-align: center;', 'placeholder': 'CR'}))
    