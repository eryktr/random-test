from pymongo import MongoClient
from exceptions import WrongFormatError


class DBService:
    def __init__(self, ip, port, dbname, collection, user, password):
        client = MongoClient(ip, port)
        client[dbname].authenticate(user, password, dbname)
        self.db = client[dbname]
        self.collection = self.db[collection]

    def insert(self, question : dict):
        if 'content' not in question: raise WrongFormatError
        if 'type' not in question: raise WrongFormatError
        self.collection.insert_one(question)

    def getOpenQuestions(self):
        return self.collection.find({'type':'open'})

    def getClosedQuestions(self):
        return self.collection.find({'type':'open'})


# db = DBService("127.0.0.1", 27017, "questions", "questions", "testuser", "12345")




