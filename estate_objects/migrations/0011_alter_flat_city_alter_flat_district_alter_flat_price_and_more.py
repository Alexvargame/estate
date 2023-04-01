# Generated by Django 4.1.1 on 2022-11-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0010_alter_flat_floor_alter_flat_floors_alter_flat_square'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='city',
            field=models.CharField(blank=True, choices=[('Харьков', 'Харьков'), ('Никополь', 'Никополь')], max_length=20),
        ),
        migrations.AlterField(
            model_name='flat',
            name='district',
            field=models.CharField(blank=True, choices=[('Северный', 'ГСВ'), ('Северный', 'Северный')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='street',
            field=models.CharField(blank=True, choices=[('пр. Гагарина', 'пр. Гагарина'), ('пер. Спокойный', 'пер. Спокойный')], max_length=30),
        ),
    ]