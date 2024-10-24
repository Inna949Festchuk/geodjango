# Generated by Django 5.0 on 2023-12-23 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0019_rename_positinline_pointinline'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldpoint',
            name='myline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mypoints', to='geoapp.worldline'),
        ),
        migrations.DeleteModel(
            name='PointInLine',
        ),
    ]
