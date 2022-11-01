from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline


if __name__ == '__main__':
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()


    except Exception as e:
        print(e)