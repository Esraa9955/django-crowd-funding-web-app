from django.shortcuts import render
from project.models import *
from django.shortcuts import get_object_or_404
def home(request):
  projects = Project.objects.all()
  projectImage = ProjectImage.objects.all()
  highest_rated_projects = Project.objects.annotate(avg_rating=models.Avg('projectrating__rating')).order_by('-avg_rating')[:5]
  latest_projects = Project.objects.all().order_by('-start_time')[:5]
  context = {
        'highest_rated_projects': highest_rated_projects,
        'projects':projects,
        'projectImage':projectImage,
        'latest_projects':latest_projects
    }
  return render(request, 'home.html',context)

def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)