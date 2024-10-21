import re

from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not re.match(r'^[A-Za-z]+$', value):
        raise ValidationError('Fruit name should contain only letters!')
