
from django.urls import path
from fapp.view import views as fapp_views

urlpatterns = [
    path('', fapp_views.index), 
    path('welcome', fapp_views.welcome), 
]
