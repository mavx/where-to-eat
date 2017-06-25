import requests
import json
import os

key=os.environ['K1']

ep = "https://maps.googleapis.com/maps/api/place/textsearch/json"

token = True
next_page_token = None
d = {}

with open('dataset/database.txt', 'w') as f:
    while token:
        r = requests.get(ep, params = {"query":"restaurants in SS15", "key":key, 'next_page_token':next_page_token})
        token = r.json().get('next_page_token')
        next_page_token = token

        result = r.json().get('results')
        if token != None:
            for item in result:
                f.write('{},'.format(json.dumps(item)))
        else:
            f.write('{}'.format(json.dumps(item)))
        