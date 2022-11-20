from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from .models import Product


def paginator(request, page_name):
    paginator = Paginator(page_name, settings.PAGINATOR_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def all_product(request):
    products = Product.objects.filter(is_active=True)
    page_obj = paginator(request, products)
    context = {
        'products': page_obj,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, articul):
    products = Product.objects.get(articul=articul)
    context = {
        'products': products,
    }
    return render(request, 'products/product_detail.html', context)
