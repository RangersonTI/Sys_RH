# Generated by Django 5.0.6 on 2024-06-03 23:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rh',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rh',
            name='idade',
            field=models.TextField(),
        ),
    ]
