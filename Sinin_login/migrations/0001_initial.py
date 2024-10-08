# Generated by Django 4.2.16 on 2024-09-26 22:45

import Sinin_login.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=13)),
                ('year', models.IntegerField(default=Sinin_login.models.get_short_year)),
                ('photo', models.ImageField(default='images/websiteicon.png', upload_to=Sinin_login.models.user_directory_path)),
            ],
        ),
    ]
