# Generated by Django 5.0 on 2023-12-29 10:21

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0026_alter_worldline_options_alter_worldpoint_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worldline',
            options={'verbose_name': 'Схема движеия по азимутам'},
        ),
        migrations.AlterModelOptions(
            name='worldpoint',
            options={'verbose_name': 'Схема расположения ориентиров'},
        ),
        migrations.AlterField(
            model_name='worldline',
            name='location',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=28404, verbose_name='Схема движения'),
        ),
        migrations.AlterField(
            model_name='worldpoint',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28404, verbose_name='Схема ориентиров'),
        ),
    ]
