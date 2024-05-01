from django.urls import path
from . import views

urlpatterns = [
    path('', views.remember_event, name='remember_event'),
    path('events/', views.all_events, name='all_events'),
]
