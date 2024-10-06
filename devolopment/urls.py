
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.recent_images,name='test' ),
    path('upload_profile_picture',views.upload_profile_picture, name='upload_profile_picture'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

