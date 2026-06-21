from django import forms

SHAPE_CHOICE=(
    ("P", "Plate"),
    ("R", "Round"),
)

class FormIn(forms.Form):
    thk = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;', 'placeholder': 'thk'}))
    l = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;', 'placeholder': 'length'}))
    w = forms.FloatField(label = '', required=False, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;', 'placeholder': 'width'}))
    # density = forms.FloatField(label = '', required=False, initial=7850, widget=forms.TextInput(attrs={\
    #     'style': 'width: 14.2857%; text-align: center;', 'placeholder': 'density'}))
    qty = forms.FloatField(label = '', required=False, initial=1, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;', 'placeholder': 'qty'}))
    shape = forms.ChoiceField(label = '', choices = SHAPE_CHOICE, initial='P', widget=forms.Select(attrs={\
        'style': 'width: 14.2857%; text-align: center;',}))
    
    ans_mass = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;'}))
    
    ans_inertia = forms.FloatField(label = '', required=False, disabled = True, widget=forms.TextInput(attrs={\
        'style': 'width: 14.2857%; text-align: center;'}))


# forms.ChoiceField(choices = SHAPE_CHOICE, initial='2',label=False)