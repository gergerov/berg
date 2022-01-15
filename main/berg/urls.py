from django.urls import path
from berg.views import (
    ProductStructView, ProductStructShortView
)

urlpatterns = [
    path(
        'product_struct_by_product/<int:product_id>', 
        view=ProductStructView.as_view(), 
        name='product-struct-by-product'
    ),
    path(
        'product_struct_by_product/<int:product_id>/short', 
        view=ProductStructShortView.as_view(), 
        name='product-struct-by-product-short'
    ),
]