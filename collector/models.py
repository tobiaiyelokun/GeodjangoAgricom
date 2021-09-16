from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    Name=models.CharField(max_length=20)
    Landuse = models.PointField(srid=4326)
    #objects = models.GeoManager()


    def __unicode__(self):
        return self.name

#to correct the plural issue
    class Meta:
        verbose_name_plural = 'Incidences'


class Ward(models.Model):
    objectid = models.BigIntegerField()
    statecode = models.CharField(max_length=254)
    wardname = models.CharField(max_length=254)
    urban = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.wardname
