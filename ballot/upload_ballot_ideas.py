#!/usr/bin/env python3

"""
Usage:
-----

First, ensure that you have set SHAREABOUTS_FLAVOR, SHAREABOUTS_DATASET_ROOT,
SHAREABOUTS_USERNAME, and SHAREABOUTS_PASSWORD.

    foreman run ballot/upload_ballot_ideas.py [BALLOT_IDEAS_CSV_FILE] > [OUTPUT_CSV_FILE]

    e.g., foreman run ballot/upload_ballot_ideas.py ~/Downloads/PBNYC\ FY19\ Ballot\ -\ Form\ Responses\ 1.csv

"""

import csv
import json
import os
from os.path import dirname, join as pathjoin, pardir
import requests
import sys
import time
import yaml


def get_categories():
    """
    Get a map from category labels to location_type values. Requires environment
    variable SHAREABOUTS_FLAVOR to be set.
    """
    FLAVORDIR = pathjoin(dirname(sys.argv[0]), pardir, 'src', 'flavors', os.environ['SHAREABOUTS_FLAVOR'])
    configname = pathjoin(FLAVORDIR, 'config.yml')
    with open(configname) as configfile:
        config = yaml.load(configfile)

    category_map = {}
    for location_type, typeconfig in config['place_types'].items():
        if not location_type.endswith('shortlisted'):
            continue
        label = typeconfig['label'].strip('_()')
        category_map[label] = location_type

    return category_map


def prep_geojson():
    infilename = sys.argv[1]
    with open(infilename, 'rU') as infile:
        reader = csv.DictReader(infile)
        data = list(reader)

    CATEGORYMAP = get_categories()
    CATEGORYMAP['Arts, Culture and Community Facilities'] = 'culture-shortlisted'
    CATEGORYMAP['Education'] = 'education-shortlisted'
    CATEGORYMAP['Streets'] = 'streets-shortlisted'
    CATEGORYMAP['Transit'] = 'transit-shortlisted'

    # Transform
    features = []
    for row in data:
        coords = [c.strip() for c in row.pop('Mapping Location').split(',')]
        coords = [float(coords[1]), float(coords[0])]

        row['shortlisted'] = True
        row['location_type'] = CATEGORYMAP[row.pop('Category ')]
        row['Title'] = row.pop('Project Title ')
        district = [d.strip() for d in row.pop('Council District')[len('District '):].split(',')]
        row['CounDist'], row['CounPerson'] = district
        row['Location'] = row.pop('Location ')
        row['Description'] = row.pop('Description ')

        feature = {
            'type': 'Feature',
            'properties': row,
            'geometry': {'type': 'Point', 'coordinates': coords}
        }
        features.append(feature)

    return features


def write_csv(data):
    writer = csv.DictWriter(sys.stdout, fieldnames=data[0]['properties'].keys())
    writer.writeheader()
    writer.writerows(f['properties'] for f in data)


def log(s, **k):
    print(s, file=sys.stderr, **k)


def request_with_retry(session, method, *args, **kwargs):
    retries = 10

    requestfunc = getattr(session, method.lower())
    while retries:
        response = requestfunc(*args, **kwargs)
        if 200 <= response.status_code < 400:
            return response
        else:
            log('Got an error: {}'.format(response.status_code))
            for arg in args:
                log(arg)
            for key, arg in kwargs.items():
                log('{}={!r}'.format(key, arg))
            retries -= 1
            time.sleep(0.5)
    sys.exit(1)



if __name__ == '__main__':
    data = prep_geojson()

    username = os.environ['SHAREABOUTS_USERNAME']
    password = os.environ['SHAREABOUTS_PASSWORD']
    session = requests.Session()
    session.auth = (username, password)
    session.headers.update({'x-shareabouts-silent': 'true'})
    session.headers.update({'content-type': 'application/json'})

    dataset = os.environ['SHAREABOUTS_DATASET_ROOT']
    places = pathjoin(dataset, 'places')
    for feature in data:
        query = feature['properties'].copy()
        for key in list(query.keys()):
            if key not in ('CounDist', 'location_type', 'Title'):
                query.pop(key)
        log('Checking for feature with title "{}"...'.format(query['Title']))
        response = request_with_retry(session, 'get', places, params=query)

        features = response.json()['features']
        featurejson = json.dumps(feature)
        if features:
            feature['id'] = features[0]['id']
            log('Updating existing place {}...'.format(feature['id']), end='')
            saveurl = pathjoin(places, str(feature['id']))
            saveresponse = session.patch(saveurl, data=featurejson)
        else:
            log('Saving new place...', end='')
            saveurl = places
            saveresponse = session.post(saveurl, data=featurejson)
        log('Done.')
