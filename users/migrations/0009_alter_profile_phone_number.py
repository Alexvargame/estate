# Generated by Django 4.1.1 on 2022-12-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default=['', '', '', '', '', '', '', '', '', ''], max_length=500),
        ),
    ]
