# Generated by Django 4.2.16 on 2024-09-30 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sinin_login', '0002_newuser_age_alter_newuser_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='zip_code',
        ),
    ]
