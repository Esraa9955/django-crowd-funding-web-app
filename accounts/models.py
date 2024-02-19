# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='accounts/images/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username
    
    

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'
    

class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    birthdate = models.DateField()
    country = models.CharField(max_length=20)
    facebook = models.URLField(max_length=200)