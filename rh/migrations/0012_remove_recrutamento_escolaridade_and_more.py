# Generated by Django 5.0.6 on 2024-07-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0011_rename_categoria_funcionario_cnh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recrutamento',
            name='escolaridade',
        ),
        migrations.AddField(
            model_name='candidato',
            name='escolaridade',
            field=models.CharField(default=0.0004972650422675286, max_length=100),
            preserve_default=False,
        ),
    ]
