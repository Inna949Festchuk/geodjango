# Generated by Django 5.0 on 2024-06-06 23:48

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0040_alter_importtrekline_azimuth_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tile',
        ),
        migrations.AlterField(
            model_name='importtrek',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28404),
        ),
        migrations.AlterField(
            model_name='importtrekline',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28404, verbose_name='Местонахождение маршрута'),
        ),
        migrations.AlterField(
            model_name='pointinline',
            name='mylines',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mypoints', to='geoapp.importtrekline'),
        ),
        migrations.AlterField(
            model_name='pointinline',
            name='mypoints',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylines', to='geoapp.importtrek'),
        ),
    ]
