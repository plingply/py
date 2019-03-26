
from django.urls import path
from fapp.view import api

urlpatterns = [
    path('welcome', api.getlist), 
]