from django.urls import path
from .views import base, index

# URLS AQUI

urlpatterns = [
    path('', base, name="base"),
    path('index/', index, name="index"),
]
