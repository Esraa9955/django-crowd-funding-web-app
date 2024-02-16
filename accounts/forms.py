from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile
from .models import AdditionalInfo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     mobile_phone = forms.CharField(max_length=15, required=True)
#     profile_picture = forms.ImageField(required=False) 

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile_phone', 'profile_picture')

#     def clean_mobile_phone(self):
#         mobile_phone = self.cleaned_data.get('mobile_phone')
#         if not mobile_phone.startswith('+20') or not len(mobile_phone) == 13:
#             raise ValidationError("Enter a valid Egyptian phone number.")
#         return mobile_phone
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    mobile_phone = forms.CharField(max_length=15, required=True)
    profile_picture = forms.ImageField(required=False)  # Add this field for image upload

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile_phone', 'profile_picture')

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data.get('mobile_phone')
        if not mobile_phone.startswith('+20') or not len(mobile_phone) == 13:
            raise forms.ValidationError("Enter a valid Egyptian phone number.")
        return mobile_phone

class AdditionalInfoForm(forms.ModelForm):
     class Meta:
        model = AdditionalInfo
        fields = ['birthdate', 'country', 'facebook']
