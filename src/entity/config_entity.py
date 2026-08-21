from datetime import datetime
import os 
from src.constant import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_name: str = training_pipeline.ARTIFACT_DIR
        self.artifact_dir:str = os.path.join(self.artifact_name,timestamp)
        self.model_dir: str = os.path.join("final_models",timestamp)
        self.timestamp:str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_dir: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME)

        self.ingested_train_file_path: str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME)
        self.ingested_test_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME)

        self.ingestion_train_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.ingestion_collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.ingestion_database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)

        self.data_validation_valid_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.data_validation_valid__train_file_path: str = os.path.join(self.data_validation_valid_dir, training_pipeline.TRAIN_FILE_NAME)
        self.data_validation_valid__test_file_path: str = os.path.join(self.data_validation_valid_dir, training_pipeline.TEST_FILE_NAME)


        self.data_validation_invalid_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.data_validation_invalid_train_file_path: str = os.path.join(self.data_validation_invalid_dir, training_pipeline.TRAIN_FILE_NAME)
        self.data_validation_invalid_test_file_path: str = os.path.join(self.data_validation_invalid_dir, training_pipeline.TEST_FILE_NAME)

        self.data_validation_drift_report_dir = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
                                                             training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)

class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.data_transformation_dir_transformed_dir: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR)
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir_transformed_dir, training_pipeline.TRAIN_FILE_NAME.replace("csv", "npz"))
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir_transformed_dir, training_pipeline.TEST_FILE_NAME.replace("csv", "npz"))
        self.obj_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                           training_pipeline.PREPROCESSOR_OBJECT_FILE_NAME)

class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME)
        self.model_trainer_trained_model_dir: str = os.path.join(self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR, training_pipeline.MODEL_FILE_NAME)
        self.model_expected_score: float = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.model_overfitting_underfitting_threshold: float = training_pipeline.MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD
