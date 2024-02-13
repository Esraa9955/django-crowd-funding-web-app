
from django.contrib import admin
from django.urls import path,include
from .settings import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('project/',include('project.urls'))
]+static(MEDIA_URL,document_root=MEDIA_ROOT)
