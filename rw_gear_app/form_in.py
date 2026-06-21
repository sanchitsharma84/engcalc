from django import forms

class FormIn(forms.Form):
    m = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'm'}))
    helix = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'helix'}))
    zp = forms.IntegerField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Zp'}))
    xp = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'xp'}))
    zg = forms.IntegerField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Zg'}))
    xg = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'xg'}))
    
    pcd_p = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'pcd_p'}))
    pcd_g = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'pcd_g'}))
    w_pcd_p = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'w_pcd_p'}))
    w_pcd_g = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'w_pcd_g'}))
    od_p = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'od_p'}))
    od_g = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'od_g'}))
    root_d_p = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'root_d_p'}))
    root_d_g = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'root_d_g'}))
    cd = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'cd'}))
    


# forms.ChoiceField(choices = SHAPE_CHOICE, initial='2',label=False)