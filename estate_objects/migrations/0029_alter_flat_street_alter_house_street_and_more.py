# Generated by Django 4.1.1 on 2022-11-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0028_alter_district_name_alter_flat_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
        migrations.AlterField(
            model_name='searchflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=300),
        ),
        migrations.AlterField(
            model_name='searchhouse',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=30),
        ),
        migrations.AlterField(
            model_name='searchsmartflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=30),
        ),
        migrations.AlterField(
            model_name='smartflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Науки,пр.', 'Науки,пр.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
    ]
