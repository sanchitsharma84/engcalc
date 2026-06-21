from django import forms

class FormIn(forms.Form):
    stroke = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 20%; text-align: center;', 'placeholder': 'stroke'}))
    spm = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 20%; text-align: center;', 'placeholder': 'spm'}))
    ca = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 20%; text-align: center;', 'placeholder': 'ca'}))
    
    fbos = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 20%; text-align: center;', 'placeholder': 'fbos'}))
    velocity = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 20%; text-align: center;', 'placeholder': 'velocity'}))
    