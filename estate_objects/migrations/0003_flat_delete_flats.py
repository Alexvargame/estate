# Generated by Django 4.1.1 on 2022-11-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_objects', '0002_remove_flats_id_object_alter_flats_author_object_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('street', models.CharField(blank=True, max_length=20)),
                ('num_house', models.IntegerField()),
                ('num_kor', models.CharField(blank=True, max_length=3)),
                ('district', models.CharField(blank=True, max_length=20)),
                ('price', models.FloatField()),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('text_info', models.TextField(blank=True, max_length=10)),
                ('author_object', models.CharField(blank=True, max_length=10)),
                ('rooms', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('square', models.FloatField()),
                ('plan', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Flats',
        ),
    ]
