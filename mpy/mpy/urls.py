
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fapp.url.api')), 
    path('', include('fapp.url.view')), 
]
