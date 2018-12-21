from django import forms

class HomeForm(forms.Form):
    Target = forms.CharField()

class HomeFormOptions(forms.Form):

    Options = forms.CharField()
