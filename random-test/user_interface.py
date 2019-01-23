from dbservice import DBService
import commands

class UserInterface:

    def __init__(self):
        print("Please, fill in database information: ")
        ip = input("IP: ")
        port = int(input("Port: "))
        dbname = input("Database name: ")
        collection = input("Collection name: ")
        user = input("Username: ")
        password = input("Password: ")

        self.again = True
        self.db_service = DBService(ip, port, dbname, collection, user, password)
        self.commands = {
            '0': commands.IllegalChoiceCommand(self.db_service),
            '1': commands.AddQuestionCommand(self.db_service),
            '2' : commands.ExitCommand(self.db_service)
        }

    def run(self):
        while True:
            print("[1] Add question")
            print("[2] Exit")
            choice = input("Choice: ")
            self.commands.get(choice, 0).execute()

ui = UserInterface()
ui.run()
