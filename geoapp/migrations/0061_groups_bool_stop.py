# Generated by Django 4.0.3 on 2024-06-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0060_rename_groops_groups_rename_id_groop_groups_id_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='bool_stop',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
