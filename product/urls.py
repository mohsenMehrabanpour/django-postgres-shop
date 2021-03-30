from django.urls import path
from product.views import Product_single, Show_products
urlpatterns = [
    path('',Show_products.as_view(), name='home_page'),
    path('<int:id>/', Product_single.as_view(), name='single_product')
]
