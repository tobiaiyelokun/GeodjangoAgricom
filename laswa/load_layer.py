import os
from django.contrib.gis.utils import LayerMapping
from .models import Bathy, Route, Chart


#This is the layer mapping code.
bathy_mapping = {
    'bathy': 'Bathy',
    'geom': 'MULTIPOLYGON',
}

route_mapping = {
    'name': 'Name',
    'route_id': 'Route_ID',
    'avg_depth': 'avg_depth',
    'geom': 'MULTILINESTRING',
}


chart_mapping = {
    'depth': 'Depth',
    'geom': 'MULTIPOINT',
}

#Adding the path to the shapefile to import
bathy_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/bathy.shp'))
route_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/route.shp'))
chart_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/chart.shp'))

#followed by run function to add them.
def run(verbose=True):
	lm = LayerMapping(Bathy, bathy_shp, bathy_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)

	lx = LayerMapping(Route, route_shp, route_mapping, transform= False, encoding='iso-8859-1')
	lx.save(strict=True,verbose=verbose)

	ly = LayerMapping(Chart, chart_shp, chart_mapping, transform= False, encoding='iso-8859-1')
	ly.save(strict=True,verbose=verbose)
