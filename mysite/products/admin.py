from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count', 'is_active', 'articul', 'image')
    empty_value_display = '-empty-'
    inlines = [ProductImageInline]

    def image(self, obj):
        return format_html(f'<img src="/{obj.images.get().image}" style="width: 45px; height:45px;" />')
    image.short_description = 'Изображение'
