from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bathy, Route, Chart
# Create your views here.

class HomePageView(TemplateView):
	template_name = 'index.html'

def bathy_datasets(request):
	bathy = serialize('geojson', Bathy.objects.all())
	return HttpResponse(bathy,content_type='json')

def route_datasets(request):
	route = serialize('geojson', Route.objects.all())
	return HttpResponse(route,content_type='json')

def chart_datasets(request):
	chart = serialize('geojson', Chart.objects.all())
	return HttpResponse(chart,content_type='json')
