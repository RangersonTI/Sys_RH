# Generated by Django 5.0.6 on 2024-07-08 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0010_rename_data_nasicimento_funcionario_data_nascimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='categoria',
            new_name='cnh',
        ),
    ]
