from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.remember, name='create'),
    path('events/', views.view_all, name='events'),
]
