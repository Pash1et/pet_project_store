from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_product),
    path('<int:articul>/', views.product_detail),
]
