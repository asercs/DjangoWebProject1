# Generated by Django 2.2.20 on 2021-04-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, verbose_name='Имя')),
                ('secondName', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('currentTeam', models.CharField(max_length=30, verbose_name='Команда')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
    ]
