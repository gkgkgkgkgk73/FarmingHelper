# Generated by Django 4.2 on 2024-10-01 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0003_farming_net_per_hour_alter_farming_blue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farming',
            name='net_per_hour',
        ),
    ]
