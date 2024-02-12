from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    
    path('list',views.projectslist,name='projects.list'),
    path('<int:proid>',views.projectdetailes,name="project.detailes"),
    path('create',views.createproject,name="project.create"),
]