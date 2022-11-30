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
    recently_viewed = None
    recently_viewed_sort = None

    if 'recently_viewed' in request.session:
        if articul in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(articul)

        if len(request.session['recently_viewed']) > 4:
            request.session['recently_viewed'].pop()

        recently_viewed = Product.objects.filter(
            articul__in=request.session['recently_viewed']
        )

        recently_viewed_sort = sorted(
            recently_viewed,
            key=lambda x: request.session['recently_viewed'].index(x.articul)
        )

        request.session['recently_viewed'].insert(0, articul)

    else:
        request.session['recently_viewed'] = [articul]

    request.session.modified = True

    context = {
        'products': products,
        'recently_viewed': recently_viewed_sort,
    }
    return render(request, 'products/product_detail.html', context)
