# Generated by Django 2.2.20 on 2021-04-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_players_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='photo',
            field=models.TextField(blank=True, null=True, verbose_name='Фото'),
        ),
    ]