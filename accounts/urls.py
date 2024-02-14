from django.urls import path,include
from . import views
from .views import *
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/',views.myProfile,name='myProfile'),
    path('Register/',RegistrationForm.as_view(),name='RegistrationForm'),
     path('logout/', LogoutView.as_view(), name='logout'),

]