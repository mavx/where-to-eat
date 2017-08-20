"""Class to query CSV database"""
import csv
import pandas as pd    

class Query(object):
    """Initialize instance with Pandas DataFrame as input"""
    def __init__(self, filename):
        # Take dataframe as database
        self.db = pd.read_csv(filename)
    
        # Setup individual functions
        def query_name(df, name):
            try:
                return df[df['name'].str.contains(name, case=False)]
            except:
                return df
        
        def min_rating(df, decimal):
            try:
                return df[df['rating'] >= decimal]
            except:
                return df

        self.queries = {
            'name': query_name,
            'rating': min_rating
        }
    
    def columns(self):
        """Prints columns in DB"""
        cols = self.db.columns
        print('Columns in DB:')
        [print(n, c) for n, c in enumerate(cols)]
    
    def build(self):
        """Build the parameters to be used with final query
        Creates:
            Dictionary of parameters by corresponding criteria (column)
        """
        # Initialize a class instance that is reusable within a session
        self.params = {}

        # Validate inputs
        req_name = input('Input a restaurant name (any keyword): ')
        if isinstance(req_name, str):
            self.params['name'] = req_name

        req_rating = input("What is the minimum rating? (1.0 - 5.0): ")
        if req_rating.replace('.', '').isdigit():
            self.params['rating'] = float(req_rating)
    
    def parse_record(self, record):
        """Outputs DF record in a neater format"""
        template = (
            "Name: {name}\n"
            "Types: {types}\n"
            "Address: {address}\n"
            "Opening Hours: {open_hours}\n"
            "Price: {price}\n"
            "Rating: {rating}\n"
            "LatLong: {latlong}\n"
        )

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
    
    def query(self, req_name, req_rating):
        """Query database with structured params
        Args:
            req_name (str): searchable text within a venue name
            req_rating (str): minimum rating of a venue
        Returns:
            Results in a blob of text
        """
        results = self.db
        params = {}

        # Validate inputs
        if isinstance(req_name, str):
            params['name'] = req_name
        else:
            print('something wrong with name')

        if req_rating.replace('.', '').isdigit():
            params['rating'] = float(req_rating)
        else:
            print('something wrong with rating')

        # Iterate query functions over results
        print('Quering DB with params: {}'.format(params))
        for p in params:
            print('iterating...')
            results = self.queries[p](results, params[p])

        results.sort_values(by=['rating'], ascending=False, inplace=True)

        all_results = []
        if len(results) > 0:
            n = min(5, len(results))
            print('Found {} results, printing first {}:'.format(len(results), n))
            for index, row in results[:n].iterrows():
                # print(self.parse_record(row))
                all_results.append(self.parse_record(row))
        else:
            print('No results.')
        
        return all_results


if __name__ == '__main__':
    filename = 'dataset/df.csv'
    q = Query(filename)
    results = q.query('silva', '4.0')
    print(results)
