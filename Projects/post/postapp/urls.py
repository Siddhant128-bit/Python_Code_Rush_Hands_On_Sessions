from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/',views.post,name="post"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('logout/',views.logout_page,name="logout"),
    path('delete-post/<id>/',views.delete_post,name="delete_post"),
    path('update-post/<id>/',views.update_post,name="update_post"),
    path('login/',views.login_page,name="login_page"),
    path('register/',views.register_page,name="register_page"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)