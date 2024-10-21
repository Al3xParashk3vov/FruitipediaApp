import re

from django.core.exceptions import ValidationError


def name_validator(value):
    if not re.match(r'[A-Za-z]', value):
        raise ValidationError('Your name must start with a letter!')

