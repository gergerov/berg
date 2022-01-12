from rest_framework import routers
from berg.views import UnitViewSet


berg_router = routers.DefaultRouter()
berg_router.register(r'units', UnitViewSet, basename='unit')