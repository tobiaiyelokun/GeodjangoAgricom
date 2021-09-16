from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Incidences, Ward
# Create your views here.

class HomePageView(TemplateView):
	template_name = 'index.html'

def ward_datasets(request):
	ward = serialize('geojson', Ward.objects.all())
	return HttpResponse(ward,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')
