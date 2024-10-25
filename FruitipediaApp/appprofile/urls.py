from django.urls import path

from FruitipediaApp.appprofile import views

urlpatterns = [
    path('create/', views.create_profile, name='profile_create'),
    # path('details/', views.index, name='index'),
    # path('delete/', views.index, name='index'),
]