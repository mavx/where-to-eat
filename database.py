"""Class to query CSV database"""

import csv
import pandas as pd



class Database(object):
    def __init__(self, filename):
        # Import CSV file as DataFrame
        self.db = pd.read_csv(filename)

    def preview(self):
        # Previews the DataFrame
        print(self.db.head())
    
    def columns(self):
        cols = self.db.columns
        print('Columns in DB:')
        [print(n, c) for n, c in enumerate(cols)]

    def query(
        self, name=None
    ):
        """Query DF column `name` for matching string"""
        df = self.db
        if name is not None:
            print(f'Searching for {name} in `name`..')
            # Search for row with `name` like ...
            condition = df['name'].str.contains(name, case=False)
        else:
            # Prompt user for input
            name = input('Search for a restaurant name: ')
            condition = df['name'].str.contains(name, case=False)
        
        # Filter DF for matching conditions
        results = df[condition].values.tolist()
        # print(results, '\n')
        
        
        for n, r in enumerate(results):
            if n < 10:
                print(n, r)
            else:
                break

    
    # def query_v2(self, args={}):
    #     """Query DF columns for all matching conditions"""
        



if __name__ == '__main__':
    # q = Database('dataset/test.csv')
    q = Database('df.csv')
    # q.preview()
    q.columns()
    q.query(name='Res')
    q.query(name='mus')
    q.query(name='jibby')
    q.query(name='yesterday')
    q.query()
