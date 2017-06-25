from database import Query
import pandas as pd

DATASET = 'dataset/df.csv'

def main():
    db = pd.read_csv(DATASET)
    q = Query(db) # Initialize Query class
    q.execute() # Run query instance

if __name__ == '__main__':
    main()
