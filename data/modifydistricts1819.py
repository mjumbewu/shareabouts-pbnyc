#!/usr/bin/env python3

import json

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

with open('alldistricts.geojson') as jsonfile:
    indata = json.load(jsonfile)

outdata = {attr:indata[attr] for attr in indata if attr != 'features'}
outdata['features'] = []

for infeature in indata['features']:
    district_id = infeature['properties']['CounDist']
    if district_id in districts:
        outfeature = infeature.copy()
        outfeature['properties']['CounPerson'] = districts[district_id][0]
        outfeature['properties']['Borough'] = districts[district_id][1]
        outdata['features'].append(outfeature)

with open('districts.geojson', 'w') as jsonfile:
    json.dump(outdata, jsonfile)
