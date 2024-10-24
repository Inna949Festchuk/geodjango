# Generated by Django 5.0 on 2024-06-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0046_alter_importtrekline_azimuth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importtrekline',
            name='azimuth',
            field=models.CharField(blank=True, default=' - ', max_length=250, verbose_name='Значение азимута магнитного'),
        ),
        migrations.AlterField(
            model_name='importtrekline',
            name='distance',
            field=models.CharField(blank=True, default=' - ', max_length=250, verbose_name='Значение расстояния в пар-шагах'),
        ),
    ]
