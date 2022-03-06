from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, CustomerSerializer, StockSerializer
from inventario.models import Product
from facturacion.models import Customer
from django.db.models import Q


class Stock(APIView):
    def get(self, request):
        product = Product.objects.filter(stock__gt=0)
        data = StockSerializer(product, many=True).data
        return Response(data)

class ProductList(APIView):
    def get(self, request):
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data
        return Response(data)

class ProductDetail(APIView):
    def get(self, request, code):
        product = get_object_or_404(Product, Q(code=code)|Q(barCode=code))
        data = ProductSerializer(product).data
        return Response(data)

class customerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        data = CustomerSerializer(customer).data
        return Response(data, status=status.HTTP_200_OK)
