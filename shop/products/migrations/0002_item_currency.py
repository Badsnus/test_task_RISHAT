# Generated by Django 4.1.7 on 2023-02-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'USD'), ('euro', 'eur')], default='usd', max_length=5, verbose_name='валюта'),
        ),
    ]