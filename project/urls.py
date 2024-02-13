from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    
    path('list',views.projectslist,name='projects.list'),
    path('<int:proid>',views.projectdetailes,name="project.detailes"),
    path('create',views.createproject,name="project.create"),
    path('report/<int:proid>', views.report_project, name='projects.report'),
    path('thank-you-for-reporting/', views.thank_you_for_reporting, name='thank_you_for_reporting'),
]