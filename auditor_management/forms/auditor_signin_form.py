__author__ = 'stephen'

from django import forms

class AuditorSigninForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(min_length=6, max_length=16,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password'}))
