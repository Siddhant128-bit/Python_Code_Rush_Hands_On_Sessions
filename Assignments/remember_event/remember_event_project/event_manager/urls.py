from django.urls import path
from event_manager import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('remember_event/',views.remember_event,name='remember_event'),
    path('all_events/',views.all_events,name='all_event'),
]
