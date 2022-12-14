from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name='Цена, ₽')
    articul = models.IntegerField(verbose_name='Артикул')
    count = models.PositiveIntegerField(verbose_name='Количество')
    is_active = models.BooleanField(default=False,
                                    verbose_name='Показать на сайте?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/media/product_img/',
                              verbose_name='Фотография')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
