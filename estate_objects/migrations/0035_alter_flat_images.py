# Generated by Django 4.1.1 on 2022-12-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0034_flat_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='images',
            field=models.ImageField(null=True, upload_to='flats/pics'),
        ),
    ]
