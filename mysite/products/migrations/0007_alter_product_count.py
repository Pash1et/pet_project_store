# Generated by Django 4.1.3 on 2022-12-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
    ]
