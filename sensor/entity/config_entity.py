from datetime import datetime
from sensor.constants.database import COLLECTION_NAME
from sensor.constants.training_pipeline import *

class TrainingPipelineConfig:

    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline_name:str = PIPELINE_NAME
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR,timestamp)
        self.timestamp:str = timestamp


class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingest_dir:str = os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path:str = os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME)
        self.training_file_path:str = os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
        self.test_file_path:str = os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
        self.train_test_split_ratio:float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str = COLLECTION_NAME
        
if __name__ == '__main__':
    training_pipe_line_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config= training_pipe_line_config)
    print(data_ingestion_config.__dict__)
        