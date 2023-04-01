# Generated by Django 4.1.1 on 2022-12-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0031_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
        migrations.AlterField(
            model_name='house',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], max_length=30),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
        migrations.AlterField(
            model_name='searchflat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], max_length=30),
        ),
        migrations.AlterField(
            model_name='searchflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=300),
        ),
        migrations.AlterField(
            model_name='searchhouse',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], default=('Салтовка', 'Салтовка'), max_length=30),
        ),
        migrations.AlterField(
            model_name='searchhouse',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=30),
        ),
        migrations.AlterField(
            model_name='searchsmartflat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], max_length=30),
        ),
        migrations.AlterField(
            model_name='searchsmartflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], default=('Гагарина,пр.', 'Гагарина,пр.'), max_length=30),
        ),
        migrations.AlterField(
            model_name='smartflat',
            name='district',
            field=models.CharField(blank=True, choices=[('Алексеевка', 'Алексеевка'), ('ГСВ', 'ГСВ'), ('Новые Дома', 'Новые Дома'), ('Салтовка', 'Салтовка')], max_length=30),
        ),
        migrations.AlterField(
            model_name='smartflat',
            name='street',
            field=models.CharField(blank=True, choices=[('Гагарина,пр.', 'Гагарина,пр.'), ('Героев Сталинграда,пр.', 'Героев Сталинграда,пр.'), ('Героев Труда,ул.', 'Героев Труда,ул.'), ('Науки,пр.', 'Науки,пр.'), ('Одесская, ул.', 'Одесская, ул.'), ('Омская,ул.', 'Омская,ул.'), ('Сумская,ул.', 'Сумская,ул.'), ('Харьковских Дивизий,ул.', 'Харьковских Дивизий,ул.')], max_length=30),
        ),
    ]
