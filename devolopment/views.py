import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from Sinin_login.models import newuser
from .models import UserProfile
from django.core.files.base import ContentFile
import base64
from . import models

def user_directory_path(request):
    user_data = request.session.get('user')
    year =  user_data['year']
    username=user_data['username']
    return 'photos/{0}/{1}'.format(year,username)


# def recent_images(request):
#     photos= user_directory_path(request)
#     image_folder = os.path.join(settings.MEDIA_ROOT, photos)
#     images = os.listdir(image_folder)
#     images = [photos  for img in images if img.endswith(('jpg', 'png', 'jpeg'))]
#     context = {'images': images}
#     return render(request, 'test/test.html',context)

def recent_images(request):
    # الحصول على مسار مجلد الصور للمستخدم
    photos = user_directory_path(request)

    # المسار الكامل لمجلد الصور
    image_folder = os.path.join(settings.MEDIA_ROOT, photos)

    # الحصول على قائمة الصور في المجلد
    images = os.listdir(image_folder)

    # فلترة الصور مع تصحيح المسار باستخدام .replace()
    images = [os.path.join(photos, img).replace('\\', '/') for img in images if img.endswith(('jpg', 'png', 'jpeg'))]

    # تمرير الصور إلى القالب
    context = {'images': images}
    return render(request, 'test/test.html', context)

def upload_profile_picture(request):
    print("heloo")
    if request.method == 'POST':
        # استلام الصورة المقطوعة
        image_data = request.FILES.get('croppedImage')

        if image_data:
            # حفظ الصورة
            user_profile = newuser.photo
            user_profile.profile_picture.save(f'{request.user.username}.png', image_data)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)



def test (request):
    return render(request, 'test/test.html')