from django import forms

class UnitForm(forms.Form):
    convert_from = forms.CharField(label='convert from', max_length = 100, required = True)
    convert_to = forms.CharField(label='convert to', max_length = 100,required = True)
