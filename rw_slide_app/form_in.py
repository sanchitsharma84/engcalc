from django import forms

class FormIn(forms.Form):
    tfx = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'TF x mm'}))  # top flange x
    tfy = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'TF y mm'}))  # top flange y
    bfx = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'BF x mm'}))  # bottom flange x
    bfy = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'BF y mm'}))  # bottom flange y
    wx = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Web x mm'}))  # web x
    wy = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Web y mm'}))  # web y
    rtx = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'TR x mm'}))  # top reinforced plate x
    rty = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'TR y mm'}))  # top reinforced plate y
    rbx = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'BR x mm'}))  # bottom reinforced plate x
    rby = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'BR y mm'}))  # bottom reinforced plate y
    

    e = forms.FloatField(label = '', required=False, initial=210000, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'E MPa'}))  # Youngs modulus
    g = forms.FloatField(label = '', required=False, initial=80000, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'G MPa'}))  # Shear modulus
    
    pf = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'Force ton'}))  # press force
    lr = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'LR mm'}))  # LR size of Slide
    pc_l = forms.FloatField(label = '', required=False, initial=0.667,widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'pc_l'}))  # % distance under load 
    cd_sus = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'sus cd mm'}))  # distance bw suspension
    
    sec_a = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'area mm2'}))  # section area
    weight = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'weight kg'}))  # beam weight
    sb = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'sb MPa'}))  # bending stress
    ss = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'ss MPa'}))  # shear stress
    def_m = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'm def mm'}))  # deflection due to bending
    def_s = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 's def mm'}))  # deflection due to shear
    def_pm = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 100%; text-align: center;', 'placeholder': 'tot def mm/m'}))  # deflection due to shear + bending per meter
    