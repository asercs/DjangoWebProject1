# Generated by Django 2.2.20 on 2021-04-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_market_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='seller_url',
            field=models.TextField(null=True, verbose_name='Ссылка на продавца'),
        ),
    ]
