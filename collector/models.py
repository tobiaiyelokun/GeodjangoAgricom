from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Incidences(models.Model):
    Name=models.CharField(max_length=20)
    Landuse=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
        
#to correct the plural issue
    class Meta:
        verbose_name_plural = 'Incidences'