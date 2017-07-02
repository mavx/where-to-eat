import requests
import json
import os
import pandas as pd
import time

key=os.environ['K1']

# token = True
# next_page_token = None
# d = []


def query(token):
    ep = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": "restaurants in SS15", 
        "key": key, 
        "pagetoken": token
    }
    r = requests.get(ep, params=params)
    print('SENT REQUEST:', r.url)
    print('REQUEST SUCCESSFUL:', r.ok)
    print('REQUEST STATUS:', r.json().get('status'))

    print('Printing items...')
    for item in r.json().get('results'):
        print(item.get('name'))

    return r.json()


token = None
n = 0
while n < 5:
    j = query(token)
    token = j.get('next_page_token')
    print('RETRIEVED TOKEN:', token)
    print(j.keys())

    n += 1
    print('\nPAUSING FOR 3 FREAKING SECONDS...')
    time.sleep(3) # Pause a while https://developers.google.com/places/web-service/search#PlaceSearchPaging
    if token is None:
        break

raise SystemExit

n = 0
while token and (n < 2):
    print('Requesting #{}'.format(n))
    j = query(next_page_token)
    print('RESULTS:', j)
    token = j.get('next_page_token', 'NIGGA')
    next_page_token = token

    result = j.get('results')
    d.append(result)
    
    n += 1

raise SystemExit



# j = json.dumps(d, indent= 2)
# prsint(d[0][0]['name'])
dd = {} #dictionary of database
for i , x in enumerate(d[0]):
    dd[d[0][i]['name']] = d[0][i]

print(len(dd))    

# df = pd.read_json(j)
# print(df.head())

# def fn1(val):
#     return val['location']['lat']

# def fn2(val):
#     return val['location']['lng']

# df['latitude'] = df['geometry'].apply(fn1, 1)
# df['longitude'] = df['geometry'].apply(fn2, 1)
# df2 = df.drop(['geometry'], axis = 1)
# df2.drop(['icon'], axis = 1, inplace = True)
# df2.drop(['photos'], axis = 1, inplace = True)
# df2.drop(['reference'], axis = 1, inplace = True)
# df2.drop(['id'], axis = 1, inplace = True)

# df2.to_csv('dataset/df.csv')