from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Bathy, Route, Chart

# Register your models here.

@admin.register(Bathy)
class BathyAdmin(LeafletGeoAdmin):
    list_display = ('bathy',)

@admin.register(Route)
class RouteAdmin(LeafletGeoAdmin):
    list_display = ('route_id','name','avg_depth')

@admin.register(Chart)
class ChartAdmin(LeafletGeoAdmin):
    list_display = ('depth',)
