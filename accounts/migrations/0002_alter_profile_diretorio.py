# Generated by Django 4.2.5 on 2023-09-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='diretorio',
            field=models.CharField(max_length=255),
        ),
    ]
