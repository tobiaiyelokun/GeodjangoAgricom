from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Bathy(models.Model):
    bathy = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.bathy

class Route(models.Model):
    name = models.CharField(max_length=50)
    route_id = models.CharField(max_length=80)
    avg_depth = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    def __unicode__(self):
        return self.name


class Chart(models.Model):
    depth = models.FloatField()
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.depth
