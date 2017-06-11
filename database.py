"""Class to query CSV database"""
import csv
import pandas as pd    

class Query(object):
    """Initialize instance with Pandas DataFrame as input"""
    def __init__(self, dataframe):
        # Take dataframe as database
        self.db = dataframe
    
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
        if req_rating.isdigit():
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

    def execute(self):
        """Executes functions in the query dictionary"""
        # Build the parameters by prompting for inputs
        self.build()
        results = self.db

        # Iterate query functions over results
        for p in self.params:
            if (self.params[p]) and (p in self.queries):
                results = self.queries[p](results, self.params[p])
        results.sort_values(by=['rating'], ascending=False, inplace=True)

        n = 5
        if len(results) > 0:
            n = min(5, len(results))
            print('Found {} results, printing first {}:'.format(len(results), n))
            for index, row in results[:n].iterrows():
                print(self.parse_record(row))
        else:
            print('No results.')


if __name__ == '__main__':
    db = pd.read_csv('df.csv')
    q = Query(db)
    q.execute()
    # q.columns()
