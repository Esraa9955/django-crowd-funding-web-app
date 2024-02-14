from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.


def myLogin(request):
    context={'form':authenticate()}
    return render(request,'registration/login.html',context)

@login_required()
def myProfile(request):
    return render(request,'registration/profile.html')


class RegistrationForm(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



   
