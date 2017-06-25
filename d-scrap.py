import requests
import json
import os
import pandas as pd

key=os.environ['K1']

ep = "https://maps.googleapis.com/maps/api/place/textsearch/json"

token = True
next_page_token = None
d = []

n = 0
while token and (n < 1):
    print('Requesting #{}'.format(n))
    r = requests.get(ep, params = {"query":"restaurants in SS15", "key":key, 'next_page_token':next_page_token})
    token = r.json().get('next_page_token')
    next_page_token = token

    result = r.json().get('results')
    d.append(result)
    
    n += 1

# j = json.dumps(d, indent= 2)
j = d.json()

df = pd.read_json(j)
print(df.head())

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