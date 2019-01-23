from pymongo import MongoClient
from exceptions import WrongFormatError
from consts import  constants


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

    def get_open_questions(self):
        return list(self.collection.find({constants['TYPE_KEY']: constants['OPEN_QUESTION_KEY']}))

    def get_closed_questions(self):
        return list(self.collection.find({constants['TYPE_KEY']: constants['CLOSED_QUESTION_KEY']}))

    def delete_question(self, content):
        self.collection.delete_many({constants['CONTENT_KEY']: content})





