
from django.shortcuts import render

from FruitipediaApp.utils import get_profile


def add_furit(request):
    profile = get_profile(request)
    context = {

    }
    return render(request, 'fruit/create_fruit.html', context)