#!/usr/bin/env python3

from json import load, dumps
from shapely.geometry import shape, mapping
from shapely.validation import make_valid

# Load the raw data
data = load(open('alldistricts.geojson'))

for feature in data['features']:
    # Make each geometry valid
    valid_geom = make_valid(shape(feature['geometry']))
    feature['geometry'] = mapping(valid_geom)

    # Get rid of unnecessary fields
    del feature['properties']['OBJECTID']
    del feature['properties']['Shape__Area']
    del feature['properties']['Shape__Length']

    # Set a proper id
    feature['id'] = feature['properties']['CounDist']

# Order by district
data['features'] = sorted(data['features'], key=lambda f: f['properties']['CounDist'])

# Output GeoJSON
print(dumps(data, indent='\t'))
