#!/usr/bin/env python3

import json
from shapely.geometry import shape, mapping
from shapely.validation import make_valid

districts = {
    1: ('Council Member Christopher Marte', 'Manhattan', '''Battery Park City, Civic Center, Chinatown, Financial District, Little Italy, the Lower East Side, NoHo, SoHo, South Street Seaport, South Village, TriBeCa & Washington Square'''),
    3: ('Council Member Erik Bottcher', 'Manhattan', '''Chelsea, Hell’s Kitchen, Greenwich Village, West SoHo, Hudson Square, Times Square, Garment District, Flatiron, Upper West Side'''),
    4: ('Council Member Keith Powers', 'Manhattan', '''Upper East Side, Carnegie Hill, Yorkville, Central Park South, Midtown East, Times Square, Koreatown, Stuyvesant Town and Peter Cooper Village, Waterside Plaza, Tudor City, Turtle Bay, Murray Hill, Sutton Place'''),
    5: ('Council Member Julie Menin', 'Manhattan', '''Upper East Side's Yorkville, Lenox Hill, Carnegie Hill, Roosevelt Island, Midtown East, Sutton Place, El Barrio in East Harlem'''),
    6: ('Council Member Gale A. Brewer', 'Manhattan', '''Central Park, Lincoln Square, Upper West Side, Clinton'''),
    7: ('Council Member Shaun Abreu', 'Manhattan', '''Manhattan Valley, Manhattanville, Morningside Heights, Hamilton Heights'''),
    10: ('Council Member Carmen De La Rosa', 'Manhattan', '''Washington Heights, Inwood, Marble Hill'''),
    12: ('Council Member Kevin C. Riley', 'Bronx', ''),
    13: ('Council Member Marjorie Velazquez', 'Bronx', '''Allerton, City Island, Country Club, Edgewater Park, Ferry Point, Locust Point, Morris Park, Pelham Bay, Pelham Gardens, Pelham Parkway, Schuylerville, Silver Beach, Spencer Estates, Throggs Neck, Van Nest, Waterbury LaSalle, Westchester Square, Zerega'''),
    14: ('Council Member Pierina Ana Sanchez', 'Bronx', ''),
    16: ('Council Member Althea Stevens', 'Bronx', '''Claremont, Concourse, Concourse Village, Highbridge, Morris Heights, Mount Eden, Morrisania'''),
    18: ('Council Member Amanda Farias', 'Bronx', ''),
    22: ('Council Member Tiffany Caban', 'Queens', '''Astoria, East Elmhurst, Jackson Heights, Woodside'''),
    23: ('Council Member Linda Lee', 'Queens', ''),
    25: ('Council Member Shekar Krishnan', 'Queens', ''),
    26: ('Council Member Julie Won', 'Queens', '''Sunnyside, Woodside, Long Island City, Astoria, Dutch Kills'''),
    27: ('Council Member Nantasha Williams', 'Queens', '''Cambria Heights, Hollis, Jamaica, St. Albans, Queens Village, and Springfield Gardens'''),
    28: ('Speaker Adrienne E. Adams', 'Queens', '''Jamaica, Richmond Hill, Rochdale Village, South Ozone Park'''),
    29: ('Council Member Lynn Schulman', 'Queens', '''Rego Park, Forest Hills, Kew Gardens, Richmond Hill'''),
    33: ('Council Member Lincoln Restler', 'Brooklyn', '''Boerum Hill, Brooklyn Heights, Brooklyn Navy Yard, Downtown Brooklyn, Dumbo, Fulton Ferry, Greenpoint, Vinegar Hill, Williamsburg.'''),
    34: ('Council Member Jennifer Gutierrez', 'Brooklyn', '''Williamsburg, Bushwick, Ridgewood'''),
    35: ('Council Member Crystal Hudson', 'Brooklyn', '''Fort Greene, Clinton Hill, Crown Heights, Prospect Heights, Bedford Stuyvesant'''),
    36: ('Council Member Chi Osse', 'Brooklyn', '''Bedford Stuyvesant, Northern Crown Heights'''),
    37: ('Council Member Sandy Nurse', 'Brooklyn', '''Bushwick, Ocean Hill, Brownsville, Cypress Hills, East New York, City Line'''),
    38: ('Council Member Alexa Aviles', 'Brooklyn', '''Red Hook, Sunset Park, Greenwood Heights and portions of Windsor Terrace, Dyker Heights, and Boro Park'''),
    39: ('Council Member Shahana Hanif', 'Brooklyn', '''Cobble Hill, Carroll Gardens, Columbia Waterfront, Gowanus, Park Slope, Windsor Terrace, Borough Park, Kensington'''),
    40: ('Council Member Rita Joseph', 'Brooklyn', '''Crown Heights, East Flatbush, Flatbush, Kensington, Midwood, Prospect Park, and Prospect Lefferts Gardens'''),
    42: ('Council Member Charles Barron', 'Brooklyn', ''),
    45: ('Council Member Farah Louis', 'Brooklyn', '''Flatbush, East Flatbush, Flatlands, Midwood, Canarsie'''),
}

with open('alldistricts.geojson') as jsonfile:
    indata = json.load(jsonfile)

outdata = {attr:indata[attr] for attr in indata if attr != 'features'}
outdata['features'] = []

for infeature in indata['features']:
    district_id = infeature['properties']['CounDist']
    if district_id in districts:
        outfeature = infeature.copy()
        outfeature['geometry'] = mapping(make_valid(shape(infeature['geometry'])))
        outfeature['properties']['CounPerson'] = districts[district_id][0]
        outfeature['properties']['Borough'] = districts[district_id][1]
        outdata['features'].append(outfeature)

with open('districts.geojson', 'w') as jsonfile:
    json.dump(outdata, jsonfile, indent=1, sort_keys=True)
