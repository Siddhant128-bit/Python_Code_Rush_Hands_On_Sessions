# events/urls.py
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.remember_event, name='remember_event'),
    path('all/', views.all_events, name='all_events'),
]
