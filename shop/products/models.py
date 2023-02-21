from django.db import models


class Item(models.Model):
    name = models.CharField('название', max_length=300)
    description = models.CharField('описание', max_length=2000)
    price = models.PositiveIntegerField('цена')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
