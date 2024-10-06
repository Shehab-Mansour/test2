from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import auth_login, auth_logout

urlpatterns=[
    path('',views.sininlogin,name='register'),
    path('management',views.account_management,name='management'),
    path('home',views.home,name='home'),
    path('end_session/', views.end_session_view, name='end_session'),
    path('update_user', views.update_user, name='update_user'),
    path('password_change',views.password_change,name='password_change'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)