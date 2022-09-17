# Data Preparation

To prepare the districts geo data, I start with the *alldistricts.geojson* file.

## Shareabouts Boundary Service

Copy the latest *modyfidistricts* script and update the cycle. Open the new
script and update the participating districts. Run this script from within the
*data/* folder to generate a new *districts.geojson* file. This file should be
added to the boundary service instance.

Update the URL in *[flavor]/templates/\_region_service_url*. Be careful not to
include a newline at the end of the file.

## Districts Page

Copy the latest *generatedistricts.py* script and update the cycle. Open the new
script and update the participating districts. Run this script from within the
*data/* folder, something like:

    ./generatedistricts.py > ../src/flavors/2018/jstemplates/pages/district.html

## Map Styles

Open *PBNYC-Base(...)/style.json* and find all instances of `CounDist`. Update
and use the same version of the list of districts for each of these sections.
Head to https://www.mapbox.com/studio/ and replace the **PBNYC Base** style
with this *style.json* file.

## Map Tile Source Data

The following commands can be useful in managing the map tile source data:

```bash
# ~~~~~~~~~~~~~~~~~~~~
# Generate clean districts, as the original alldistricts.geojson file could contain invalid polygons.
./generatealldistrictsclean.py > alldistricts-clean.geojson

tilesets upload-source --replace pbnyc alldistricts-clean alldistricts-clean.geojson
#tilesets create pbnyc.alldistricts-clean --recipe alldistricts-clean.recipe.json --name alldistricts-clean
tilesets update-recipe pbnyc.alldistricts-clean alldistricts-clean.recipe.json
tilesets publish pbnyc.alldistricts-clean

# ~~~~~~~~~~~~~~~~~~~~
# Generate a cutout of the city.
./generatealldistrictsinverse.py > alldistricts-inverse.geojson

tilesets upload-source --replace pbnyc alldistricts-inverse alldistricts-inverse.geojson
#tilesets create pbnyc.alldistricts-inverse --recipe alldistricts-inverse.recipe.json --name alldistricts-inverse
tilesets update-recipe pbnyc.alldistricts-inverse alldistricts-inverse.recipe.json
tilesets publish pbnyc.alldistricts-inverse

# ~~~~~~~~~~~~~~~~~~~~
# Centroids may be edited manually, so just upload them to Mapbox.
tilesets upload-source --replace pbnyc alldistricts-centroids alldistricts-centroids.geojson
#tilesets create pbnyc.alldistricts-centroids --recipe alldistricts-centroids.recipe.json --name alldistricts-centroids
tilesets update-recipe pbnyc.alldistricts-centroids alldistricts-centroids.recipe.json
tilesets publish pbnyc.alldistricts-centroids
```