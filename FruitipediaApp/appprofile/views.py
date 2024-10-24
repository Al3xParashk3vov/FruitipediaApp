from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from FruitipediaApp.utils import get_user_obj
from FruitipediaApp.appprofile.forms import ProfileCreateForm
from FruitipediaApp.appprofile.models import Profile


# class ProfileCreateView():
#     pass

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dash')

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data()
        context['profile'] = get_user_obj()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

