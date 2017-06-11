import requests
import json

key="AIzaSyDMEfxL5n4WP0r3zojDU8fN7dM37Q8HBSc"
key2='AIzaSyDIhBPrraLRN3Z57zi3lSkziu7B0HxhAKY'

ep = "https://maps.googleapis.com/maps/api/place/textsearch/json"

token = True
next_page_token = None
d = {}

# file = open('database.txt','a')
with open('database.txt', 'a') as f:
    while token:
        r = requests.get(ep, params = {"query":"restaurants in SS15", "key":key, 'next_page_token':next_page_token})
        # for item in r.json().get('results'):
        # print(r.ok)
        # print(r.json())
        token = r.json().get('next_page_token')
        next_page_token = token

        result = r.json().get('results')
        if token != None:
            for item in result:
                f.write('{},'.format(json.dumps(item)))
        else:
            f.write('{}'.format(json.dumps(item)))
        