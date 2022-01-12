from django.db import models


class UnitManager(models.Manager):

  def all(self):
    return self.get_queryset()