from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from project.models import *
from category.models import *
from django.shortcuts import get_object_or_404
def home(request):
  projects = Project.objects.all()
  category = Category.objects.all()
  projectImage = ProjectImage.objects.all()
  highest_rated_projects = Project.objects.annotate(avg_rating=models.Avg('projectrating__rating')).order_by('-avg_rating')[:5]
  latest_projects = Project.objects.all().order_by('-start_time')[:5]
  context = {
        'highest_rated_projects': highest_rated_projects,
        'projects':projects,
        'projectImage':projectImage,
        'latest_projects':latest_projects,
        'category':category
    }
  return render(request, 'home.html',context)

   
def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)

def Cate(request, id):

    cate = Category.objects.filter(id=id).values_list('name', flat=True).first()
    projects = Project.objects.filter(category=id)

    context = {
        'cate':cate,
        'projects': projects,
    }
    return render(request, 'search_results.html', context)
