from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
import os, sys
from pandas import DataFrame



class DataIngestion:

    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    
    def export_data_into_feature_store(self)-> DataFrame:
        """
        Export the data from MongoDB collection as dataframe into feature store
        """
        pass

    def split_data_as_train_test_split(self, dataframe:DataFrame):
        """
        Feature store dataset will be split into train and test file
        """
        pass
    

    