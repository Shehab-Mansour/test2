from django.db import models
from datetime import datetime


def user_directory_path(instance, filename):
    year = datetime.now().strftime('%y')
    return 'photos/{0}/{1}/{2}'.format(year, instance.username, filename)

def get_short_year():
    return int(datetime.now().strftime('%y'))


class newuser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, default="first_name")
    last_name = models.CharField(max_length=50, default="last_name")
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default="address")
    # zip_code = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="city")
    state = models.CharField(max_length=50, default="state")
    phone = models.CharField(max_length=13, default="phone")
    year = models.IntegerField(default=get_short_year)
    photo = models.ImageField(upload_to=user_directory_path, default='photos/default/defaultimage.png')
    def __str__(self):
        return self.username



