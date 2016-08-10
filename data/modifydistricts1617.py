import json

districts = {
    11: ('Andrew Cohen', 'Bronx'),
    22: ('Costa Constantinides', 'Queens'),
    36: ('Robert Cornegy', 'Brooklyn'),
    35: ('Laurie Cumbo', 'Brooklyn'),
    30: ('Elizabeth Crowley', 'Queens'),
    40: ('Mathieu Eugene', 'Brooklyn'),
    21: ('Julissa Ferreras', 'Queens'),
    44: ('David Greenfield', 'Brooklyn'),
    3:  ('Corey Johnson', 'Manhattan'),
    5:  ('Ben Kallos', 'Manhattan'),
    29: ('Karen Koslowitz', 'Queens'),
    39: ('Brad Lander', 'Brooklyn'),
    33: ('Steve Levin', 'Brooklyn'),
    7:  ('Mark Levine', 'Manhattan'),
    8:  ('Melissa Mark-Viverito', 'Manhattan_Bronx'),
    38: ('Carlos Menchaca', 'Brooklyn'),
    27: ('Daneek Miller', 'Queens'),
    34: ('Antonio Reynoso', 'Brooklyn_Queens'),
    31: ('Donovan Richards', 'Queens'),
    10: ('Ydanis Rodriguez', 'Manhattan'),
    6:  ('Helen Rosenthal', 'Manhattan'),
    15: ('Ritchie Torres', 'Bronx'),
    47: ('Mark Treyger', 'Brooklyn'),
    32: ('Eric Ulrich', 'Queens'),
    19: ('Paul Vallone', 'Queens'),
    26: ('Jimmy Van Bramer', 'Queens'),
    45: ('Jumaane Williams', 'Brooklyn'),
    16: ('Vanessa Gibson', 'Bronx'),
    17: ('Rafael Salamanca', 'Bronx'),
    49: ('Deborah Rose', 'Staten Island'),
    23: ('Barry Grodenchik', 'Queens'),
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
