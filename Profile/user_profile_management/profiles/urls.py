from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
]
