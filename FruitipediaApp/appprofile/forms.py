from django import forms
from django.forms import PasswordInput

from FruitipediaApp.appprofile.models import Profile
from FruitipediaApp.mixins import PlaceholderMixin


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        widgets = {
            'password': PasswordInput,
        }

class ProfileCreateForm(ProfileBaseForm): #  PlaceholderMixin,
    pass