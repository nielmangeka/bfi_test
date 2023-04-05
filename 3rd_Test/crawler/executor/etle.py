import requests
import json
from datetime import datetime
from utils.api import EtleApi
from utils.postgress import PostgresUtils

class EtleExecutor():
    
    def get_etle_data(self):
        etle_api_util = EtleApi()
        postgres_ingestion = PostgresUtils()

        etle_api_util = etle_api_util.etle_data()
        if etle_api_util:
            print('Success get data from ETLE API')
        
        print('Start to Ingest data to Postgres')
        postgres_ingestion_util = postgres_ingestion.upload_to_db(etle_api_util)
        print('Success load data to Postgres')

        
        return etle_api_util
    
    def run(self):
        etle_data = self.get_etle_data()
        