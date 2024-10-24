from django.urls import path

from FruitipediaApp.appprofile import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='profile_create'),
    # path('details/', views.index, name='index'),
    # path('delete/', views.index, name='index'),
]