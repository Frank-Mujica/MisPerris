# Generated by Django 2.1.2 on 2018-11-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0002_auto_20181105_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregaradoptante',
            name='telContacto',
            field=models.CharField(max_length=8),
        ),
    ]