#!/usr/bin/env python3

from json import load
from shapely import geometry

collection = load(open('alldistricts.geojson'))

boroughs = [
    'Bronx',
    'Brooklyn',
    'Manhattan',
    'Queens',
    'Staten Island',
]

districts = {
    1: ('Margaret S. Chin', 'Manhattan', '''Battery Park City, Civic Center, Chinatown, Financial District, Little Italy, the Lower East Side, NoHo, SoHo, South Street Seaport, South Village, TriBeCa & Washington Square'''),
    2: ('Carlina Rivera', 'Manhattan', '''East Village, Gramercy Park, Kips Bay, Lower East Side, Murray Hill, Rose Hill'''),
    3: ('Corey Johnson', 'Manhattan', '''Chelsea, Hell’s Kitchen, Greenwich Village, West SoHo, Hudson Square, Times Square, Garment District, Flatiron, Upper West Side'''),
    4: ('Keith Powers', 'Manhattan', '''Upper East Side, Carnegie Hill, Yorkville, Central Park South, Midtown East, Times Square, Koreatown, Stuyvesant Town and Peter Cooper Village, Waterside Plaza, Tudor City, Turtle Bay, Murray Hill, Sutton Place'''),
    5: ('Ben Kallos', 'Manhattan', '''Upper East Side's Yorkville, Lenox Hill, Carnegie Hill, Roosevelt Island, Midtown East, Sutton Place, El Barrio in East Harlem'''),
    6: ('Helen Rosenthal', 'Manhattan', '''Central Park, Lincoln Square, Upper West Side, Clinton'''),
    7: ('Mark Levine', 'Manhattan', '''Manhattan Valley, Manhattanville, Morningside Heights, Hamilton Heights'''),
    8: ('Diana Ayala', 'Manhattan/Bronx', '''El Barrio/East Harlem, Mott Haven, Highbridge, Concourse, Longwood, Port Morris'''),
    9: ('Bill Perkins', 'Manhattan', '''Central Harlem, Morningside Heights, Upper West Side, East Harlem'''),
    10: ('Ydanis Rodriguez', 'Manhattan', '''Washington Heights, Inwood, Marble Hill'''),
    13: ('Mark Gjonaj', 'Bronx', '''Allerton, City Island, Country Club, Edgewater Park, Ferry Point, Locust Point, Morris Park, Pelham Bay, Pelham Gardens, Pelham Parkway, Schuylerville, Silver Beach, Spencer Estates, Throggs Neck, Van Nest, Waterbury LaSalle, Westchester Square, Zerega'''),
    15: ('Ritchie J. Torres', 'Bronx', '''Bedford Park, Fordham, Mount Hope, Bathgate, Belmont, East Tremont, West Farms, Van Nest, Allerton, Olinville'''),
    16: ('Vanessa L. Gibson', 'Bronx', '''Claremont, Concourse, Concourse Village, Highbridge, Morris Heights, Mount Eden, Morrisania'''),
    17: ('Rafael Salamanca Jr.', 'Bronx', '''Concourse Village, Crotona Park East, East Tremont, Hunts Point, Longwood, Melrose, Morrisania, Port Morris, West Farms, North Brother Island, South Brother Island'''),
    19: ('Paul Vallone', 'Queens', '''Auburndale, Bay Terrace, Bayside, Beechhurst, College Point, Douglaston, Flushing, Little Neck, Malba, Whitestone'''),
    22: ('Costa Constantinides', 'Queens', '''Astoria, East Elmhurst, Jackson Heights, Woodside'''),
    26: ('Jimmy Van Bramer', 'Queens', '''Sunnyside, Woodside, Long Island City, Astoria, Dutch Kills'''),
    27: ('I. Daneek Miller', 'Queens', '''Cambria Heights, Hollis, Jamaica, St. Albans, Queens Village, and Springfield Gardens'''),
    28: ('Adrienne E. Adams', 'Queens', '''Jamaica, Richmond Hill, Rochdale Village, South Ozone Park'''),
    29: ('Karen Koslowitz', 'Queens', '''Rego Park, Forest Hills, Kew Gardens, Richmond Hill'''),
    31: ('Donovan J. Richards', 'Queens', '''Arverne, Brookville, Edgemere, Far Rockaway, Laurelton, Rosedale, Springfield Gardens'''),
    33: ('Stephen T. Levin', 'Brooklyn', '''Boerum Hill, Brooklyn Heights, Brooklyn Navy Yard, Downtown Brooklyn, Dumbo, Fulton Ferry, Greenpoint, Vinegar Hill, Williamsburg.'''),
    34: ('Antonio Reynoso', 'Brooklyn/Queens', '''Williamsburg, Bushwick, Ridgewood'''),
    35: ('Laurie A. Cumbo', 'Brooklyn', '''Fort Greene, Clinton Hill, Crown Heights, Prospect Heights, Bedford Stuyvesant'''),
    36: ('Robert E. Cornegy, Jr.', 'Brooklyn', '''Bedford Stuyvesant, Northern Crown Heights'''),
    37: ('Rafael Espinal', 'Brooklyn', '''Bushwick, Ocean Hill, Brownsville, Cypress Hills, East New York, City Line'''),
    38: ('Carlos Menchaca', 'Brooklyn', '''Red Hook, Sunset Park, Greenwood Heights and portions of Windsor Terrace, Dyker Heights, and Boro Park'''),
    39: ('Brad Lander', 'Brooklyn', '''Cobble Hill, Carroll Gardens, Columbia Waterfront, Gowanus, Park Slope, Windsor Terrace, Borough Park, Kensington'''),
    40: ('Mathieu Eugene', 'Brooklyn', '''Crown Heights, East Flatbush, Flatbush, Kensington, Midwood, Prospect Park, and Prospect Lefferts Gardens'''),
    41: ('Alicka Ampry-Samuel', 'Brooklyn', '''Bedford-Stuyvesant, Ocean Hill-Brownsville, East Flatbush, Crown Heights'''),
    43: ('Justin Brannan', 'Brooklyn', '''Bay Ridge, Dyker Heights, Bensonhurst, Bath Beach'''),
    45: ('Farah Louis', 'Brooklyn', '''Flatbush, East Flatbush, Flatlands, Midwood, Canarsie'''),
    47: ('Mark Treyger', 'Brooklyn', '''Bensonhurst, Coney Island, Gravesend, Sea Gate'''),
    49: ('Deborah Rose', 'Staten Island', '''Arlington, Clifton, Clove Lakes, Concord, Elm Park, Graniteville, Livingston, Mariners Harbor, New Brighton, Port Richmond, Randall Manor, Rosebank, St. George, Snug Harbor, Silver Lake, Stapleton, Sunnyside, West Brighton and Tompkinsville'''),
}

html = '''
<h1>{{#_}}Choose Your Council District{{/_}}</h1>
'''

for borough in boroughs:
    html += f'''\n<h4>{{{{#_}}}}{borough}{{{{/_}}}}</h4>\n'''
    for district, (member, distborough, neighborhoods) in sorted(districts.items(), key=lambda i: i[0]):
        if borough not in distborough:
            continue

        for feature in collection['features']:
            if int(feature['properties']['CounDist']) == district:
                break

        shape = geometry.shape(feature['geometry'])
        bounds = shape.bounds
        center_x = str((bounds[0] + bounds[2]) / 2)[:13]
        center_y = str((bounds[1] + bounds[3]) / 2)[:13]
        html += f'''<p class="district-item"><a rel="internal" href="/14/{center_y}/{center_x}">{{{{#_}}}}District{{{{/_}}}} {district}</a>: {member}<br><small>{neighborhoods}</small></p>\n'''

print(html)
