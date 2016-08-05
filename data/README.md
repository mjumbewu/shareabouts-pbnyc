# Data Preparation

To prepare the districts geo data, I start with the *alldistricts.geojson* file.

## Shareabouts Boundary Service

Copy the latest *modyfidistricts* script and update the years. Open the new
script and update the participating districts. Run this script from within the
*data/* folder to generate a new *districts.geojson* file. This file should be
added to the boundary service instance.

## Map Tiles

Open a new qgis project and add layers from *district-centroids.geojson* and
*districts.geojson*. Make sure that there are centroids for each district. If
not, convert the districts layer to a shapefile, add the required centroids,
and save the geojson file again.