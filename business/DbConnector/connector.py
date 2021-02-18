from pymongo import MongoClient


class BDConnector:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        # refers to db name
        self.db = self.client.test



