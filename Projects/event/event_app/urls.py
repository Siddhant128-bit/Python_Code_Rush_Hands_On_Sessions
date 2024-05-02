from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('remember_event/',views.remember_event,name='remember_event'),
    path('all_event/',views.all_event,name='all_event'),

]
