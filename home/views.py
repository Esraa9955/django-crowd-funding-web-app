from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from project.models import *
from category.models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
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

# def Search(request):
#     # if request.method == 'POST':
#         # metaform = ProjectForm(request.POST)
#         # cate = Category.objects.filter(id=id).values_list('name', flat=True).first()
#         # projects = Project.objects.filter(category=id)
#         proName=request.GET
#         projects = Project.objects.filter()

#         context = {
#             # 'cate':cate,
#             'projects': proName,
#         }
#         return render(request, 'search_results.html', context)
#     # else:
#     #     return "failed"
class Search(ListView):
    model = Project
    template_name = 'search_results.html'
    context_object_name = 'projects'

    def get_queryset(self):
        query = self.request.GET.get('proName')
        return Project.objects.filter(title__icontains=query)
