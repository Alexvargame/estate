# Generated by Django 4.1.1 on 2023-03-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0043_alter_flatimage_flat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatimage',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_image', to='estate_objects.flat'),
        ),
    ]