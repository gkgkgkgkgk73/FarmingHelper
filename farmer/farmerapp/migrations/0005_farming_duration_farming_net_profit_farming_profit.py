# Generated by Django 4.2 on 2024-10-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0004_remove_farming_net_per_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='farming',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='farming',
            name='net_profit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='farming',
            name='profit',
            field=models.FloatField(default=0),
        ),
    ]
