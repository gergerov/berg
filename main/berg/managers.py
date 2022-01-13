from django.db import models


class UnitManager(models.Manager):

  def all(self):
    return self.get_queryset().order_by('unit_id')


class NutrientManager(models.Manager):

  def all(self):
    return self.get_queryset().order_by('nutrient_name')

  def active(self):
    return self.all().filter(status=0)
