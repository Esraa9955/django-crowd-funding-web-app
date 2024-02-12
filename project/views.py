from django.shortcuts import render

# Create your views here.


def projectslist(request):
   
    return render(request, 'projectdir/projectlist.html')


def projectdetailes(request, proid):
    return render(request, 'projectdir/projectdetailes.html')


def createproject(request):
    return render(request, 'projectdir/projectcreate.html')