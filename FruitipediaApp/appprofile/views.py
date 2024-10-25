from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from FruitipediaApp.utils import get_profile
from FruitipediaApp.appprofile.forms import ProfileCreateForm
from FruitipediaApp.appprofile.models import Profile


# class ProfileCreateView():
#     pass

def create_profile(request):
    profile = get_profile()
    form = ProfileCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'profile': profile,
        'form': form,

    }

    return render(request, 'profile/create-profile.html', context)

