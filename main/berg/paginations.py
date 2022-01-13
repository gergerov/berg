from rest_framework.pagination import PageNumberPagination


class UnitPagination(PageNumberPagination):
    page_size = 30
    max_page_size = 120


class NutrientPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60


class ProductPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 30
