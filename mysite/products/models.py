from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name='Цена')
    articul = models.IntegerField(verbose_name='Артикул')
    is_active = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
