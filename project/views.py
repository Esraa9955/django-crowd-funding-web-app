from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectRating
from .forms import RatingForm
from django.db.models import Avg

def projectslist(request):
    context = {'myprojectslist': Project.project_list()}  # from db
    return render(request, 'projectdir/projectlist.html', context)


def projectdetailes(request, proid):
    pro = Project.objects.get(id=proid)
    comments = pro.comments.all()
    comment_form = CommentForm()
    reports = Report.objects.filter(project=pro)
    # Calculate average rating
    average_rating = ProjectRating.objects.filter(project=pro).aggregate(Avg('rating'))['rating__avg']
    
    
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
    context = {'project': pro, 'images': pro.images.all(), 'comments': comments, 'comment_form': comment_form,
               'reports': reports, 'report_form': ReportForm(), 'average_rating': average_rating}
    return render(request, 'projectdir/projectdetailes.html', context)

    # context = {'project': pro, 'images': pro.images.all(), 'comments': comments, 'comment_form': comment_form,'reports': reports, 'report_form': ReportForm()  }
    # return render(request, 'projectdir/projectdetailes.html', context)
      


@login_required()
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


def report_project(request, proid):
    project = Project.objects.get(id=proid)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            # Create a new report instance and save it
            report = Report(project=project, reason=reason)
            report.save()
            return redirect('thank_you_for_reporting')
    else:
        form = ReportForm()
    return render(request, 'projectdir/report_project.html', {'form': form, 'project': project})

def thank_you_for_reporting(request):
    return render(request, 'projectdir/thank_you_for_reporting.html')


def report_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        form = ReportCommentForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['comment_reason']
            report = ReportComment(comment=comment, comment_reason=reason)
            report.save()
            return redirect('thank_you_for_reporting')  # Redirect after successful report
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ReportCommentForm()
    return render(request, 'projectdir/report_comment.html', {'form': form, 'comment': comment})



def rate_project(request, project_id):
    project = Project.objects.get(id=project_id)
    user_rating = None
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            # Check if the user has already rated this project
            existing_rating = ProjectRating.objects.filter(user=request.user, project=project).first()
            if existing_rating:
                existing_rating.rating = rating_value
                existing_rating.save()
            else:
                ProjectRating.objects.create(user=request.user, project=project, rating=rating_value)
            return redirect(reverse("project.detailes", kwargs={'proid': project_id}))
    else:
        form = RatingForm()
        user_rating_instance = ProjectRating.objects.filter(user=request.user, project=project).first()
        if user_rating_instance:
            user_rating = user_rating_instance.rating

    return render(request, 'projectdir/rate_project.html', {'form': form, 'project': project, 'user_rating': user_rating})