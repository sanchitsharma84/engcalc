from django import forms

class FormIn(forms.Form):
    pf = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Pf ton'}))  # Press force
    stk = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Stk mm'}))  # stroke
    rd = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'RD mm'}))  # rated dist
    spm = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'spm'}))  # spm
    ca = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'CA deg'}))    # crank angle deg
    
    
    teg = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Teg Nm'}))  # torque at eg
    fbos = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'fbos mm'}))  # fbos at ca
    vel = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'vel mm/s'}))  # slide vel at ca
    