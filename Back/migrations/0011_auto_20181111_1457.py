# Generated by Django 2.1.2 on 2018-11-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0010_auto_20181111_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imgMascota',
            field=models.ImageField(upload_to=''),
        ),
    ]