# Generated by Django 4.1.3 on 2022-12-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
    ]