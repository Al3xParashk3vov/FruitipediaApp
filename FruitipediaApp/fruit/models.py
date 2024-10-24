from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruit.validators import only_letters_validator
from FruitipediaApp.appprofile.models import Profile


class Fruit(models.Model):
    fruit_name = models.CharField(
        blank=False,
        max_length=30,
        validators=[
            only_letters_validator,
            MinLengthValidator(2),
        ],
        error_messages={
          'unique': 'This fruit name is already in use! Try a new one.'
        },
    )
    image_url = models.URLField(
        blank=False,
    )
    description = models.TextField(
        blank=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        to ='appprofile.Profile',
        on_delete=models.CASCADE,
        related_name='fruits',
    )