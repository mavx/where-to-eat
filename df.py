import json
import pandas as pd

df = pd.read_json("database.json")

def fn1(val):
    return val['location']['lat']

def fn2(val):
    return val['location']['lng']

df['latitude'] = df['geometry'].apply(fn1, 1)
df['longitude'] = df['geometry'].apply(fn2, 1)
df2 = df.drop(['geometry'], axis = 1)
df2.drop(['icon'], axis = 1, inplace = True)
df2.drop(['photos'], axis = 1, inplace = True)
df2.drop(['reference'], axis = 1, inplace = True)
df2.drop(['id'], axis = 1, inplace = True)

df2.to_csv('df.csv')