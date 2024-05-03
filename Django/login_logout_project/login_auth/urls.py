# login_auth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),  # Add signup URL pattern
    path('', views.home_view, name='home'),  # Define URL pattern for home page
]