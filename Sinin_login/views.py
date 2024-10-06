from django.shortcuts import render, redirect
from Al_Araak import urls
from doctor.views import homebage
from func.func import getuser
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from func import func
from django.shortcuts import render, get_object_or_404, redirect


def sininlogin(request):
    user_data = request.session.get('user', None)
    if user_data:
        return redirect('home')
    else:
        if request.method == 'POST':
            new_user = request.POST.get('user')
            if new_user:
                username = request.POST['user']
                password = request.POST['pass']
                user_exists_in_db = newuser.objects.using('default').filter(username=username,password=password).exists()
                if user_exists_in_db:
                    user = newuser.objects.using('default').get(username=username)
                    request.session['user'] = {
                        'username': user.username,
                        'email': user.email,
                        'id': user.id,
                        'photo': user.photo.url,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'address': user.address,
                        'city': user.city,
                        'state': user.state,
                        'age': user.age,
                        'phone': user.phone,
                        'year': user.year,
                    }
                    return redirect('home')
                else:
                    messages.error(request, 'Username or Password is incorrect')
                    return redirect('register')
            else:
                username = request.POST['new_user']
                password1 = request.POST['new_pass1']
                password2 = request.POST['new_pass2']

                if password1 == password2:
                    user = newuser.objects.create(username=username, password=password1)
                    user.email = ""
                    user.save()
                    messages.success(request, 'Your account has been created!')

                    user = newuser.objects.using('default').get(username=username)
                    request.session['user'] = {
                        'username': user.username,
                        'email': user.email,
                        'id': user.id,
                        'photo': user.photo.url,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'address': user.address,
                        'city': user.city,
                        'state': user.state,
                        'age': user.age,
                        'phone': user.phone,
                        'year': user.year,

                    }
                    return redirect('register')
                else:
                    messages.error(request, 'Passwords do not match!')
                    return redirect('register')

        return render(request, 'sinin_login/index.html')


def suinup(request):
        return render(request, 'sinin_login/index.html')

def home(request):
    return getuser(request, 'home/home.html', 'register')

def account_management(request):
    return getuser(request,'account_management/accuntManegmint.html','register')


def end_session_view(request):
    request.session.flush()
    return redirect('register')



def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(newuser, id=user_id)

        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.city = request.POST.get('city')
        user.state = request.POST.get('state')
        user.age = request.POST.get('age')

        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']

        user.save()

        return redirect('end_session')

    return redirect('management')


def password_change(request):
    user_data = request.session.get('user', None)
    if user_data:
        if request.method == 'POST':
            username=user_data['username']
            user = get_object_or_404(newuser, username=username)
            user_password = user.password
            currentPassword=request.POST.get('currentPassword')
            if currentPassword==user_password:
                newPassword=request.POST.get('newPassword')
                confirmPassword=request.POST.get('confirmPassword')
                if newPassword==confirmPassword:
                    user.password=newPassword
                    user.save()
                    return redirect('end_session')

    return redirect('management')

