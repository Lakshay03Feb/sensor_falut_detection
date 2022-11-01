import sys
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:

    def __init__(self) -> None:
        self.traininig_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(self.traininig_pipeline_config)

    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("starting data ingestion")
            logging.info("data ingestion completed")
        except Exception as e:
            raise SensorException(e,sys)


    def start_data_validatiohn(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact : DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)