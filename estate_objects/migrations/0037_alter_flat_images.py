# Generated by Django 4.1.1 on 2022-12-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0036_alter_flat_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='images',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='flats/pics'),
        ),
    ]