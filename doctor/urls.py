from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.homebage,name='doctorhome'),
    path('patients/',views.Patients,name='patients'),
]