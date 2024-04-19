"""
URL configuration for notes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes_project.notes.views import add_note
from notes_project.notes.views import view_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    # Route, View function and Name to call when referring in templates
    path('view-notes/', view_notes, name='view_notes'),
    path('', add_note, name='add_note'),
]
