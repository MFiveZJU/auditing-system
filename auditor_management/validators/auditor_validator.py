__author__ = 'stephen'

from django.core.exceptions import ValidationError


def phone_validator(phone_number):
    if len(phone_number) != 11:
        raise ValidationError('Phone number should be 11-digit.')
    for char in phone_number:
        if char < '0' or char > '9':
            raise ValidationError('Phone number should only contain digits.')
