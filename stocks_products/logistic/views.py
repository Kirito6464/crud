from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from models import Product, Stock
from serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from filters import StockFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StockFilter
    # при необходимости добавьте параметры фильтрации
