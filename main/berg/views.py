from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from berg.serializers import (
  UnitSerializer, NutrientSerializer, ProductSerializer
)
from berg.models import (
  Unit, Nutrient, Product
)
from berg.paginations import (
  UnitPagination, NutrientPagination, ProductPagination
)
from berg.filters import ProductFilter


class UnitViewSet(ModelViewSet):
  """Представление единиц измерения"""
  
  serializer_class = UnitSerializer
  queryset = Unit.units.all()
  pagination_class = UnitPagination
  permission_classes = [IsAdminUser]


class NutrientViewSet(ModelViewSet):
  """Представление нутриентов"""

  serializer_class = NutrientSerializer
  queryset = Nutrient.nutrients.all()
  pagination_class = NutrientPagination
  permission_classes = [IsAdminUser]


class ProductViewSet(ModelViewSet):
  """Представление продуктов. Search - поиск по названию."""

  serializer_class = ProductSerializer
  queryset = Product.products.all()
  pagination_class = ProductPagination
  permission_classes = [IsAdminUser]
  filter_backends = [
    ProductFilter
  ]
  search_fields = ['^product_name',]
