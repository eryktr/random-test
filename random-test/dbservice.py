from pymongo import MongoClient

class DBService:
    def __init__(self, ip, port, dbname, collection, user, password):
        client = MongoClient(ip, port)
        client[dbname].authenticate(user, password, dbname)
        self.db = client[dbname]
        self.collection = self.db[collection]

    def insert(self, question : dict):
        self.collection.insert_one(question)


