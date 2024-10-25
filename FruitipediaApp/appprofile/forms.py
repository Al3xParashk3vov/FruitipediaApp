from django import forms
from django.forms import PasswordInput

from FruitipediaApp.appprofile.models import Profile
from FruitipediaApp.mixins import PlaceholderMixin


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        widgets = {
            'password': PasswordInput,
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'password': "*Password length requirements: 8 to 20 characters",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
