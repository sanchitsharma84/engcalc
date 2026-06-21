from django import forms

class FormIn(forms.Form):
    m = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'mn'}))
    h = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'hel deg'}))
    zp = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'zp'}))
    zg = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'zg'}))
    
    trq = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Pinion trq Nm'}))
    pcd_p = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'pcd_p mm'}))
    pcd_g = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'pcd_g mm'}))
    fw = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'fw mm'}))
    