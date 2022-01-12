from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from berg.serializers import UnitSerializer
from berg.models import Unit
from berg.paginations import UnitPagination


class UnitViewSet(ModelViewSet):
  """Представление единиц измерения"""
  
  serializer_class = UnitSerializer
  queryset = Unit.units.all()
  pagination_class = UnitPagination
  permission_classes = [IsAdminUser]
