# Generated by Django 4.1.3 on 2022-11-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_created_order_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='price',
            new_name='total_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]
