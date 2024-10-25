from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from FruitipediaApp.appprofile.forms import ProfileCreateForm
from FruitipediaApp.fruit.models import Fruit
from FruitipediaApp.utils import get_profile, get_all_fruits


def index(request):
    fruits = get_all_fruits()
    profile = get_profile()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'index.html', context)

def dashboard(request):
    profile = get_profile()
    fruits = get_all_fruits()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context)