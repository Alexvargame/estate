# Generated by Django 4.1.1 on 2022-11-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0024_alter_searchflat_street_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchflat',
            name='street_s',
        ),
    ]
