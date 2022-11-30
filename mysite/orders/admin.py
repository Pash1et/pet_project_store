from django.contrib import admin
from .models import Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('id', 'name', 'phone', 'created', 'updated')

    inlines = [ProductInOrderInline]
