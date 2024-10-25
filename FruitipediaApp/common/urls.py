
from django.urls import path

from FruitipediaApp.common import views

urlpatterns=[
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dash'),
]
