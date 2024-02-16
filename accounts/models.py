from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    birthdate = models.DateField()
    country = models.CharField(max_length=20)
    facebook = models.URLField(max_length=200)