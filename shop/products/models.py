from django.db import models


class Item(models.Model):
    name = models.CharField('название', max_length=300)
    description = models.CharField('описание', max_length=2000)
    price = models.PositiveIntegerField('цена')

    CURRENCY_CHOICES = (
        ('USD', 'usd'),
        ('EUR', 'euro')
    )

    currency = models.CharField('валюта', choices=CURRENCY_CHOICES, max_length=5, default='usd')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name
