from django.shortcuts import render
from project.models import *
def home(request):
  projects = Project.objects.all()
  projectImage = ProjectImage.objects.all()
  return render(request, 'home.html',{'projects':projects,'projectImage':projectImage})

def error_404(request, exception):
    data = {}
    return render(request, 'home/404.html', data)