from django.db import models
from products.models import Product


class Order(models.Model):

    name = models.CharField(max_length=256, verbose_name='ФИО')
    phone = models.CharField(max_length=32, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True,
                                   verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,
                                   verbose_name='Обновлен')

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0,
                                verbose_name='Цена за единицу')
    count = models.IntegerField(default=1, verbose_name='Кол-во')
    total_price = models.DecimalField(max_digits=10, decimal_places=0,
                                      default=0, verbose_name='Общая цена')

    def __str__(self) -> str:
        return self.product.name

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.total_price = self.price * self.count
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар в заказ'
        verbose_name_plural = 'Товары в заказе'
