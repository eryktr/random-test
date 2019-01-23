from dbservice import DBService
from exceptions import NotEnoughClosedQuestionsError, NotEnoughOpenQuestionsError, WrongFormatError
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
            '0': lambda : commands.illegal_choice_command(),
            '1': lambda : commands.add_question_command(self.db_service),
            '2' : lambda : commands.delete_command(self.db_service),
            '3': lambda : commands.create_random_test_command(self.db_service),
            '9': lambda: commands.exit_command()
        }

    def run(self):
        while True:
            print("[1] Add question")
            print("[2] Exit")
            print("[2] Delete question")
            print("[3] Generate random test")
            choice = input("Choice: ")
            try:
                self.commands.get(choice, self.commands['0'])()
            except NotEnoughOpenQuestionsError:
                print("Not enough open questions.")
            except NotEnoughClosedQuestionsError:
                print("Not enough closed questions.")
            except ValueError:
                print("Incorrect data.")

ui = UserInterface()
ui.run()
