from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import sys
from sensor.logger import logging

def get_client():
    try:
        logging.info("we are trying to create a mongo db client")
        mongodb_client   = MongoDBClient(s)
        print(mongodb_client.database.list_collection_names())
    except Exception as e:
        logging.error("issue in creating the mongo db client")
        logging.error(f"{SensorException(e,sys)}")
        raise SensorException(e,sys)


if __name__ == '__main__':
    try:
        get_client()
    except Exception as e:
        print(e)