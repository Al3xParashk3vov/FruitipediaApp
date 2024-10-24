from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from FruitipediaApp.appprofile.forms import ProfileCreateForm
from FruitipediaApp.fruit.models import Fruit
from FruitipediaApp.utils import get_user_obj


def index(request):

    return render(request, 'index.html')

class DashboardView(ListView, ): #BaseFormView
    model = Fruit
    form_class = ProfileCreateForm
    success_url = reverse_lazy('dash')

    def get_context_date(self, *, object_list=None, **kwargs):
        context = super().get_context_date()
        context['profile'] = get_user_obj()
        return context

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['dashboard.html']

        return ['profile/create-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)