from django.db.models import fields
from rest_framework import serializers as s
from berg.models import Product, ProductStruct, Nutrient, Unit


class UnitSerializer(s.HyperlinkedModelSerializer):
  class Meta:
    model = Unit
    fields = ('unit_id', 'value', 'url', )