import os
from django.contrib.gis.utils import LayerMapping
from .models import Ward



ward_mapping = {
    'objectid': 'OBJECTID',
    'statecode': 'StateCode',
    'wardname': 'WardName',
    'urban': 'Urban',
    'geom': 'MULTIPOLYGON',
}

ward_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/ward.shp'))

def run(verbose=True):
	lm = LayerMapping(Ward, ward_shp, ward_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)
