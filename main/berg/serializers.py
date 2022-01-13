from django.db.models import fields
from rest_framework import serializers as s
from berg.models import Product, ProductStruct, Nutrient, Unit


class UnitSerializer(s.HyperlinkedModelSerializer):
  class Meta:
    model = Unit
    fields = ('unit_id', 'value', 'url', )


class NutrientSerializer(s.HyperlinkedModelSerializer):
  class Meta:
    model = Nutrient
    fields = ('nutrient_id', 'nutrient_name', 'status', 'url', )


class ProductSerializer(s.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    fields = ('product_id', 'product_name', 'status', 'url', )
