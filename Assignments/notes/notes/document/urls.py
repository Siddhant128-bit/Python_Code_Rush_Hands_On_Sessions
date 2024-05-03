from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('custom_logout/', views.custom_logout, name='logout'),
    path('', views.editor, name='editor'),
    path('delete_note/<int:docid>/', views.delete_note, name='delete_note'),
]
