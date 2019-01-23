import abc
from consts import constants
from dbservice import DBService

class Command(metaclass=abc.ABCMeta):

    def __init__(self,  dbservice : DBService):
        self.db_service = dbservice

    @abc.abstractmethod
    def execute(self):
        pass


class AddOpenQuestionCommand(Command):

    def __init__(self, dbservice : DBService):
        super(Command).__init__(AddOpenQuestionCommand, dbservice)

    def execute(self):
        content = input("Question content: ")
        question = {
            constants['CONTENT_KEY'] : content,
            constants['TYPE_KEY'] : constants['OPEN_QUESTION_KEY']
        }
        self.db_service.insert(question)


class AddClosedQuestionCommand(Command):

    def _init__(self, dbservice : DBService):
        Command.__init__(self, dbservice)

    def execute(self):
        content = input("Question content: ")
        num_of_answers = int(input("Number of answers: "))
        answers = []
        for i in range (0, num_of_answers):
            answer = input("answer: ")
            answers.append(answer)
        question = {
            constants['CONTENT_KEY'] : content,
            constants['TYPE_KEY'] : constants['CLOSED_QUESTION_KEY'],
            constants['ANSWERS_KET'] : answers
        }
        self.db_service.insert(question)


class IllegalChoiceCommand(Command):
    def __init__(self, dbservice : DBService):
        Command.__init__(self, dbservice)

    def execute(self):
        print("Illegal choice.")


class AddQuestionCommand(Command):
    def __init__(self, dbservice : DBService):
        Command.__init__(self, dbservice)

    def execute(self):
        print("What kind of question would you like to add?")
        print("[1] - Open Question")
        print("[2] - Closed Question")
        choice = input("Choice: ")
        if choice == '1':
            command = AddOpenQuestionCommand(self.db_service)

        elif choice == '2':
            command = AddClosedQuestionCommand(self.db_service)

        else:
            command = IllegalChoiceCommand(self.db_service)

        command.execute()


class DeleteQuestionCommand(Command):

    def __init(self, dbservice : DBService):
        Command.__init__(self, dbservice)

    def execute(self):
        content = input("Content of the question to be deleted: ")
        self.db_service.deleteQuestion(content)

class ExitCommand(Command):

    def __init__(self, dbservice : DBService):
        Command.__init__(self, dbservice)

    def execute(self):
        print("Goodbye!")
        exit(0)