from django.contrib import admin
from .models import Incidences
# Register your models here.

class IncidencesAdmin (admin.ModelAdmin):
    list_display = ('Name', 'Landuse')


admin.site.register(Incidences, IncidencesAdmin)
