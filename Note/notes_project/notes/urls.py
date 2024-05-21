# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_notes, name='add_notes'),
    path('view/', views.view_notes, name='view_notes'),
]
