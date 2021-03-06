"""TestApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from collector import views
from collector.views import ward_datasets, point_datasets
from laswa.views import bathy_datasets, route_datasets, chart_datasets


urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'^', include('collector.urls'))
    path('',views.HomePageView.as_view()),

    path('ward_datasets/', views.ward_datasets, name='ward_datasets'),
    path('point_datasets/', views.point_datasets, name='point_datasets'),

    path('bathy_datasets/', bathy_datasets, name='bathy'),
    path('route_datasets/', route_datasets, name='route'),
    path('chart_datasets/', chart_datasets, name='chart'),

    ]
