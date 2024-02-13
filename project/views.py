from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from decimal import Decimal


def projectslist(request):
    context = {'myprojectslist': Project.project_list()}  # from db
    return render(request, 'projectdir/projectlist.html', context)


def projectdetailes(request, proid):
    pro = Project.objects.get(id=proid)
    comments = pro.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        print("POST request received")
        print(request.POST)  # Print POST data for debugging
        if 'donation_amount' in request.POST:
            print("Donation form submitted")
            donation_amount = Decimal(request.POST.get('donation_amount', 0))
            print("Donation amount:", donation_amount)
            if donation_amount > 0:
                pro.donation_amount += donation_amount
                pro.save()
                print("Donation amount updated")
                return redirect(reverse("projects.list"))
        elif 'content' in request.POST:
            print("Comment form submitted")
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.project = pro
                new_comment.save()
                print("Comment saved")
                return redirect("projects.list")
            else:
                print("Comment form is not valid")
        else:
            print("Unknown form submitted")

    context = {'project': pro, 'images': pro.images.all(), 'comments': comments, 'comment_form': comment_form}
    return render(request, 'projectdir/projectdetailes.html', context)



def createproject(request):
    if request.method == 'POST':
        metaform = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if metaform.is_valid() and formset.is_valid():
            project = metaform.save()
            for form in formset:
                image = form.cleaned_data.get('image')
                if image:
                    ProjectImage.objects.create(project=project, image=image)
            return redirect(reverse("projects.list"))
    else:
        metaform = ProjectForm()
        formset = ImageFormSet()
    return render(request, 'projectdir/projectcreate.html', {'metaform':  metaform, 'formset': formset})
