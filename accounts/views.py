from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
# Create your views here.



def myLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Check if the user exists
            username = form.cleaned_data.get('username')
            if not User.objects.filter(username=username).exists():
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'This account has been deleted.'})

            # If the user exists, proceed with login
            user = form.get_user()
            auth_login(request, user)
            return redirect('myProfile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required()
def myProfile(request):
    return render(request,'registration/profile.html')


class RegistrationForm(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# def activeEmail(request,user,to_email):
#     messages.success(request,(request, f'Dear <b>{user.username}</b>, please go to your email <b>{user.email}</b> to complete registration'))
                     

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myProfile')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



def delete_confirmation(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'registration/delete_confirmation.html', {'user': user})

def DeleteAccount(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('login')  
    else:
        return redirect('myProfile')
    
@login_required
def updateUser(request, user_id):
    userr=User.objects.get(id=user_id)
    context={'userr': userr}
    if (request.method == 'POST'):
        if (request.POST['username'] !=None) :
         User.objects.filter(id=user_id).update(username=request.POST['username'],
                                               first_name=request.POST['first_name'],
                                               last_name=request.POST['last_name'],
                                            #    mobile_phone=request.POST['mobile_phone'],
                                            #    password1=request.POST['password1'],
                                            #    password2=request.POST['password2'],
                                            #    profile_picture=request.POST['profile_picture'],
                                               )
        r=reverse('myProfile')
        return HttpResponseRedirect(r)
    else:
        context['msg'] = 'Kindly fill all fields'
    return render(request,'registration/update.html',context)
  


    
    


