# Generated by Django 2.2.20 on 2021-04-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20210414_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='headset',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Наушники'),
        ),
        migrations.AlterField(
            model_name='players',
            name='insta',
            field=models.TextField(blank=True, null=True, verbose_name='Instagram-link'),
        ),
        migrations.AlterField(
            model_name='players',
            name='keyboard',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Клавиатура'),
        ),
        migrations.AlterField(
            model_name='players',
            name='monitor',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Монитор'),
        ),
        migrations.AlterField(
            model_name='players',
            name='mouse',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Мышка'),
        ),
        migrations.AlterField(
            model_name='players',
            name='mousepad',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Коврик'),
        ),
        migrations.AlterField(
            model_name='players',
            name='steam',
            field=models.TextField(blank=True, null=True, verbose_name='Steam-profile'),
        ),
        migrations.AlterField(
            model_name='players',
            name='vk',
            field=models.TextField(blank=True, null=True, verbose_name='VK-link'),
        ),
    ]