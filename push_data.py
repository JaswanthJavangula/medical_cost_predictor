import os, sys, json
import pymongo
import certifi
import pandas as pd
from src.exception.exception import MedicalCostException
from src.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

ca = certifi.where()

class DataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise MedicalCostException(e, sys)

    def csv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise MedicalCostException(e, sys)

    def push_data_to_mongo(self, records, db, collection):
        try:
            self.db = db
            self.collection = collection
            self.records = records
            client = pymongo.MongoClient(mongo_db_url)
            self.db = client[self.db]

            self.collection = self.db[self.collection]
            self.collection.insert_many(self.records)
            
            logging.info(f"Data pushed to MongoDB collection: {self.collection.name}")
            return (len(self.records))
        except Exception as e:

            raise MedicalCostException(e, sys)

if __name__ == "__main__":
    file_path = "medical_data/insurance.csv"
    database = "medical_insurance"
    collection = "cost_data"

    dataextract_obj = DataExtract()
    records = dataextract_obj.csv_to_json(file_path)
    logging.info(f"Number of records to be pushed: {len(records)}")
    num_records = dataextract_obj.push_data_to_mongo(records, database, collection)
    logging.info(f"Number of records pushed: {num_records}")
