# Generated by Django 2.2.20 on 2021-04-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20210413_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='teamName',
            field=models.CharField(max_length=30, null=True, verbose_name='Название команды'),
        ),
    ]
