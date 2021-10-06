from airtable import Airtable 
import os
#from essay_app import app
import itertools
from requests.exceptions import HTTPError


AT_API_KEY = "AT_API_KEY"
AT_BASE_ID = "appobvoowf7mz8RYD"
table_name = "essays"

try:
    at_api_key = str(os.environ.get(AT_API_KEY))
except (FileNotFoundError,RuntimeError) as e:
    print('Fucked up with Airtable API key ')
    

COLUMNS = ['Demo ID',
            'Essay',
            'ML Score',
            'Self Assessed Score'
            ]

essay_airtable = Airtable(AT_BASE_ID, table_name, at_api_key)

try:
    essay_airtable.get_all(fields=COLUMNS)
except HTTPError:
    print('WARNING @Initation: Mismatching columns')

def insert_record(args):
    if len(COLUMNS) != len(args):
        print("WARNING @Insert: Mismatching columns")
    
    data = dict(zip(COLUMNS, args))
    print(f'Data pushed is: {data}')
    try:
        response = essay_airtable.insert(data)
        print("Pushed to Airtable")
    except Exception as e:
        print(f"Error: {e}")
        response = e

    return response
        
