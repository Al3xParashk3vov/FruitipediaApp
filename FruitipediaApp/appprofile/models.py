from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.appprofile.validators import name_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        blank=False,
        validators=(
            MinLengthValidator(2),
            name_validator,
        )
    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        validators=(
            MinLengthValidator(1),
            name_validator,
        )
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        max_length=40,
    )
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ],
        help_text='*Password length requirements: 8 to 20 characters'

    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )