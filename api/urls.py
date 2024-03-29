from django.urls import path, include
from .views import ProductList, ProductDetail, customerDetail, Stock

urlpatterns = [
    path('v1/product/stock', Stock.as_view(), name="productStock"),
    path('v1/customer/<int:pk>', customerDetail.as_view(), name="customerDetail"),
    path('v1/products/', ProductList.as_view(), name='productList'),
    path('v1/products/<str:code>', ProductDetail.as_view(), name='productDetail'),
]