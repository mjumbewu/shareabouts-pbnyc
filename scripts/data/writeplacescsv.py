#!/usr/bin/env python3

"""
Required python-dateutil, shapely
"""

import collections
import csv
from dateutil.parser import parse
import json
import os
import pathlib
import pytz
from request_utils import download_all_pages
import requests
import shapely.geometry
import sys


USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

session = requests.Session()
session.auth = (USERNAME, PASSWORD)
session.headers = {'content-type': 'application/json', 'x-shareabouts-silent': 'true'}

# Update the DATASET_URL with the root URL of the dataset. There are a few ways
# you can find the root URL.
DATASET_URL = 'https://shareaboutsapi.poepublic.com/api/v2/pbnyc/datasets/cycle12'

IDEAS_URL = DATASET_URL + '/places?include_private=True&include_invisible=True'
ET = pytz.timezone('US/Eastern')

# Load in the data
idea_pages = download_all_pages(IDEAS_URL, session=session)

def load_features(path):
    with path.open() as f:
        features = json.load(f)["features"]

    for feature in features:
        g = feature['geometry']
        feature['geometry'] = shapely.geometry.shape(g)
    
    return features

# Load active districts data
active_districts_path = pathlib.Path(__file__).resolve().parent.parent.parent / 'data' / 'districts.geojson'
active_districts = load_features(active_districts_path)

# Load all districts data
all_districts_path = pathlib.Path(__file__).resolve().parent.parent.parent / 'data' / 'alldistricts-clean.geojson'
all_districts = load_features(all_districts_path)

# Load boroughs data
boroughs_path = pathlib.Path(__file__).resolve().parent.parent.parent / 'data' / 'Borough Boundaries.geojson'
boroughs = load_features(boroughs_path)

def find_feature(g, features, default=None):
    assert g['type'] == 'Point'

    point = shapely.geometry.shape(g)
    for feature in features:
        if feature['geometry'].contains(point):
            break
    else:
        feature = default

    return feature

# Transform the data
rows = []
fields = collections.OrderedDict([
    ('Title', 'name'),
    ('Description', 'description'),
    ('Category', 'location_type'),
    ('Submitted', lambda f: parse(f['properties']['created_datetime']).astimezone(ET).isoformat()[:19].replace('T', ' ')),
    ('Comment count', lambda f: f['properties']['submission_sets'].get('comments', {}).get('length', 0)),
    ('Support count', lambda f: f['properties']['submission_sets'].get('support', {}).get('length', 0)),
    ('URL', lambda f: f"http://ideas.pbnyc.org/place/{f['properties']['id']}"),

    ('Approximate Address', lambda f: f['properties'].get('location', '')),
    ('Latitude', lambda f: f['geometry']['coordinates'][1]),
    ('Longitude', lambda f: f['geometry']['coordinates'][0]),
    ('Borough', lambda f: find_feature(f['geometry'], boroughs, {}).get('properties', {}).get('boro_name')),
    ('District', lambda f: find_feature(f['geometry'], all_districts, {}).get('properties', {}).get('CounDist')),
    ('Council Member', lambda f: find_feature(f['geometry'], active_districts, {}).get('properties', {}).get('CounPerson')),

    ('Submitter', lambda f: f['properties'].get('submitter_name') or f['properties']['submitter']['name']),
    ('Submitter Email', 'private-email'),

    ('Hidden', lambda f: not f['properties']['visible']),

    # ('Already submitted personal info', 'private-completed_personal_info_survey'),
    # ('Previous participant', 'private-previous_participant'),
    # ('Civically involved', 'private-other_civic_participant'),
    # ('Municipal election voter', 'private-municipal_election_voter'),
    # ('Heard about PB from...', lambda f: ', '.join(f['properties'].get('heard_about_pb')) if isinstance(f['properties'].get('heard_about_pb'), list) else f['properties'].get('heard_about_pb')),
    # ('Other-source detail', 'heard_about_pb-other-detail'),
    # ('Age', 'private-age'),
    # ('Gender', 'private-gender'),
    # ('Other-gender detail', 'private-gender-other-detail'),
    # ('Race', lambda f: ', '.join(f['properties'].get('private-race')) if isinstance(f['properties'].get('private-race'), list) else f['properties'].get('private-race')),
    # ('Education', 'private-education'),
    # ('Household income', 'private-income'),
    # ('ZIP', 'private-zip'),

])
for page in idea_pages:
    for feature in page['features']:
        if feature['properties']['created_datetime'] < '2022-10-18':
            row = {key: getter(feature) if callable(getter) else feature['properties'].get(getter, '') for key, getter in fields.items()}
            rows.append(row)

writer = csv.DictWriter(sys.stdout, fieldnames=fields.keys())
writer.writeheader()
writer.writerows(rows)
