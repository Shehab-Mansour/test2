
# Create your models here.
from Sinin_login.models import *
from django.db import models




class UserProfile(models.Model):
    user = models.OneToOneField(newuser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='test/', null=True, blank=True)