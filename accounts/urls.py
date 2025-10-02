# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # ← Import auth views
from . import views

urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]