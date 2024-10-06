from django.shortcuts import render

from Sinin_login.models import newuser
from func.func import getuser, getalluser


# Create your views here.

def homebage(request):
    return getuser(request,'doctor/home/index.html','register')


def Patients(request):
    context = {
        'user':newuser.objects.all()
    }
    return getalluser(request,'doctor/home/Patients.html','register')