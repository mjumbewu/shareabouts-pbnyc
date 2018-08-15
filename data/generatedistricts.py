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
    2:	('Carlina Rivera', 'Manhattan', '''East Village, Gramercy Park, Kips Bay, Lower East Side, Murray Hill, Rose Hill'''),
    3:	('Corey Johnson', 'Manhattan', '''West Village, Flatiron, Chelsea, Hell's Kitchen'''),
    4:	('Keith Powers', 'Manhattan', ''''''),
    5:	('Ben Kallos', 'Manhattan', '''Upper East Side, Yorkville'''),
    6:	('Helen Rosenthal', 'Manhattan', '''Upper West Side'''),
    7:	('Mark Levine', 'Manhattan', '''Morningside Heights, Manhattanville, Hamilton Heights'''),
    8:	('Diana Ayala', 'Manhattan/Bronx', '''El Barrio/East Harlem, Mott Haven, Highbridge, Concourse, Longwood'''),
    9:	('Bill Perkins', 'Manhattan', '''Central Harlem, Morningside Heights, Upper West Side, East Harlem'''),
    10:	('Ydanis Rodriguez', 'Manhattan', '''Washington Heights, Inwood, Marble Hill'''),
    11:	('Andrew Cohen', 'Bronx', '''Bedford Park, Kingsbridge, Norwood, Riverdale, Van Cortlandt Village, Wakefield, Woodlawn'''),
    15:	('Ritchie Torres', 'Bronx', '''Belmont, Tremont, Allerton'''),
    16:	('Vanessa Gibson', 'Bronx', '''West Bronx, Morrisania, Highbridge and Melrose'''),
    17:	('Rafael Salamanca', 'Bronx', '''Longwood, Hunts Point, Concourse, Crotona Park, Melrose, Morrisania, Mott Haven, North Brother Island, Port Morris and Soundview'''),
    19:	('Paul Vallone', 'Queens', '''Bayside, Whitestone, Auburndale, College Point, Little Neck, Douglaston, North Flushing'''),
    22:	('Costa Constantinides', 'Queens', '''Astoria, parts of Woodside, East Elmhurst, Jackson Heights'''),
    26:	('Jimmy Van Bramer', 'Queens', '''Woodside, Sunnyside, Long Island City, Astoria'''),
    27:	('I. Daneek Miller', 'Queens', '''St. Albans, Hollis, Cambria Heights, Queens Village, Addisleigh Park, Jamaica, Springfield Gardens'''),
    28:	('Adrienne Adams', 'Queens', '''Jamaica, Richmond Hill, Rochdale Village, South Ozone Park'''),
    29:	('Karen Koslowitz', 'Queens', '''Forest Hills, Rego Park, Kew Gardens, Richmond Hill'''),
    31:	('Donovan Richards', 'Queens', '''Laurelton, Rosedale, parts of Springfield Gardens, Bayswater, Hammels, Arverne, Edgemere, Far Rockaway'''),
    33:	('Stephen Levin', 'Brooklyn', '''Brooklyn Heights, DUMBO, Williamsburg, Greenpoint, Boerum Hill, Vinegar Hill, Downtown Brooklyn, Bedford–Stuyvesant'''),
    34:	('Antonio Reynoso', 'Brooklyn/Queens', '''Bushwick, Williamsburg, Ridgewood'''),
    35:	('Laurie Cumbo', 'Brooklyn', '''Clinton Hill, Fort Greene, Prospect Heights, Crown Heights, Bedford-Stuyvesant, Boerum Hill'''),
    36:	('Robert Cornegy', 'Brooklyn', '''Bedford-Stuyvesant and Crown Heights'''),
    38:	('Carlos Menchaca', 'Brooklyn', '''Sunset Park, Greenwood, South Slope, Red Hook'''),
    39:	('Brad Lander', 'Brooklyn', '''Cobble Hill, Carroll Gardens, Columbia Waterfront, Gowanus, Park Slope, Windsor Terrace, Kensington, Boro Park'''),
    40:	('Mathieu Eugene', 'Brooklyn', '''Kensington, Prospect-Lefferts, Ditmas Park, Crown Heights, Flatbush and East Flatbush'''),
    41:	('Alicka Ampry-Samuel', 'Brooklyn', '''Bedford-Stuyvesant, Ocean Hill-Brownsville, East Flatbush, Crown Heights'''),
    43:	('Justin Brannan', 'Brooklyn', '''Bay Ridge, Dyker Heights, Bensonhurst, Bath Beach'''),
    45:	('Jumaane Williams', 'Brooklyn', '''Flatbush, East Flatbush, Flatlands, parts of Midwood, Canarsie'''),
    47:	('Mark Treyger', 'Brooklyn', '''Bensonhurst, Coney Island, Gravesend, Sea Gate'''),
    49:	('Debi Rose', 'Staten Island', '''St. George, Tompkinsville, Stapleton, Snug Harbor, Livingston, New Brighton, Randall Manor, West Brighton, Silver lake, Clove Lakes, Clifton, Concord, Rosebank, Port Richmond, Elm Park and Mariners Harbor'''),
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
