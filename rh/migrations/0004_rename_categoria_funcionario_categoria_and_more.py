# Generated by Django 5.0.6 on 2024-07-03 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0003_funcionario_delete_rh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Estado_Civil',
            new_name='estado_civil',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
