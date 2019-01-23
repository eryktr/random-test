from dbservice import DBService

class UserInterface:

    def __init__(self):
        print("Please, fill in database information: ")
        ip = input("IP: ")
        port = input("Port: ")
        dbname = input("Database name: ")
        collection = input("Collection name: ")
        user = input("Username: ")
        password = input("Password")

        self.db_service = DBService(ip, port, dbname, collection, user, password)

