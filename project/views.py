from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def projectslist(request):

    return render(request, 'projectdir/projectlist.html')


def projectdetailes(request, proid):
    return render(request, 'projectdir/projectdetailes.html')


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












'''
def create_campaign(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProjectImage.objects.none())
        if form.is_valid() and formset.is_valid():
            Pro = form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = ProjectImage(campaign=Pro, image=image)
                    photo.save()
            return redirect('campaign_created')  # Redirect to a success page
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=ProjectImage.objects.none())
    return render(request, 'campaign_create.html', {'form': form, 'formset': formset})
    '''
