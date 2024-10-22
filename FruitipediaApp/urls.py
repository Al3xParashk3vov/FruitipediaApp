from django.contrib import admin
from django.urls import path, include

from FruitipediaApp import fruit, appprofile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruit/', include('FruitipediaApp.fruit.urls')),
    path('profile/', include('FruitipediaApp.appprofile.urls')),
]

#4 : 45