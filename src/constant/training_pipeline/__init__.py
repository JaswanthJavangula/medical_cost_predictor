import os
import sys
import numpy as np
from pathlib import Path

# ============ GENERAL ============
PIPELINE_NAME: str = "medical_insurance_prediction"
ARTIFACT_DIR: str = "artifacts"
TARGET_COLUMN: str = "charges"
MODEL_DIR: str = "final_models"

FILE_NAME: str = "insurance_data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH: str = os.path.join("data_schema", "schema.yaml")
SAVED_MODEL_DIR: str = os.path.join("saved_models")
MODEL_FILE_NAME: str = "model.pkl"

# ============ DATA INGESTION ============
DATA_INGESTION_COLLECTION_NAME: str = "cost_data"
DATA_INGESTION_DATABASE_NAME: str = "medical_insurance"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# ============ DATA VALIDATION ============
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

# ============ DATA TRANSFORMATION ============
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}
PREPROCESSOR_OBJECT_FILE_NAME: str = "preprocessor.pkl"

# ============ MODEL TRAINER ============
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.75
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD: float = 0.05

# ============ HYPERPARAMETERS ============
N_ESTIMATORS: int = 100
MAX_DEPTH: int = 5
LEARNING_RATE: float = 0.01
RANDOM_STATE: int = 42

# ============ FEATURES ============
CATEGORICAL_FEATURES: list = ["sex", "smoker", "region"]
NUMERICAL_FEATURES: list = ["age", "bmi", "children"]
ALL_FEATURES: list = CATEGORICAL_FEATURES + NUMERICAL_FEATURES

# ============ MODEL ARTIFACTS ============
SCALER_NAME: str = "scaler.pkl"
ENCODER_NAME: str = "encoder.pkl"