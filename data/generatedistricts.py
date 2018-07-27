#!/usr/bin/env python

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
    2:	('Carlina Rivera', 'Manhattan'),
    3:	('Corey Johnson', 'Manhattan'),
    5:	('Ben Kallos', 'Manhattan'),
    6:	('Helen Rosenthal', 'Manhattan'),
    7:	('Mark Levine', 'Manhattan'),
    8:	('Diana Ayala', 'Manhattan/Bronx'),
    9:	('Bill Perkins', 'Manhattan'),
    10:	('Ydanis Rodriguez', 'Manhattan'),
    11:	('Andrew Cohen', 'Bronx'),
    15:	('Ritchie Torries', 'Bronx'),
    16:	('Vanessa Gibson', 'Bronx'),
    17:	('Rafael Salamanca', 'Bronx'),
    19:	('Paul Vallone', 'Queens'),
    22:	('Costa Constantinides', 'Queens'),
    26:	('Jimmy Van Bramer', 'Queens'),
    27:	('I. Daneek Miller', 'Queens'),
    28:	('Adrienne Adams', 'Queens'),
    29:	('Karen Koslowitz', 'Queens'),
    31:	('Donovan Richards', 'Queens'),
    33:	('Stephen Levin', 'Brooklyn'),
    34:	('Antonio Reynoso', 'Brooklyn/Queens'),
    35:	('Laurie Cumbo', 'Brooklyn'),
    36:	('Robert Cornegy', 'Brooklyn'),
    38:	('Carlos Menchaca', 'Brooklyn'),
    39:	('Brad Lander', 'Brooklyn'),
    40:	('Mathieu Eugene', 'Brooklyn'),
    41:	('Alicka Ampry-Samuel', 'Brooklyn'),
    43:	('Justin Brannan', 'Brooklyn'),
    45:	('Jumaane Williams', 'Brooklyn'),
    47:	('Mark Treyger', 'Brooklyn'),
    49:	('Debi Rose', 'Staten Island'),
}

html = '''
<h1>{{#_}}Choose Your Council District{{/_}}</h1>
'''

for borough in boroughs:
    html += f'''\n<h4>{{{{#_}}}}{borough}{{{{/_}}}}</h4>\n'''
    for district, (member, distborough) in sorted(districts.items(), key=lambda i: i[0]):
        if borough not in distborough:
            continue

        for feature in collection['features']:
            if int(feature['properties']['CounDist']) == district:
                break

        shape = geometry.shape(feature['geometry'])
        bounds = shape.bounds
        center_x = str((bounds[0] + bounds[2]) / 2)[:13]
        center_y = str((bounds[1] + bounds[3]) / 2)[:13]
        neighborhoods = ''
        html += f'''<p class="district-item"><a rel="internal" href="/14/{center_y}/{center_x}">{{{{#_}}}}District{{{{/_}}}} {district}</a>: {member}<br><small>{neighborhoods}</small></p>\n'''

print(html)
