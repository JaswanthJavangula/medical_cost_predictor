import os, sys
from typing import List
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from src.logging.logger import logging
from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sklearn.model_selection import train_test_split
from src.exception.exception import MedicalCostException
from src.entity.artifact_entity import DataIngestionArtifact

load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

#jessyhima4_db_user
#vrxFwp3Y5lrCYndp


class DataIngestion:
    def __init__(self, DataIngestionConfig: DataIngestionConfig):
        self.data_ingestion_config = DataIngestionConfig

    def export_collection_as_dataframe(self):
        try:
            self.client = pymongo.MongoClient(mongo_db_url)
            db = self.data_ingestion_config.ingestion_database_name
            collection = self.data_ingestion_config.ingestion_collection_name
            collection = self.client[db][collection]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns =["_id"], inplace=True)
            df.replace({"na":np.nan}, inplace =True)
            return df
        except Exception as e:
            raise MedicalCostException(e, sys)

    def export_data_into_feature_store(self, dataframe : pd.DataFrame):
        try:
            feature_store_dir = self.data_ingestion_config.feature_store_dir
            #creating folder
            dir_path = os.path.dirname(feature_store_dir)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_dir, index=False, header=True)
            return dataframe
        except Exception as e:
            raise MedicalCostException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(dataframe, test_size =self.data_ingestion_config.ingestion_train_split_ratio, random_state=42)
            dir_path = os.path.dirname(self.data_ingestion_config.ingested_train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.ingested_train_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.ingested_test_file_path, index=False, header=True)
            logging.info(f"Train test split is done. Train file: {self.data_ingestion_config.ingested_train_file_path} and Test file: {self.data_ingestion_config.ingested_test_file_path}")
        except Exception as e:
            raise MedicalCostException(e, sys)
        
    def initiate_data_ingestion(self):
        try:
            df = self.export_collection_as_dataframe()
            df =self.export_data_into_feature_store(dataframe=df)
            self.split_data_as_train_test(dataframe=df)
            data_ingestion_artifact = DataIngestionArtifact(ingested_train_file_path=self.data_ingestion_config.ingested_train_file_path,
                                                            ingested_test_file_path=self.data_ingestion_config.ingested_test_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise MedicalCostException(e, sys)
    