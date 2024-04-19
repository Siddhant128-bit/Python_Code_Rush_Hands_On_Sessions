
from django.contrib import admin
from django.urls import path
from encrypt.enter_page.views import encrypt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',encrypt)  
]
