# Generated by Django 4.0.3 on 2024-06-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0071_alter_groups_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='result',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='groups',
            name='stop',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
