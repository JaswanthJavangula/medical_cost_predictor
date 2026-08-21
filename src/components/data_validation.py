import os, sys
from typing import List
import pandas as pd
import numpy as np
from src.logging.logger import logging
from src.exception.exception import MedicalCostException

from src.entity.config_entity import DataValidationConfig, TrainingPipelineConfig, DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from utils.main_utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(self.data_validation_config.schema_file_path)
        except Exception as e:
            raise MedicalCostException(e, sys)
    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MedicalCostException(e, sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame)-> bool:
        try:
            num_of_cols = len(self._schema_config['columns'])
            logging.info(f"Required number of columns: {num_of_cols}. Dataframe has columns: {len(dataframe.columns)}")
            if len(dataframe.columns) == num_of_cols:
                return True
            return False
        except Exception as e:
            raise MedicalCostException(e, sys)
    logging.info(f" Validated Number of COL")

    def validate_columns_exist_in_df (self, dataframe: pd.DataFrame)-> list:
        try:
            missing_cols =[]
            for col in self._schema_config['columns'].keys():
                if col not in dataframe.columns:
                    missing_cols.append(col)
            return missing_cols
        except Exception as e:
            raise MedicalCostException(e, sys)

    def detect_data_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, threshold: float = 0.05)->dict:
        try:
            status = True
            report = {}
            for col in base_df.columns:
                d1 = base_df[col]
                d2 = current_df[col]
                is_same_dist = ks_2samp(d1, d2)
                if threshold < is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({col: {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found
                }})
            drift_report_file_path = self.data_validation_config.data_validation_drift_report_dir
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path= drift_report_file_path, content=report)
            return status
        except Exception as e:
            raise MedicalCostException(e, sys)

    def initiate_data_validation
