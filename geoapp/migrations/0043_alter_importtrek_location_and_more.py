# Generated by Django 5.0 on 2024-06-07 00:57

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0042_alter_importtrek_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importtrek',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28427),
        ),
        migrations.AlterField(
            model_name='importtrekline',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28427, verbose_name='Местонахождение маршрута'),
        ),
    ]
