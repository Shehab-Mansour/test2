from django.shortcuts import render,redirect

from doctor.views import *
from doctor.urls import *



def getuser(request,return1,return2):
    user_data = request.session.get('user', None)
    if user_data:
        data = {
            'username': user_data['username'],
            'email': user_data['email'],
            'id': user_data['id'],
            'photo': user_data['photo'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'address': user_data['address'],
            'city': user_data['city'],
            'state': user_data['state'],
            'phone': user_data['phone'],
            'year': user_data['year'],
            'age': user_data['age'],
        }
        return render(request,return1, data)
    else:
        return redirect(return2)

def getalluser(request,return1,return2):
    user_data = request.session.get('user', None)
    if user_data:
        data = {
            'username': user_data['username'],
            'email': user_data['email'],
            'id': user_data['id'],
            'photo': user_data['photo'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'address': user_data['address'],
            'city': user_data['city'],
            'state': user_data['state'],
            'phone': user_data['phone'],
            'year': user_data['year'],
            'age': user_data['age'],
            'allusers':newuser.objects.all()
        }
        print(data)
        return render(request,return1, data)
    else:
        return redirect(return2)
