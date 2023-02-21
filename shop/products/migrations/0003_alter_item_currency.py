# Generated by Django 4.1.7 on 2023-02-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'usd'), ('EUR', 'euro')], default='usd', max_length=5, verbose_name='валюта'),
        ),
    ]