from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from berg.serializers import (UnitSerializer, NutrientSerializer)
from berg.models import (Unit, Nutrient)
from berg.paginations import (UnitPagination, NutrientPagination)


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
