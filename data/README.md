# Data Preparation

To prepare the districts geo data, I start with the *alldistricts.geojson* file.

## Shareabouts Boundary Service

Copy the latest *modyfidistricts* script and update the years. Open the new
script and update the participating districts. Run this script from within the
*data/* folder to generate a new *districts.geojson* file. This file should be
added to the boundary service instance.

Update the URL in *[flavor]/templates/\_region_service_url*. Be careful not to
include a newline at the end of the file.

## Districts Page

Copy the latest *generatedistricts.py* script and update the years. Open the new
script and update the participating districts. Run this script from within the
*data/* folder, something like:

    ./generatedistricts.py > ../src/flavors/2018/jstemplates/pages/district.html

## Map Tiles

Open *PBNYC-Base(...)/style.json* and find all instances of `CounDist`. Update
and use the same version of the list of districts for each of these sections.
Head to https://www.mapbox.com/studio/ and replace the **PBNYC Base** style
with this *style.json* file.
