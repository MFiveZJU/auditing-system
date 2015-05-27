__author__ = 'stephen'

from django import forms
from auditor_management.validators import auditor_validator


class AuditorSignupForm(forms.Form):
    # email1 = forms.EmailField()
    email2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    username = forms.CharField(min_length=2, max_length=32,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(min_length=6, max_length=16,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password_confirm = forms.CharField(min_length=6, max_length=16,
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', 'placeholder': 'Password Confirmed'}))
    #
    phone = forms.CharField(validators=[auditor_validator.phone_validator],
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))


class NameForm(forms.Form):
    email = forms.EmailField()
