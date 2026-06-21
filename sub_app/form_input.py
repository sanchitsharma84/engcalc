from django import forms

class FormInput(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()