# Generated by Django 4.1.1 on 2022-11-30 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_about_user_profile_date_birth_profile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]