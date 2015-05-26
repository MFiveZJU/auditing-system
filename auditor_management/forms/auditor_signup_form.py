__author__ = 'stephen'

from django import forms
from auditor_management.validators import auditor_validator


class AuditorSignupForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(min_length=2, max_length=32)
    password = forms.CharField(min_length=6, max_length=16)
    password_confirm = forms.CharField(min_length=6, max_length=16)
    #
    phone = forms.CharField(validators=[auditor_validator.phone_validator])


class NameForm(forms.Form):
    email = forms.EmailField()
