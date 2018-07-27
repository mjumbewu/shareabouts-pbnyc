import json
import collections

f = open('alldistrict-centroids-downloaded.geojson')
data = json.load(f)

d = collections.defaultdict(list)
for feat in data['features']:
    id = int(feat['properties']['CounDist'])
    feat['properties']['CounDist'] = id
    d[id].append(feat)

features = []
for id, feats in d.items():
    feats[0]['properties'].pop('marker-color', None)
    feats[0]['properties'].pop('marker-size', None)
    feats[0]['properties'].pop('marker-symbol', None)

    points = []
    for feat in feats:
        if feat['geometry']['type'] == 'MultiPoint':
            points.extend(feat['geometry']['coordinates'])
        else:
            points.append(feat['geometry']['coordinates'])

    newfeat = {
        'type': 'Feature',
        'id': id,
        'properties': feats[0]['properties'],
        'geometry': {
            'type': 'MultiPoint',
            'coordinates': points
        }
    }
    features.append(newfeat)

features = list(sorted(features, key=lambda feat: feat['id']))

print(json.dumps({
    'type': 'FeatureCollection',
    'features': features
}, indent=1))
