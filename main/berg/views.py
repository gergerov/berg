from rest_framework.viewsets import ModelViewSet, generics
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
from berg.permissions import BergModelPermission


class BergModelViewSet(ModelViewSet):
  """
  Базовый класс modelvieset приложения berg.
  Задает права к представлению и методы аутентификации.
  Распределяет тротлинг в зависимости от категории пользователя
  (админу - одно, простому юзеру - другое) 
  с помощью метода dispath.
  """
  authentication_classes = [
    TokenAuthentication, 
    BasicAuthentication, 
    SessionAuthentication
  ]
  permission_classes = [BergModelPermission]

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser:
      self.throttle_scope = 'berg-admin'
    else:
      self.throttle_scope = 'berg-user'
    return super().dispatch(request, *args, **kwargs)


class UnitViewSet(BergModelViewSet):
  """Представление единиц измерения"""
  serializer_class = UnitSerializer
  queryset = Unit.units.all()
  pagination_class = UnitPagination


class NutrientViewSet(BergModelViewSet):
  """Представление нутриентов"""
  serializer_class = NutrientSerializer
  queryset = Nutrient.nutrients.all()
  pagination_class = NutrientPagination


class ProductViewSet(BergModelViewSet):
  """Представление продуктов. Search - поиск по названию."""
  serializer_class = ProductSerializer
  queryset = Product.products.all()
  pagination_class = ProductPagination
  filter_backends = [ProductFilter]
  search_fields = ['^product_name',]


class ProductStructView(generics.RetrieveAPIView):
  """Представление состава продукта"""
  serializer_class = ProductStructSerializer

  def get(self, request, product_id, *args, **kwargs):
    queryset = ProductStruct.product_structs.by_product(product_id)
    serializer = self.serializer_class(queryset, many=True, context={'request': request})
    return Response(serializer.data, status=200)


class ProductStructShortView(generics.RetrieveAPIView):
  """Представление состава продукта (краткий формат)"""
  serializer_class = ProductStructShortSerializer

  def get(self, request, product_id, *args, **kwargs):
    queryset = ProductStruct.product_structs.by_product(product_id).short()
    serializer = self.serializer_class(queryset, many=True)
    if len(queryset) == 0:
      return Response(status=404)
    return Response(serializer.data, status=200)
