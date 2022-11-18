from django.shortcuts import render
from products.models import Product


def landing(request):
    products = Product.objects.filter(is_active=True)[:4]
    return render(request,
                  'landing/landing.html',
                  context={'products': products})
