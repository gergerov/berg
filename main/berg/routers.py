from rest_framework import routers
from berg.views import (UnitViewSet, NutrientViewSet)


berg_router = routers.DefaultRouter()
berg_router.register(r'units', UnitViewSet, basename='unit')
berg_router.register(r'nutrients', NutrientViewSet, basename='nutrient')
