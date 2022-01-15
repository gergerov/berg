from django.db import models


class UnitManager(models.Manager):

  def all(self):
    return self.get_queryset().order_by('unit_id')


class NutrientManager(models.Manager):

  def all(self):
    return self.get_queryset().order_by('nutrient_name')

  def active(self):
    return self.all().filter(status=0)


class ProductManager(models.Manager):

  def all(self):
    return self.get_queryset().order_by('product_name')

  def active(self):
    return self.all().filter(status=0)


class ProductStructQuerySet(models.QuerySet):
  
  def active(self):
    return self.filter(status=0)

  def by_product(self, product_id):
    return self.filter(product__product_id=product_id)

  def related(self):
    return self.select_related('unit', 'product', 'nutrient')

  def ordered(self):
    return self.order_by('product_struct_id')

  def short(self):
    return self.values('nutrient__nutrient_name', 'quantity', 'unit__value').distinct()


class ProductStructManager(models.Manager):

  def get_queryset(self):
      return ProductStructQuerySet(self.model, self._db)

  def all(self):
      return self.get_queryset().order_by_id()
  
  def by_product(self, product_id):
    return self.get_queryset().ordered().related().by_product(product_id)
