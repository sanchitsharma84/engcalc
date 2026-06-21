from django import forms

class FormIn(forms.Form):
    d = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'dia mm'}))
    qty = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'qty'}))
    sb_all = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'sb_all MPa'}))
    l = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'len mm'}))
    
    b = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'width mm'}))
    h = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'height mm'}))
    ds = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'dep shft mm'}))
    dh = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'dep hub mm'}))
    trq = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Trq Nm'}))
    