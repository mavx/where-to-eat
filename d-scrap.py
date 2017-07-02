import requests
import json
import os
import pandas as pd

key=os.environ['K1']

ep = "https://maps.googleapis.com/maps/api/place/textsearch/json"

token = True
next_page_token = None
d = []


def query(token):
    r = requests.get(ep, params = {"query":"restaurants in SS15", "key":key, "pagetoken":token})
    print('SENT REQUEST:', r.url)
    return r.json()

n = 0
while token and (n < 2):
    print('Requesting #{}'.format(n))
    # print(token)
    # r = requests.get(ep, params = {"query":"restaurants in SS15", "key":key, "pagetoken":next_page_token})
    # print('SENT REQUEST:', '\n\n{}\n\n'.format(r.url))
    j = query(next_page_token)
    print('RESULTS:', j)
    # token = r.json().get('next_page_token')
    # print(r.json().keys())
    # print(r.json())
    token = j.get('next_page_token', 'NIGGA')
    next_page_token = token
    # print(token)

    result = j.get('results')
    # print(result)
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