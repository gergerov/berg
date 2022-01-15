from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import (
  TokenAuthentication, 
  BasicAuthentication, 
  SessionAuthentication
)
from rest_framework.response import Response
from berg.serializers import (
  UnitSerializer, NutrientSerializer, 
  ProductSerializer, ProductStructSerializer,
  ProductStructShortSerializer
)
from berg.models import (
  Unit, Nutrient, Product, ProductStruct
)
from berg.paginations import (
  UnitPagination, NutrientPagination, ProductPagination
)
from berg.filters import ProductFilter


class UnitViewSet(ModelViewSet):
  """Представление единиц измерения"""
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  serializer_class = UnitSerializer
  queryset = Unit.units.all()
  pagination_class = UnitPagination
  permission_classes = [IsAdminUser]


class NutrientViewSet(ModelViewSet):
  """Представление нутриентов"""
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  serializer_class = NutrientSerializer
  queryset = Nutrient.nutrients.all()
  pagination_class = NutrientPagination
  permission_classes = [IsAdminUser]


class ProductViewSet(ModelViewSet):
  """Представление продуктов. Search - поиск по названию."""
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  serializer_class = ProductSerializer
  queryset = Product.products.all()
  pagination_class = ProductPagination
  permission_classes = [IsAdminUser]
  filter_backends = [ProductFilter]
  search_fields = ['^product_name',]


class ProductStructView(generics.RetrieveAPIView):
  """Представление состава продукта"""
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  serializer_class = ProductStructSerializer
  permission_classes = [IsAdminUser]

  def get(self, request, product_id, *args, **kwargs):
    queryset = ProductStruct.product_structs.by_product(product_id)
    serializer = self.serializer_class(queryset, many=True, context={'request': request})
    return Response(serializer.data, status=200)


class ProductStructShortView(generics.RetrieveAPIView):
  """Представление состава продукта (краткий формат)"""
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  serializer_class = ProductStructShortSerializer
  permission_classes = [IsAdminUser]

  def get(self, request, product_id, *args, **kwargs):
    queryset = ProductStruct.product_structs.by_product(product_id).short()
    serializer = self.serializer_class(queryset, many=True)
    if len(queryset) == 0:
      return Response(status=404)
    return Response(serializer.data, status=200)
