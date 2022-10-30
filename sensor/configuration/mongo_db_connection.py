import pymongo
# from sensor.constants.database import DATABASE_NAME

import certifi
ca =  certifi.where()


class MongoDBClient:
    client = None
    def __init__(self,database_name = "ineuron") -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://lakshay03:limit123456@cluster0.ryyuevc.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e


if __name__ == '__main__':
    client = MongoDBClient()