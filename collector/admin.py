from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidences, Ward
# Register your models here.

#class IncidencesAdmin (admin.ModelAdmin):
    #list_display = ('Name', 'Landuse')


#admin.site.register(Incidences, IncidencesAdmin)


@admin.register(Incidences)
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('Name', 'Landuse')

@admin.register(Ward)
class WardAdmin(LeafletGeoAdmin):
    list_display = ('objectid','statecode','wardname','urban' )
