# coffee/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.Home, name='home'),
    path('', views.index, name='index'), 
]

