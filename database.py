"""Class to query CSV database"""
import csv
import pandas as pd

class Database(object):
    """Database class for interacting with database source"""
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
    
    def parse_record(self, record):
        """Outputs DF record in a neater format"""
        template = """
        Name: {name}
        Types: {types}
        Address: {address}
        Opening Hours: {open_hours}
        Price: {price}
        Rating: {rating}
        LatLong: {latlong}
        """

        return template.format(
            name=record.get('name'),
            types=record.get('types'),
            address=record.get('formatted_address'),
            open_hours=record.get('opening_hours'),
            price=record.get('price_level'),
            rating=record.get('rating'),
            latlong='{}, {}'.format(
                record.get('latitude'), record.get('longitude')
            )
        )

    def query(
        self, name=None
    ):
        """Query DF column `name` for matching string"""
        df = self.db
        if name is not None:
            print('Searching for "{}" in `name`..'.format(name))
            # Search for row with `name` like ...
            condition = df['name'].str.contains(name, case=False) # Case-insensitive
        else:
            # Prompt user for input
            name = input('Search for a restaurant name: ')
            condition = df['name'].str.contains(name, case=False)
        
        # Filter DF for matching conditions
        results = df[condition]
        n = 5
        print('Found {} results, printing first {}:'.format(len(results), n))
        for index, row in results[:n].iterrows():
            print(self.parse_record(row))
    
    # def query_v2(self, args={}):
    #     """Query DF columns for all matching conditions"""
        

if __name__ == '__main__':
    # q = Database('dataset/test.csv')
    q = Database('df.csv')
    # q.preview()
    # q.columns()
    # q.query(name='Restaurant')
    q.query(name='Restaurant')
