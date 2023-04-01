# Generated by Django 4.1.1 on 2022-12-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0032_alter_flat_district_alter_flat_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchflat',
            name='city',
            field=models.CharField(blank=True, choices=[('Харьков', 'Харьков'), ('Чугуев', 'Чугуев')], default=('Харьков', 'Харьков'), max_length=20),
        ),
        migrations.AlterField(
            model_name='searchflat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], default=('Салтовка', 'Салтовка'), max_length=30),
        ),
        migrations.AlterField(
            model_name='searchflat',
            name='types',
            field=models.CharField(choices=[('Квартира', 'Квартира')], default=('Квартира', 'Квартира'), max_length=10),
        ),
        migrations.AlterField(
            model_name='searchhouse',
            name='city',
            field=models.CharField(blank=True, choices=[('Харьков', 'Харьков'), ('Чугуев', 'Чугуев')], default=('Харьков', 'Харьков'), max_length=20),
        ),
        migrations.AlterField(
            model_name='searchsmartflat',
            name='city',
            field=models.CharField(blank=True, choices=[('Харьков', 'Харьков'), ('Чугуев', 'Чугуев')], default=('Харьков', 'Харьков'), max_length=20),
        ),
        migrations.AlterField(
            model_name='searchsmartflat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], default=('Салтовка', 'Салтовка'), max_length=30),
        ),
    ]
