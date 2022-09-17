#!/usr/bin/env python3

from json import load, dumps
from shapely.geometry import box, shape, mapping
from shapely.ops import transform, unary_union
from shapely.validation import make_valid
import pyproj

# Load the raw data
data = load(open('alldistricts.geojson'))
geoms = [make_valid(shape(feature['geometry'])) for feature in data['features']]

# Create transformers to project to and from NY state plane
wgs84 = pyproj.CRS('EPSG:4326')
nyli = pyproj.CRS('EPSG:32118')  # NAD83 / New York Long Island (m)

project = pyproj.Transformer.from_crs(wgs84, nyli, always_xy=True).transform
unproject = pyproj.Transformer.from_crs(nyli, wgs84, always_xy=True).transform

# Make each geometry just a smidge larger, so that there's no space where there shouldn't be.
projected_geoms = [transform(project, geom) for geom in geoms]
buffered_geoms = [geom.buffer(1) for geom in projected_geoms]

# Union all the geometries together to get all of NYC.
projected_union = unary_union(projected_geoms)
union = transform(unproject, projected_union)

# Create a big box and subtract the totality of NYC from it.
bounds = (-75.24, 39.89, -72.81, 41.52)
extent = box(*bounds)
inverse = extent - union

# Output newline-delimited GeoJSON (even though there's only one feature)
print(dumps(
    {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'id': 0,
                'properties': {},
                'geometry': mapping(inverse),
            }
        ]
    },
    indent='\t',
))