from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages



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


# class RegistrationForm(CreateView):
#     form_class = RegistrationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('myProfile')  
#     else:
#         form = RegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            mobile_phone = form.cleaned_data.get('mobile')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('userImage')
    else:
        form = UserRegisterForm()
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
    
# @login_required
# def updateUser(request, user_id):
#     userr=User.objects.get(id=user_id)
#     context={'userr': userr}
#     if (request.method == 'POST'):
#         if (request.POST['username'] !=None) :
#          User.objects.filter(id=user_id).update(username=request.POST['username'],
#                                                first_name=request.POST['first_name'],
#                                                last_name=request.POST['last_name'],
#                                                password1=request.POST['password1'],
#                                                password2=request.POST['password2'],
#                                                image=request.POST['image'],
#                                                )
#         r=reverse('myProfile')
#         return HttpResponseRedirect(r)
#     else:
#         context['msg'] = 'Kindly fill all fields'
#     return render(request,'registration/update.html',context)



from django.shortcuts import render, redirect
from .forms import AdditionalForm

def additional_info(request):
    try:
        additional_info = request.user.additionalinfo
    except AdditionalInfo.DoesNotExist:
        additional_info = None
    
    if request.method == 'POST':
        form = AdditionalForm(request.POST, instance=additional_info)
        if form.is_valid():
            additional_info = form.save(commit=False)
            additional_info.user = request.user
            additional_info.save()
            messages.success(request, 'Additional information saved successfully.')
            return redirect('user_project')
    else:
        form = AdditionalForm(instance=additional_info)
    
    return render(request, 'registration/additional_info.html', {'form': form})

@login_required
def userImage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('projects.list')  # Assuming you have a URL named 'profile_detail' for profile detail view
    else:
        form = ProfileForm()
    return render(request, 'registration/userImage.html', {'form': form})



# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileEditForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('user_project')  
#     else:
#         form = ProfileEditForm(instance=request.user.profile)
#     return render(request, 'registration/edit_profile.html', {'form': form})


    # additional_info_instance = AdditionalInfo.objects.filter(user=request.user).first()

    # if request.method == 'POST':
    #     if additional_info_instance:  
    #         form = AdditionalInfoForm(request.POST, request.FILES, instance=additional_info_instance)
    #     else:  
    #         form = AdditionalInfoForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         additional_info = form.save(commit=False)
    #         additional_info.user = request.user
    #         additional_info.save()
    #         return redirect('myProfile')  
    # else:
    #     if additional_info_instance: 
    #         form = AdditionalInfoForm(instance=additional_info_instance)
    #     else: 
    #         form = AdditionalInfoForm()
    
    # return render(request, 'registration/additional_info.html', {'form': form})

   


    
    


