from django.shortcuts import render
from .models import Product


def all_product(request):
    products = Product.objects.filter(is_active=True)
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
