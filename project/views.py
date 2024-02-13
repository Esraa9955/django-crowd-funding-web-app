from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def projectslist(request):
    context = {'myprojectslist': Project.project_list()}  # from db
    return render(request, 'projectdir/projectlist.html',context)


def projectdetailes(request, proid):
    pro = Project.objects.get(id=proid)
    context = {'project': pro,
              'images': pro.images.all()
               }
    return render(request, 'projectdir/projectdetailes.html',context)


def createproject(request):
    if request.method == 'POST':
        metaform = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if  metaform.is_valid() and formset.is_valid():
            project =  metaform.save()
            for form in formset:
                image = form.cleaned_data.get('image')
                if image:
                    ProjectImage.objects.create(project=project, image=image)
            return redirect(reverse("projects.list"))
    else:
        metaform = ProjectForm()
        formset = ImageFormSet()
    return render(request, 'projectdir/projectcreate.html', {'metaform':  metaform, 'formset': formset})













