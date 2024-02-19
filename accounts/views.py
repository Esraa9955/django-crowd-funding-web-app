from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from .forms import  ProfileForm
from .models import Activation
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import *





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
    return render(request,'projectdir/user_profile.html')


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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')  # Updated variable name
        password2 = request.POST.get('password2')  # Updated variable name
        
        if username and email and password1 and password2:  # Ensure all required keys are present
            if password1 == password2:  # Ensure passwords match
                user = User.objects.create_user(username=username, email=email, password=password1)
                activation = Activation.objects.create(user=user)
                subject = 'Activate your account'
                message = render_to_string('registration/activation_email.html', {
                    'user': user,
                    'domain': request.get_host(),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': str(activation.token),
                })
                user.email_user(subject, message)

                return render(request, 'registration/login.html')
            else:
                return HttpResponse('Passwords do not match.')
        else:
            
            return HttpResponse('Please provide all required information for registration.')
    else:
        return render(request, 'registration/register.html')
    
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist, UnicodeDecodeError):
        user = None
    
    activation = Activation.objects.filter(user=user, token=token).first()
    if user is not None and activation is not None and not activation.is_expired():
        user.is_active = True
        user.save()
        activation.delete()
        return render(request, 'registration/activation_success.html')
    else:
        return render(request, 'registration/activation_failure.html')
    
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








    



