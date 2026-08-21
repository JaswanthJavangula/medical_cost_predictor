from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from src.components.data_ingestion import DataIngestion

tp_config = TrainingPipelineConfig()
di_config = DataIngestionConfig(tp_config)
ingestion = DataIngestion(di_config)
artifact = ingestion.initiate_data_ingestion()
print(artifact)